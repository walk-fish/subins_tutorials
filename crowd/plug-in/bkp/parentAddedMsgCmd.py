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

# import maya
# maya.cmds.loadPlugin("parentAddedMsgCmd.py")
# maya.cmds.spParentAddedMsg()

import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx

kPluginCmdName = "spParentAddedMsg"

messageId = 0
messageIdSet = False


def removeCallback(id):
	try:
		OpenMaya.MMessage.removeCallback(id)
	except:
		sys.stderr.write("Failed to remove callback\n")
		raise


def dagParentAddedCallback(child, parent, clientData):
	print "dagParentAddedCallback..."
	print "\tchild %s" % child.fullPathName()
	print "\tparent %s" % parent.fullPathName()
	print "\tclient data %s" % clientData


def createParentAddedCallback(stringData):
	# global declares module level variables that will be assigned
	global messageIdSet
	try:
		id = OpenMaya.MDagMessage.addParentAddedCallback(dagParentAddedCallback, stringData)
	except:
		sys.stderr.write("Failed to install dag parent added callback\n")
		messageIdSet = False
	else:
		messageIdSet = True
	return id


# command
class scriptedCommand(OpenMayaMPx.MPxCommand):

	def __init__(self):
		OpenMayaMPx.MPxCommand.__init__(self)

	def doIt(self, argList):
		global messageId
		if (messageIdSet):
			print "Message callaback already installed"
		else:
			print "Installing parent added callback message"
			messageId = createParentAddedCallback("_noData_")


# Creator
def cmdCreator():
	return OpenMayaMPx.asMPxPtr(scriptedCommand())

	
# Initialize the script plug-in
def initializePlugin(mobject):
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.registerCommand(kPluginCmdName, cmdCreator)
	except:
		sys.stderr.write("Failed to register command: %s\n" % name)
		raise


# Uninitialize the script plug-in
def uninitializePlugin(mobject):
	# Remove the callback
	if (messageIdSet):
		removeCallback(messageId)
	# Remove the plug-in command
	mplugin = OpenMayaMPx.MFnPlugin(mobject)
	try:
		mplugin.deregisterCommand(kPluginCmdName)
	except:
		sys.stderr.write("Failed to unregister command: %s\n" % kPluginCmdName)
		raise
	
