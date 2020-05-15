# -
# ==========================================================================
# Copyright (C) 1995 - 2006 Autodesk, Inc. and/or its licensors.  All
# rights reserved.
#
# The coded instructions, statements, computer programs, and/or related
# material (collectively the "Data") in these files contain unpublished
# information proprietary to Autodesk, Inc. ("Autodesk") and/or its
# licensors, which is protected by U.S. and Canadian federal copyright
# law and by international treaties.
#
# The Data is provided for use exclusively by You. You have the right
# to use, modify, and incorporate this Data into other products for
# purposes authorized by the Autodesk software license agreement,
# without fee.
#
# The copyright notices in the Software and this entire statement,
# including the above license grant, this restriction and the
# following disclaimer, must be included in all copies of the
# Software, in whole or in part, and all derivative works of
# the Software, unless such copies or derivative works are solely
# in the form of machine-executable object code generated by a
# source language processor.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
# AUTODESK DOES NOT MAKE AND HEREBY DISCLAIMS ANY EXPRESS OR IMPLIED
# WARRANTIES INCLUDING, BUT NOT LIMITED TO, THE WARRANTIES OF
# NON-INFRINGEMENT, MERCHANTABILITY OR FITNESS FOR A PARTICULAR
# PURPOSE, OR ARISING FROM A COURSE OF DEALING, USAGE, OR
# TRADE PRACTICE. IN NO EVENT WILL AUTODESK AND/OR ITS LICENSORS
# BE LIABLE FOR ANY LOST REVENUES, DATA, OR PROFITS, OR SPECIAL,
# DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES, EVEN IF AUTODESK
# AND/OR ITS LICENSORS HAS BEEN ADVISED OF THE POSSIBILITY
# OR PROBABILITY OF SUCH DAMAGES.
#
# ==========================================================================
# +

import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import sys

import polyModifier


def statusError(message):
	fullMsg = "Status failed: %s\n" % message
	sys.stderr.write(fullMsg)
	OpenMaya.MGlobal.displayError(fullMsg)
	raise  # called from exception handlers only, reraise exception


kPluginCmdName = "spSplitUV"
kPluginNodeTypeName = "spSplitUVNode"
kPluginNodeId = OpenMaya.MTypeId(0x87013)

#####################################################################
## COMMAND ##########################################################
#####################################################################

# Overview:
#
# 		The purpose of the splitUV command is to unshare (split) any selected UVs
# 		on a given object.
#
# How it works:
#
# 		This command is based on the polyModifierCmd. It relies on the polyModifierCmd
# 		to manage "how" the effects of the splitUV operation are applied (ie. directly
# 		on the mesh or through a modifier node). See polyModifier.py for more details
#
# 		To understand the algorithm behind the splitUV operation, refer to splitUVFty
#
# Limitations:
#
# 		(1) Can only operate on a single mesh at a given time. If there are more than one
# 			mesh with selected UVs, only the first mesh found in the selection list is
# 			operated on.
#


class splitUV(polyModifier.polyModifierCmd):

	def __init__(self):
		polyModifier.polyModifierCmd.__init__(self)
		# Selected UVs
		#
		# Note: The MObject, fComponentList, is only ever accessed on a single call to the plugin.
		# 		 It is never accessed between calls and is stored on the class for access in the
		# 		 overriden initModifierNode() method.
		#
		self.__fComponentList = OpenMaya.MObject()
		self.__fSelUVs = OpenMaya.MIntArray()
		self.__fSplitUVFactory = splitUVFty()

	def isUndoable(self):
		return True

	def doIt(self, args):
		"""
		implements the scripted splitUV command.

		Arguments:
			args - the argument list that was passes to the command from MEL
		"""
		# Parse the selection list for objects with selected UV components.
		# To simplify things, we only take the first object that we find with
		# selected UVs and operate on that object alone.
		#
		# All other objects are ignored and return warning messages indicating
		# this limitation.
		#
		selList = OpenMaya.MSelectionList()
		OpenMaya.MGlobal.getActiveSelectionList(selList)
		selListIter = OpenMaya.MItSelectionList(selList)

		# The splitUV node only accepts a component list input, so we build
		# a component list using MFnComponentListData.
		#
		# MIntArrays could also be passed into the node to represent the uvIds,
		# but are less storage efficient than component lists, since consecutive 
		# components are bundled into a single entry in component lists.
		#
		compListFn = OpenMaya.MFnComponentListData()
		compListFn.create()
		found = False
		foundMultiple = False

		while not selListIter.isDone():
			dagPath = OpenMaya.MDagPath()
			component = OpenMaya.MObject()
			itemMatches = True
			selListIter.getDagPath(dagPath, component)

			# Check for selected UV components
			#
			if itemMatches and (component.apiType() == OpenMaya.MFn.kMeshMapComponent):
				if not found:  
					# The variable 'component' holds all selected components on the selected
					# object, thus only a single call to MFnComponentListData::add() is needed
					# to store the selected components for a given object.
					#
					compListFn.add(component)

					# Copy the component list created by MFnComponentListData into our local
					# component list MObject member.
					#
					self.__fComponentList = compListFn.object()

					# Locally store the actual uvIds of the selected UVs so that this command
					# can directly modify the mesh in the case when there is no history and
					# history is turned off.
					#
					compFn = OpenMaya.MFnSingleIndexedComponent(component)
					compFn.getElements(self.__fSelUVs)

					# Ensure that this DAG path will point to the shape of our object.
					# Set the DAG path for the polyModifierCmd.
					#
					dagPath.extendToShape()
					self._setMeshNode(dagPath)
					found = True
				else:
					# Break once we have found a multiple object holding selected UVs, since
					# we are not interested in how many multiple objects there are, only
					# the fact that there are multiple objects.
					#
					foundMultiple = True
					break

			selListIter.next()

		if foundMultiple:
			self.displayWarning("Found more than one object with selected UVs - Only operating on first found object.")

		# Initialize the polyModifierCmd node type - mesh node already set
		#
		self._setModifierNodeType(kPluginNodeId)

		if found:
			if self.__validateUVs():
				# Now, pass control over to the polyModifierCmd._doModifyPoly() method
				# to handle the operation.
				#
				try:
					self._doModifyPoly()
				except:
					self.displayError("splitUV command failed!")
					raise
				else:
					self.setResult("splitUV command succeeded!")
			else:
				self.displayError("splitUV command failed: Selected UVs are not splittable")
		else:
			self.displayError("splitUV command failed: Unable to find selected UVs")

	def redoIt(self):
		"""
		Implements redo for the scripted splitUV command. 

		This method is called when the user has undone a command of this type
		and then redoes it.  No arguments are passed in as all of the necessary
		information is cached by the doIt method.
		"""
		try:
			self._redoModifyPoly()
			self.setResult("splitUV command succeeded!")
		except:
			self.displayError("splitUV command failed!")
			raise

	def undoIt(self):
		"""
		implements undo for the scripted splitUV command.  

		This method is called to undo a previous command of this type.  The 
		system should be returned to the exact state that it was it previous 
		to this command being executed.  That includes the selection state.
		"""
		try:
			self._undoModifyPoly()
			self.setResult("splitUV undo succeeded!")
		except:
			self.displayError("splitUV undo failed!")
			raise

	def _initModifierNode(self, modifierNode):
		# We need to tell the splitUV node which UVs to operate on. By overriding
		# the polyModifierCmd._initModifierNode() method, we can insert our own
		# modifierNode initialization code.
		#
		depNodeFn = OpenMaya.MFnDependencyNode(modifierNode)
		uvListAttr = depNodeFn.attribute("inputComponents")

		# Pass the component list down to the splitUV node
		#
		uvListPlug = OpenMaya.MPlug(modifierNode, uvListAttr)
		uvListPlug.setMObject(self.__fComponentList)

	def _directModifier(self, mesh):
		self.__fSplitUVFactory.setMesh(mesh)
		self.__fSplitUVFactory.setUVIds(self.__fSelUVs)

		# Now, perform the splitUV
		#
		self.__fSplitUVFactory.doIt()

	def __validateUVs(self):
		"""
		Validate the UVs for the splitUV operation. UVs are valid only if they are shared
		by more than one face. While the splitUVNode is smart enough to not process the
		split if a UV is not splittable, a splitUV node is still created by the polyModifierCmd.
		So call this method to validate the UVs before calling _doModifyPoly().

		validateUVs() will return true so long as there is at least one valid UV. It will
		also prune out any invalid UVs from both the component list and UVId array.
		"""
		# Get the mesh that we are operating on
		#
		dagPath = self._getMeshNode()
		mesh = dagPath.node()

		# Get the number of faces sharing the selected UVs
		#
		meshFn = OpenMaya.MFnMesh(mesh)
		polyIter = OpenMaya.MItMeshPolygon(mesh)
		selUVFaceCountArray = OpenMaya.MIntArray()

		indexParam = OpenMaya.MScriptUtil(0)
		indexPtr = indexParam.asIntPtr()

		count = 0
		selUVsCount = self.__fSelUVs.length()
		for i in range(selUVsCount):
			while not polyIter.isDone():
				if polyIter.hasUVs():
					polyVertCount = polyIter.polygonVertexCount()

					for j in range(polyVertCount):
						polyIter.getUVIndex(j, indexPtr)
						UVIndex = indexParam.getInt(indexPtr)

						if UVIndex == self.__fSelUVs[i]:
							count += 1
							break
				polyIter.next()
			selUVFaceCountArray.append(count)

		# Now, check to make sure that at least one UV is being shared by more than one
		# face. So long as we have one UV that we can operate on, we should proceed and let
		# the splitUVNode ignore the UVs which are only shared by one face.
		#
		isValid = False
		validUVIndices = OpenMaya.MIntArray()

		for i in range(selUVsCount):
			if selUVFaceCountArray[i] > 1:
				isValid = True
				validUVIndices.append(i)

		if isValid:
			self.__pruneUVs(validUVIndices)

		return isValid

	def __pruneUVs(self, validUVIndices):
		"""
		This method will remove any invalid UVIds from the component list and UVId array.
		The benefit of this is to reduce the amount of extra processing that the node would
		have to perform. It will result in less iterations through the mesh as there are
		less UVs to search for.
		"""
		validUVIds = OpenMaya.MIntArray()

		for i in range(validUVIndices.length()):
			uvIndex = validUVIndices[i]
			validUVIds.append(self.__fSelUVs[uvIndex])

		# Replace the local int array of UVIds
		#
		self.__fSelUVs.clear()
		self.__fSelUVs = validUVIds

		# Build the list of valid components
		#
		compFn = OpenMaya.MFnSingleIndexedComponent()
		try:
			compFn.create(OpenMaya.MFn.kMeshMapComponent)
		except:
			statusError("compFn.create( MFn::kMeshMapComponent )")
		
		try:
			compFn.addElements(validUVIds)
		except:
			statusError("compFn.addElements( validUVIds )")
		
		# Replace the component list
		#
		component = compFn.object()
		compListFn = OpenMaya.MFnComponentListData()
		compListFn.create()
		try:
			compListFn.add(component)
		except:
			statusError("compListFn.add( component )")

		self.__fComponentList = compListFn.object()

#####################################################################
## FACTORY ##########################################################
#####################################################################


# Overview:
#
# 		The splitUV factory implements the actual splitUV operation. It takes in
# 		only two parameters:
#
# 			1) A polygonal mesh
# 			2) An array of selected UV Ids
#
# 		The algorithm works as follows:
#
# 			1) Parse the mesh for the selected UVs and collect:
#
# 				(a) Number of faces sharing each UV
# 					(stored as two arrays: face array, indexing/offset array)
# 				(b) Associated vertex Id
#
# 			2) Create (N-1) new UVIds for each selected UV, where N represents the number of faces
# 			   sharing the UV.
#
# 			3) Set each of the new UVs to the same 2D location on the UVmap.
#
# 			3) Arbitrarily let the last face in the list of faces sharing this UV to keep the original
# 			   UV.
#
# 			4) Assign each other face one of the new UVIds.
#
#
class splitUVFty(polyModifier.polyModifierFty):

	def __init__(self):
		polyModifier.polyModifierFty.__init__(self)
		# Mesh Node
		# Note: We only make use of this MObject during a single call of
		# 		the splitUV plugin. It is never maintained and used between
		# 		calls to the plugin as the MObject handle could be invalidated
		# 		between calls to the plugin.
		#
		self.__fMesh = OpenMaya.MObject()
		self.__fSelUVs = OpenMaya.MIntArray()
		self.__fSelUVs.clear()

	def setMesh(self, mesh):
		self.__fMesh = mesh

	def setUVIds(self, uvIds):
		self.__fSelUVs = uvIds

	def doIt(self):
		"""
		Performs the actual splitUV operation on the given object and UVs
		"""
		####################################
		# Declare our processing variables #
		####################################

		# Face Id and Face Offset map to the selected UVs
		#
		selUVFaceIdMap = OpenMaya.MIntArray()
		selUVFaceOffsetMap = OpenMaya.MIntArray()

		# Local Vertex Index map to the selected UVs
		#
		selUVLocalVertIdMap = OpenMaya.MIntArray()

		#################################################
		# Collect necessary information for the splitUV #
		# 												#
		# - uvSet										#
		# - faceIds / localVertIds per selected UV		#
		#################################################

		meshFn = OpenMaya.MFnMesh(self.__fMesh)
		selUVSet = meshFn.currentUVSetName()

		indexParam = OpenMaya.MScriptUtil(0)
		indexPtr = indexParam.asIntPtr()

		offset = 0
		selUVsCount = self.__fSelUVs.length()
		polyIter = OpenMaya.MItMeshPolygon(self.__fMesh)
		for i in range(selUVsCount):
			selUVFaceOffsetMap.append(offset)

			polyIter.reset()
			while not polyIter.isDone():
				if polyIter.hasUVs():
					polyVertCount = polyIter.polygonVertexCount()

					for j in range(polyVertCount):
						polyIter.getUVIndex(j, indexPtr)
						UVIndex = indexParam.getInt(indexPtr)

						if UVIndex == self.__fSelUVs[i]:
							selUVFaceIdMap.append(polyIter.index())
							selUVLocalVertIdMap.append(j)
							offset += 1
							break

				polyIter.next()

		# Store total length of the faceId map in the last element of
		# the offset map so that there is a way to get the number of faces
		# sharing each of the selected UVs
		#
		selUVFaceOffsetMap.append(offset)

		###############################
		# Begin the splitUV operation #
		###############################

		currentUVCount = meshFn.numUVs(selUVSet)

		for i in range(selUVsCount):
			# Get the current FaceId map offset
			#
			offset = selUVFaceOffsetMap[i]

			# Get the U and V values of the current UV
			#
			uvId = self.__fSelUVs[i]

			uParam = OpenMaya.MScriptUtil(0.0)
			uPtr = uParam.asFloatPtr()
			vParam = OpenMaya.MScriptUtil(0.0)
			vPtr = vParam.asFloatPtr()
			meshFn.getUV(uvId, uPtr, vPtr, selUVSet)
			u = uParam.getFloat(uPtr)
			v = vParam.getFloat(vPtr)
			
			# Get the number of faces sharing the current UV
			#
			faceCount = selUVFaceOffsetMap[i + 1] - selUVFaceOffsetMap[i]

			# Arbitrarily choose that the last faceId in the list of faces
			# sharing this UV, will keep the original UV.
			#
			for j in range(faceCount - 1):
				meshFn.setUV(currentUVCount, u, v, selUVSet)

				localVertId = selUVLocalVertIdMap[offset]
				faceId = selUVFaceIdMap[offset]

				meshFn.assignUV(faceId, localVertId, currentUVCount, selUVSet)

				currentUVCount += 1
				offset += 1

#####################################################################
## NODE #############################################################
#####################################################################


class splitUVNode(polyModifier.polyModifierNode):
	uvList = OpenMaya.MObject()

	def __init__(self):
		polyModifier.polyModifierNode.__init__(self)
		self.fSplitUVFactory = splitUVFty()

	def compute(self, plug, data):
		"""
		Description:
			This method computes the value of the given output plug based
			on the values of the input attributes.
	
		Arguments:
			plug - the plug to compute
			data - object that provides access to the attributes for this node
		"""
		stateData = 0
		state = OpenMayaMPx.cvar.MPxNode_state
		try:
			stateData = data.outputValue(state)
		except:
			statusError("ERROR getting state")

		# Check for the HasNoEffect/PassThrough flag on the node.
		#
		# (stateData is an enumeration standard in all depend nodes - stored as short)
		# 
		# (0 = Normal)
		# (1 = HasNoEffect/PassThrough)
		# (2 = Blocking)
		# ...
		#
		if stateData.asShort() == 1:
			try:
				inputData = data.inputValue(splitUVNode.inMesh)
			except:
				statusError("ERROR getting inMesh")

			try:
				outputData = data.outputValue(splitUVNode.outMesh)
			except:
				statusError("ERROR getting outMesh")

			# Simply redirect the inMesh to the outMesh for the PassThrough effect
			#
			outputData.setMObject(inputData.asMesh())
		else:
			# Check which output attribute we have been asked to 
			# compute. If this node doesn't know how to compute it, 
			# we must return MS::kUnknownParameter
			# 
			if plug == splitUVNode.outMesh:
				try:
					inputData = data.inputValue(splitUVNode.inMesh)
				except:
					statusError("ERROR getting inMesh")

				try:
					outputData = data.outputValue(splitUVNode.outMesh)
				except:
					statusError("ERROR getting outMesh") 

				# Now, we get the value of the uvList and use it to perform
				# the operation on this mesh
				#
				try:
					inputUVs = data.inputValue(splitUVNode.uvList)
				except:
					statusError("ERROR getting uvList")

				# Copy the inMesh to the outMesh, and now you can
				# perform operations in-place on the outMesh
				#
				outputData.setMObject(inputData.asMesh())
				mesh = outputData.asMesh()

				# Retrieve the UV list from the component list.
				#
				# Note, we use a component list to store the components
				# because it is more compact memory wise. (ie. comp[81:85]
				# is smaller than comp[81], comp[82],...,comp[85])
				#
				compList = inputUVs.data()
				compListFn = OpenMaya.MFnComponentListData(compList)

				uvIds = OpenMaya.MIntArray()
				for i in range(compListFn.length()):
					comp = compListFn[i]
					if comp.apiType() == OpenMaya.MFn.kMeshMapComponent:
						uvComp = OpenMaya.MFnSingleIndexedComponent(comp)
						for j in range(uvComp.elementCount()):
							uvId = uvComp.element(j)
							uvIds.append(uvId)

				# Set the mesh object and uvList on the factory
				#
				self.fSplitUVFactory.setMesh(mesh)
				self.fSplitUVFactory.setUVIds(uvIds)

				# Now, perform the splitUV
				#
				try:
					self.fSplitUVFactory.doIt()
				except:
					statusError("ERROR in splitUVFty.doIt()")

				# Mark the output mesh as clean
				#
				outputData.setClean()
			else:
				return OpenMaya.kUnknownParameter

		return None

#####################################################################
## REGISTRATION #####################################################
#####################################################################


def cmdCreator():
	return OpenMayaMPx.asMPxPtr(splitUV())


def nodeCreator():
	return OpenMayaMPx.asMPxPtr(splitUVNode())


def nodeInitializer():
	attrFn = OpenMaya.MFnTypedAttribute()

	splitUVNode.uvList = attrFn.create("inputComponents", "ics", OpenMaya.MFnComponentListData.kComponentList)
	attrFn.setStorable(True)  # To be stored during file-save

	splitUVNode.inMesh = attrFn.create("inMesh", "im", OpenMaya.MFnMeshData.kMesh)
	attrFn.setStorable(True)  # To be stored during file-save

	# Attribute is read-only because it is an output attribute
	#
	splitUVNode.outMesh = attrFn.create("outMesh", "om", OpenMaya.MFnMeshData.kMesh)
	attrFn.setStorable(False)
	attrFn.setWritable(False)

	# Add the attributes we have created to the node
	#
	splitUVNode.addAttribute(splitUVNode.uvList)
	splitUVNode.addAttribute(splitUVNode.inMesh)
	splitUVNode.addAttribute(splitUVNode.outMesh)

	# Set up a dependency between the input and the output.  This will cause
	# the output to be marked dirty when the input changes.  The output will
	# then be recomputed the next time the value of the output is requested.
	#
	splitUVNode.attributeAffects(splitUVNode.inMesh, splitUVNode.outMesh)
	splitUVNode.attributeAffects(splitUVNode.uvList, splitUVNode.outMesh)


def initializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject, "Autodesk", "1.0", "Any")
	try:
		mplugin.registerCommand(kPluginCmdName, cmdCreator)
	except:
		sys.stderr.write("Failed to register command: %s\n" % kPluginCmdName)
		raise

	try:
		mplugin.registerNode(kPluginNodeTypeName, kPluginNodeId, nodeCreator, nodeInitializer)
	except:
		sys.stderr.write("Failed to register node: %s" % kPluginNodeTypeName)
		raise


def uninitializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.deregisterCommand(kPluginCmdName)
	except:
		sys.stderr.write("Failed to unregister command: %s\n" % kPluginCmdName)
		raise

	try:
		mplugin.deregisterNode(kPluginNodeId)
	except:
		sys.stderr.write("Failed to deregister node: %s" % kPluginNodeTypeName)
		raise
