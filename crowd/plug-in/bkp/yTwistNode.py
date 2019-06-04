#-
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
#+

# import maya
# maya.cmds.loadPlugin("yTwistNode.py")
# maya.cmds.sphere()
# maya.cmds.deformer( type='spyTwistNode' )

import math, sys

import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim
import maya.OpenMayaMPx as OpenMayaMPx
import maya.cmds as cmds

kPluginNodeTypeName = "spyTwistNode"

yTwistNodeId = OpenMaya.MTypeId(0x8702)

kApiVersion = cmds.about(apiVersion=True)
if kApiVersion < 201600:
	outputGeom = OpenMayaMPx.cvar.MPxDeformerNode_outputGeom
	envelope = OpenMayaMPx.cvar.MPxDeformerNode_envelope
else:
	outputGeom = OpenMayaMPx.cvar.MPxGeometryFilter_outputGeom
	envelope = OpenMayaMPx.cvar.MPxGeometryFilter_envelope

# Node definition
class yTwistNode(OpenMayaMPx.MPxDeformerNode):
	# class variables
	angle = OpenMaya.MObject()
	# constructor
	def __init__(self):
		OpenMayaMPx.MPxDeformerNode.__init__(self)
	# deform
	def deform(self,dataBlock,geomIter,matrix,multiIndex):
		#
		# get the angle from the datablock
		angleHandle = dataBlock.inputValue( self.angle )
		angleValue = angleHandle.asDouble()
		#
		# get the envelope
		envelopeHandle = dataBlock.inputValue( envelope )
		envelopeValue = envelopeHandle.asFloat()
		#
		# iterate over the object and change the angle
		while geomIter.isDone() == False:
			point = geomIter.position()
			ff = angleValue * point.y * envelopeValue
			if ff != 0.0:
				cct= math.cos(ff)
				cst= math.sin(ff)
				tt= point.x*cct-point.z*cst
				point.z= point.x*cst + point.z*cct
				point.x=tt
			geomIter.setPosition( point )
			geomIter.next()
				
# creator
def nodeCreator():
	return OpenMayaMPx.asMPxPtr( yTwistNode() )

# initializer
def nodeInitializer():
	# angle
	nAttr = OpenMaya.MFnNumericAttribute()
	yTwistNode.angle = nAttr.create( "angle", "fa", OpenMaya.MFnNumericData.kDouble, 0.0 )
	#nAttr.setDefault(0.0)
	nAttr.setKeyable(True)
	# add attribute
	try:
		yTwistNode.addAttribute( yTwistNode.angle )
		yTwistNode.attributeAffects( yTwistNode.angle, outputGeom )
	except:
		sys.stderr.write( "Failed to create attributes of %s node\n", kPluginNodeTypeName )
	
# initialize the script plug-in
def initializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.registerNode( kPluginNodeTypeName, yTwistNodeId, nodeCreator, nodeInitializer, OpenMayaMPx.MPxNode.kDeformerNode )
	except:
		sys.stderr.write( "Failed to register node: %s\n" % kPluginNodeTypeName )

# uninitialize the script plug-in
def uninitializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.deregisterNode( yTwistNodeId )
	except:
		sys.stderr.write( "Failed to unregister node: %s\n" % kPluginNodeTypeName )

	
