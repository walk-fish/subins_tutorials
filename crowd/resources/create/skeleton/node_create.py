LONG_NAME = 'create skeleton'
ICON = 'skeletion'
ORDER = 0
MODULE_TYPE = 'skeleton'
BUNDLE_TYPE = 'create'
VALID = True
LAST_MODIFIED = 'June 16, 2019'
OWNER = 'Subin Gopi'
COMMENTS = 'To create skeleton'
VERSION = 1.0
CLASS = 'CreateNode'

from pymel import core

from crowd.core import skeleton
from crowd.api import crowdMaya
reload(crowdMaya)


class CreateNode(object):

    def __init__(self, **kwargs):
        print '\n#<%s> <%s> <%s>' % (BUNDLE_TYPE, MODULE_TYPE, COMMENTS)
        self.type = None
        self.tag = None
        self.input = None
        self.position = [0, 0, 0]
        self.parent = None
        if 'type' in kwargs:
            self.type = kwargs['type']
        if 'tag' in kwargs:
            self.tag = kwargs['tag']
        if 'input' in kwargs:
            self.input = kwargs['input']
        if 'position' in kwargs:
            self.position = kwargs['position']
        if 'parent' in kwargs:
            self.parent = kwargs['parent']
        self.result = self.make()

    def make(self):
        root_dag_path = None
        parent_data = None
        try:
            root_dag_path, parent_data = skeleton.create_skeleton(
                self.tag, self.input, position=self.position, parent=self.parent)
        except Exception as error:
            return 'failed', None, str(error)
        if not root_dag_path:
            return
        crowd_maya = crowdMaya.Connect()
        crowd_maya.addMessageAttribute(
            root_dag_path, 'skeletonType', 'sktyp', value=self.tag)
        return 'success', root_dag_path, parent_data


def testRun(*args):
    input_joint = CreateNode(tag=args[0], input=args[1])
    result, data, message = input_joint.result
    print '\t\tresult', result
    return result, data, message
