NAME = 'validate default shader'
ORDER = 1
VALID = True
TYPE = 'validator'
KEY = 'shader_default'
OWNER = 'Subin Gopi'
COMMENTS = 'to check all geometries are user assigned shader'
VERSION = '0.0.0'
MODIFIED = 'May 04, 2020'


def execute(**kwargs):
    from studio_usd_pipe.utils import maya_asset    
    valid, values, message = maya_asset.check_shader_assigned_geometries()
    return valid, values, message


def repair(**kwargs):   
    return False, [None], 'replace shader assignment default shader to user shader'
    
