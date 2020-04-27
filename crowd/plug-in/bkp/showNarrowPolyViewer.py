# -
# ==========================================================================
# Copyright (C) 1995 - 2006 Autodesk, Inc. and/or its licensors.  All 
# rights reserved.
# 
#  The coded instructions, statements, computer programs, and/or related 
#  material (collectively the "Data") in these files contain unpublished 
#  information proprietary to Autodesk, Inc. ("Autodesk") and/or its 
#  licensors, which is protected by U.S. and Canadian federal copyright 
#  law and by international treaties.
# 
#  The Data is provided for use exclusively by You. You have the right 
#  to use, modify, and incorporate this Data into other products for 
#  purposes authorized by the Autodesk software license agreement, 
#  without fee.
# 
#  The copyright notices in the Software and this entire statement, 
#  including the above license grant, this restriction and the 
#  following disclaimer, must be included in all copies of the 
#  Software, in whole or in part, and all derivative works of 
#  the Software, unless such copies or derivative works are solely 
#  in the form of machine-executable object code generated by a 
#  source language processor.
# 
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. 
#  AUTODESK DOES NOT MAKE AND HEREBY DISCLAIMS ANY EXPRESS OR IMPLIED 
#  WARRANTIES INCLUDING, BUT NOT LIMITED TO, THE WARRANTIES OF 
#  NON-INFRINGEMENT, MERCHANTABILITY OR FITNESS FOR A PARTICULAR 
#  PURPOSE, OR ARISING FROM A COURSE OF DEALING, USAGE, OR 
#  TRADE PRACTICE. IN NO EVENT WILL AUTODESK AND/OR ITS LICENSORS 
#  BE LIABLE FOR ANY LOST REVENUES, DATA, OR PROFITS, OR SPECIAL, 
#  DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES, EVEN IF AUTODESK 
#  AND/OR ITS LICENSORS HAS BEEN ADVISED OF THE POSSIBILITY 
#  OR PROBABILITY OF SUCH DAMAGES.
# 
#  ==========================================================================
# +

import maya


def showNarrowPolyViewer():

	window = maya.cmds.window()
	form = maya.cmds.formLayout()
	editor = maya.cmds.spNarrowPolyViewer()
	column = maya.cmds.columnLayout(adjustableColumn=True)

	#   Create some buttons that will alter the display appearance of
	#   objects in the model editor, eg. wireframe vs. shaded mode.
	# 
	maya.cmds.button(label="Wireframe", command=("maya.cmds.spNarrowPolyViewer(\"%s\",edit=True,displayAppearance=\"wireframe\")" % (editor,)))
	maya.cmds.button(label="Points", command=("maya.cmds.spNarrowPolyViewer(\"%s\",edit=True,displayAppearance=\"points\")" % (editor,)))
	maya.cmds.button(label="Bounding Box", command=("maya.cmds.spNarrowPolyViewer(\"%s\",edit=True,displayAppearance=\"boundingBox\")" % (editor,)))
	maya.cmds.button(label="Smooth Shaded", command=("maya.cmds.spNarrowPolyViewer(\"%s\",edit=True,displayAppearance=\"smoothShaded\")" % (editor,)))
	maya.cmds.button(label="Flat Shaded", command=("maya.cmds.spNarrowPolyViewer(\"%s\",edit=True,displayAppearance=\"flatShaded\")" % (editor,)))
	maya.cmds.floatField("angleTolerance", minValue=0, maxValue=180, value=10, step=1, precision=1, ann="tolerance", cc=("maya.cmds.spNarrowPolyViewer(\"%s\", edit=True,tol=maya.cmds.floatField(\"angleTolerance\",q=True,v=True))" % (editor,)), \
		ec=("maya.cmds.spNarrowPolyViewer(\"%s\", edit=True,tol=maya.cmds.floatField(\"angleTolerance\",q=True,v=True))" % (editor,)), dc=("maya.cmds.spNarrowPolyViewer(\"%s\", edit=True,tol=maya.cmds.floatField(\"angleTolerance\",q=True,v=True))" % (editor,)), \
		rfc=("maya.cmds.spNarrowPolyViewer(\"%s\", edit=True,tol=maya.cmds.floatField(\"angleTolerance\",q=True,v=True))" % (editor,)))

	#   Set up the window layout attachments.
	# 
	maya.cmds.formLayout(form, edit=True, attachForm=(column, "top", 0))
	maya.cmds.formLayout(form, edit=True, attachForm=(column, "left", 0))
	maya.cmds.formLayout(form, edit=True, attachNone=(column, "bottom"))
	maya.cmds.formLayout(form, edit=True, attachNone=(column, "right"))
	maya.cmds.formLayout(form, edit=True, attachForm=(editor, "top", 0), attachControl=(editor, "left", 0, column))
	maya.cmds.formLayout(form, edit=True, attachForm=(editor, "bottom", 0))
	maya.cmds.formLayout(form, edit=True, attachForm=(editor, "right", 0))

	#   Create a camera for the editor.  This particular camera will
	#   have a close up perspective view of the centre of the ground plane.
	# 
	camera = maya.cmds.camera(centerOfInterest=2.450351, position=(1.535314, 1.135712, 1.535314), rotation=(-27.612504, 45, 0), worldUp=(-0.1290301, 0.3488592, -0.1290301))
	g__MpTestPrimaryCamera = camera[0];

	#   Attach the camera to the model editor.
	# 
	maya.cmds.spNarrowPolyViewer(editor, edit=True, camera=camera[0])
	maya.cmds.currentTime(10.0, edit=True)
	maya.cmds.spNarrowPolyViewer(editor, edit=True, i=True)
	maya.cmds.refresh()
	maya.cmds.spNarrowPolyViewer(editor, edit=True, r=True)

	maya.cmds.showWindow(window)
