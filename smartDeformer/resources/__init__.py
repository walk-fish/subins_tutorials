import os
import getpass

CURRENT_PATH = os.path.dirname(__file__)
MODULE = 'smart_deformer'



def getInputPath(module=None):
    return os.path.join(CURRENT_PATH, 'inputs', '{}.json'.format(module))


def getIconPath():
    return os.path.join(CURRENT_PATH, 'icons')


def getWeightsPath():
    return os.path.join (getWorkspacePath(), 'weights')


def getWorkspacePath():
    return os.path.join (os.getenv('HOME'), 'Documents', MODULE)


def getPublishDirectory():
    return os.path.join(os.environ['HOME'], 'Walk_cycle', 'characters')

def getResourceTypes():
    data = {'weights': getWeightsPath()}    
    return data


def getToolKitLink():
    return 'http://download.autodesk.com/us/maya/2011help/API/classes.html'


def getToolKitHelpLink():
    return 'http://help.autodesk.com/view/MAYAUL/2017/ENU/?guid=__py_ref_class_open_maya_1_1_m_selection_list_html'

def getDownloadLink():
    return 'http://download.autodesk.com/us/maya/2011help/API/classes.html'

# end ####################################################################
