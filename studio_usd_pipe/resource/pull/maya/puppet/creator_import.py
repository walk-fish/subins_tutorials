NAME = 'import maya'
ORDER = 1
VALID = True
TYPE = 'creator'
KEY = 'puppet_scene'
OWNER = 'Subin Gopi'
COMMENTS = 'To import the maya puppet scene'
VERSION = '0.0.0'
MODIFIED = 'May 05, 2020'
ICON = 'import_maya.png'


def execute(**kwargs):       
    from studio_usd_pipe.utils import maya_scene
    current_scene = kwargs[KEY][-1].encode()
    namespace = kwargs['caption'].encode()
    valid, value, message = maya_scene.import_maya_scene(current_scene, namespace)
    return valid, [value], message
    
