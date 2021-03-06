import os
import sys
import copy
import json
import getpass
import tempfile
import warnings

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2 import QtWidgets

from functools import partial

from studio_usd_pipe import resource
from studio_usd_pipe.core import common
from studio_usd_pipe.core import swidgets
from studio_usd_pipe.utils import maya_asset
from studio_usd_pipe.api import studioShow
from studio_usd_pipe.api import studioPush
from studio_usd_pipe.api import studioPipe
from studio_usd_pipe.api import studioEnviron

reload(studioPush)


class Window(QtWidgets.QWidget):
 
    def __init__(self, parent=None, standalone=None, application=None):
        super(Window, self).__init__(parent)        
        self.setWindowFlags(QtCore.Qt.Window) 
        self.standalone = standalone
        self.application = application
        self.pipe = 'assets'
        self.title = 'Asset Publish/Push'
        self.width = 572
        self.height = 716
        shows = studioShow.Show()
        self.current_show = shows.get_current_show()
        self.current_show = 'btm'  # to remove
        self.environ = studioEnviron.Environ(self.current_show)
        self.spipe = studioPipe.Pipe(self.current_show, self.pipe) 
        self.show_icon = self.environ.get_show_icon()
        self.source_maya = None
        self.pipe_ids = {}
        self.setup_ui()
        self.setup_menu()
        self.setup_icons()
        self.set_default()
 
    def setup_ui(self):
        self.setObjectName('widget_asset_push')
        self.resize(self.width, self.height)         
        self.verticallayout = QtWidgets.QVBoxLayout(self)
        self.verticallayout.setObjectName('verticallayout')
        self.verticallayout.setSpacing(10)
        self.verticallayout.setContentsMargins(5, 5, 5, 5)        
        self.verticallayout_item, self.button_show = swidgets.set_header(
            self, self.title, self.verticallayout, show_icon=self.show_icon)    
        self.horizontallayout_output = QtWidgets.QHBoxLayout()
        self.horizontallayout_output.setObjectName('horizontallayout_output')
        self.horizontallayout_output.setSpacing(10)
        self.horizontallayout_output.setContentsMargins(5, 5, 5, 5)
        self.verticallayout_item.addLayout(self.horizontallayout_output)
        source_file = 'Current File: {}\nFile Type: {}'.format(None, None)
        self.label_source = QtWidgets.QLabel()
        self.label_source.setObjectName('label_source')
        self.label_source.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.label_source.setStyleSheet('font: 8pt;')
        self.label_source.setText(source_file)
        self.label_source.setToolTip(None)
        self.label_source.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)        
        self.label_source.customContextMenuRequested.connect(
            partial(self.on_context_menu, 'maya', self.label_source))        
        self.horizontallayout_output.addWidget(self.label_source)
        self.horizontallayout_input = QtWidgets.QHBoxLayout()
        self.horizontallayout_input.setContentsMargins(5, 5, 5, 5)
        self.horizontallayout_input.setObjectName('horizontallayout_input') 
        self.verticallayout_item.addLayout(self.horizontallayout_input)        
        self.gridlayout = QtWidgets.QGridLayout(None)
        self.gridlayout.setObjectName('gridlayout')
        self.gridlayout.setSpacing(5)
        self.gridlayout.setContentsMargins(10, 0, 0, 0)
        self.verticallayout_item.addLayout(self.gridlayout)        
        spacer_item = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticallayout.addItem(spacer_item)
        self.label_caption = QtWidgets.QLabel(self)
        self.label_caption.setObjectName('label_caption')
        self.label_caption.setText('Caption')
        self.label_caption.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_caption, 0, 0, 1, 1)
        self.combobox_caption = QtWidgets.QComboBox(self)
        self.combobox_caption.setObjectName('combobox_caption')
        self.combobox_caption.setEditable(True)
        self.combobox_caption.setEnabled(True)
        self.combobox_caption.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout.addWidget(self.combobox_caption, 0, 1, 1, 1)  
        self.label_subfield = QtWidgets.QLabel(self)
        self.label_subfield.setObjectName('label_subfield')
        self.label_subfield.setText('Subfield')
        self.label_subfield.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_subfield, 1, 0, 1, 1)
        self.combobox_subfield = QtWidgets.QComboBox(self)
        self.combobox_subfield.setObjectName('combobox_subfield')
        self.combobox_subfield.setEditable(True)
        self.combobox_subfield.setEnabled(True)
        self.combobox_subfield.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout.addWidget(self.combobox_subfield, 1, 1, 1, 1)  
        self.label_type = QtWidgets.QLabel(self)
        self.label_type.setObjectName('label_type')
        self.label_type.setText('Type')
        self.label_type.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_type, 2, 0, 1, 1)
        self.combobox_type = QtWidgets.QComboBox(self)
        self.combobox_type.setObjectName('combobox_type')
        self.combobox_type.setEditable(True)
        self.combobox_type.setEnabled(True)
        self.combobox_type.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout.addWidget(self.combobox_type, 2, 1, 1, 1)  
        self.label_tag = QtWidgets.QLabel(self)
        self.label_tag.setObjectName('label_tag')
        self.label_tag.setText('Tag')
        self.label_tag.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_tag, 3, 0, 1, 1)
        self.combobox_tag = QtWidgets.QComboBox(self)
        self.combobox_tag.setObjectName('combobox_tag')
        self.combobox_tag.setEditable(True)
        self.combobox_tag.setEnabled(True)
        self.combobox_tag.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout.addWidget(self.combobox_tag, 3, 1, 1, 1)
        self.label_dependency = QtWidgets.QLabel(self)
        self.label_dependency.setObjectName('label_dependency')
        self.label_dependency.setText('Available Model Dependencies')
        self.label_dependency.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_dependency, 4, 0, 1, 1)
        self.combobox_dependency = QtWidgets.QComboBox(self)
        self.combobox_dependency.setObjectName('combobox_dependency')
        self.combobox_dependency.setEditable(True)
        self.combobox_dependency.setEnabled(True)
        self.combobox_dependency.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout.addWidget(self.combobox_dependency, 4, 1, 1, 1) 
        self.label_thumbnail = QtWidgets.QLabel(self)
        self.label_thumbnail.setObjectName('label_thumbnail')
        self.label_thumbnail.setText('Thumbnail')
        self.label_thumbnail.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_thumbnail, 5, 0, 1, 1)
        self.button_thumbnail = QtWidgets.QPushButton(self)
        self.button_thumbnail.setObjectName('button_thumbnail')
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.button_thumbnail.setSizePolicy(size_policy)
        self.button_thumbnail.setMinimumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setMaximumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)        
        self.button_thumbnail.customContextMenuRequested.connect(
            partial(self.on_context_menu, 'image', self.button_thumbnail))        
        swidgets.image_to_button(
            self.button_thumbnail, 256, 180, path=os.path.join(resource.getIconPath(), 'screenshot.png'))     
        self.button_thumbnail.clicked.connect(partial(self.take_thumbnail, self.button_thumbnail))
        self.gridlayout.addWidget(self.button_thumbnail, 5, 1, 1, 1)  
        self.label_description = QtWidgets.QLabel(self)
        self.label_description.setObjectName('label_description')
        self.label_description.setText('Description')
        self.label_description.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_description, 6, 0, 1, 1)
        self.textedit_description = QtWidgets.QTextEdit(self)
        self.textedit_description.setObjectName('textedit_description')
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.textedit_description.setSizePolicy(size_policy)
        self.textedit_description.setMinimumSize(QtCore.QSize(0, 90))
        self.textedit_description.setMaximumSize(QtCore.QSize(16777215, 90))          
        self.gridlayout.addWidget(self.textedit_description, 6, 1, 1, 1)  
        self.label_version = QtWidgets.QLabel(self)
        self.label_version.setObjectName('label_version')
        self.label_version.setText('version')
        self.label_version.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_version, 7, 0, 1, 1)
        self.combobox_version = QtWidgets.QComboBox(self)
        self.combobox_version.setObjectName('combobox_version')
        self.combobox_version.setEditable(True)
        self.combobox_version.setEnabled(True)
        self.combobox_version.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout.addWidget(self.combobox_version, 7, 1, 1, 1)                  
        self.label_latest_version = QtWidgets.QLabel(self)
        self.label_latest_version.setObjectName('label_latest_version')
        self.label_latest_version.setText('Latest Version')
        self.label_latest_version.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_latest_version, 8, 0, 1, 1)
        self.combobox_latest_version = QtWidgets.QComboBox(self)
        self.combobox_latest_version.setObjectName('combobox_latest_version')
        self.combobox_latest_version.setEditable(True)
        self.combobox_latest_version.setEnabled(False)
        self.combobox_latest_version.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout.addWidget(self.combobox_latest_version, 8, 1, 1, 1)
        self.label_next_version = QtWidgets.QLabel(self)
        self.label_next_version.setObjectName('label_next_version')
        self.label_next_version.setText('Next Version')
        self.label_next_version.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.gridlayout.addWidget(self.label_next_version, 9, 0, 1, 1)
        self.combobox_next_version = QtWidgets.QComboBox(self)
        self.combobox_next_version.setObjectName('combobox_next_version')
        self.combobox_next_version.setEditable(True)
        self.combobox_next_version.setEnabled(False)
        self.combobox_next_version.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.gridlayout.addWidget(self.combobox_next_version, 9, 1, 1, 1)  
        self.horizontallayout_button = QtWidgets.QHBoxLayout()
        self.horizontallayout_button.setObjectName('horizontallayout_button')
        self.horizontallayout_button.setSpacing(10)
        self.horizontallayout_button.setContentsMargins(5, 5, 5, 5)        
        self.verticallayout.addLayout(self.horizontallayout_button)  
        spacer_item = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontallayout_button.addItem(spacer_item)
        self.button_cancel = QtWidgets.QPushButton(self)
        self.button_cancel.setObjectName('button_cancel')
        self.button_cancel.setText('Cancel')
        self.horizontallayout_button.addWidget(self.button_cancel)
        self.button_publish = QtWidgets.QPushButton(self)
        self.button_publish.setObjectName('button_create')
        self.button_publish.setText('Publish')
        self.horizontallayout_button.addWidget(self.button_publish)
        spacer_item = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)        
        self.combobox_caption.editTextChanged.connect(self.set_current_caption)
        self.combobox_subfield.currentIndexChanged.connect(self.set_current_version)
        self.combobox_version.currentIndexChanged.connect(self.set_current_version)
        self.button_publish.clicked.connect(self.do_publish)        
        self.button_cancel.clicked.connect(self.close)  
            
    def setup_menu(self):        
        self.menu = QtWidgets.QMenu(self)
        self.menu.setObjectName('menu')        
        self.action_maya = QtWidgets.QAction(self)
        self.action_maya.setObjectName('action_maya')
        self.action_maya.setToolTip('Load maya file') 
        self.action_maya.setText('Load maya file')
        self.action_image = QtWidgets.QAction(self)
        self.action_image.setObjectName('action_image')
        self.action_image.setToolTip('Load image') 
        self.action_image.setText('Load image')        
        self.menu.addAction(self.action_maya)
        self.menu.addAction(self.action_image)
        self.action_maya.triggered.connect(self.load_maya_file)
        self.action_image.triggered.connect(self.load_image_file)
                
    def set_menu_options(self, key):
        actions = [
            self.action_maya,
            self.action_image  
            ]
        for action in actions:
            action.setVisible(True)                
        invisibile = {
            'maya': [
                # self.action_maya,
                self.action_image      
                ],
            'image': [
                self.action_maya,
                # self.action_image     
                ]
            }
        if key in invisibile:
            for action in invisibile[key]:
                action.setVisible(False)        
         
    def setup_icons (self):
        widgets = self.findChildren(QtWidgets.QAction)
        swidgets.set_icons(mainwindow=self, widgets=widgets)
       
    def set_default(self):
        self.clear_widget()
        self.setup_current_maya()
        pub_data = self.spipe.get()
        captions = ['']
        if pub_data:  # add caption from database
            captions = [''] + pub_data.keys()
        self.combobox_caption.addItems(captions)
        self.combobox_subfield.addItems(self.spipe.pipe_inputs['subfield']['values'])
        self.combobox_type.addItems(self.spipe.pipe_inputs['type']['values'])                                                
        self.combobox_tag.addItems(self.spipe.pipe_inputs['tag']['values'])         
        self.combobox_version.addItems(['major', 'minor', 'patch'])            
        size = self.button_thumbnail.minimumSize()
        swidgets.image_to_button(
            self.button_thumbnail,
            size.width(),
            size.height(),
            path=os.path.join(resource.getIconPath(), 'screenshot.png')
            )

    def on_context_menu(self, key, widget, point):
        self.set_menu_options(key)        
        self.menu.exec_(widget.mapToGlobal(point))
     
    def clear_widget(self):
        self.combobox_caption.clear()
        self.combobox_subfield.clear()
        self.combobox_type.clear()
        self.combobox_tag.clear()
        self.combobox_dependency.clear()
        self.textedit_description.clear()
        self.combobox_version.clear()
        self.combobox_latest_version.clear()
        self.combobox_next_version.clear()   
                 
    def setup_current_maya(self):
        if self.standalone:
            return
        format = self.get_current_maya()
        self.set_current_maya(format)
         
    def get_current_maya(self):
        from studio_usd_pipe.api import studioMaya
        studio_maya = studioMaya.Maya()
        self.source_maya, format = studio_maya.get_current_file()
        return format
        
    def load_maya_file(self):
        if not self.standalone:
            format = self.get_current_maya()            
            self.set_current_maya(format)
            return
        format = self.read_current_maya()
        self.set_current_maya(format)
 
    def set_current_maya(self, format):
        source_file = 'Current File: {}\nFile Type: {}'.format(self.source_maya, format)
        self.label_source.setText(source_file)
        self.pipe_ids = self.get_pipe_ids()
        self.combobox_caption.setCurrentIndex(0) 
         
    def read_current_maya(self):
        current_file = swidgets.brows_file(
            'find the maya file', resource.getMayaFormats())   
        if not current_file:
            return
        os.environ['BROWS_PATH'] = os.path.dirname(current_file)
        format = os.path.splitext(current_file)[-1]
        file_types = resource.getMayaFileTypes()         
        format = file_types[format]
        self.source_maya = current_file
        return format
 
    def load_image_file(self):
        current_file = swidgets.brows_file(
            'find the thumbnail(image) file', resource.getImageFormats())        
        if not current_file:
            return
        os.environ['BROWS_PATH'] = os.path.dirname(current_file)
        output_path = os.path.join(
            tempfile.gettempdir(),
            'thumbnail_%s.png' % resource.getCurrentDateKey())        
        output_path = swidgets.image_resize(current_file, output_path, 768, 540)                
        size = self.button_thumbnail.minimumSize()
        swidgets.image_to_button(
            self.button_thumbnail, size.width(), size.height(), path=output_path)
        self.button_thumbnail.setToolTip(output_path)        
 
    def get_pipe_ids(self):
        if not self.standalone:
            id_data = maya_asset.get_pipe_ids()
            return id_data
        script_path = os.path.join(resource.getScriptPath(), 'maya/find_pipeids.py')
        maya_path, valid = self.environ.get_specific_environ_value(
            'show_applications', self.application, 'path')
        application_module_path = resource.getModuleApplicationsPath()    
        module = common.get_subprocess_code(application_module_path, self.application)
        id_data, message = module.execute(maya_path, self.source_maya, script_path)        
        return id_data
          
    def take_thumbnail(self, button):
        output_path = None
        if self.standalone:
            current_file = swidgets.brows_file(
                'find the thumbnail(image) file', resource.getImageFormats())
            if not current_file:
                return
            output_path = os.path.join(
                tempfile.gettempdir(),
                'thumbnail_%s.png' % resource.getCurrentDateKey())
            output_path = swidgets.image_resize(current_file, output_path, 768, 540)  
        else:            
            from studio_usd_pipe.api import studioMaya
            smaya = studioMaya.Maya()
            output_path, w, h = smaya.vieport_snapshot(
                output_path=None,
                width=768,
                height=540,
                )
        if not os.path.isfile(output_path):
            return
        qsize = button.minimumSize()            
        swidgets.image_to_button(
            button, qsize.width(), qsize.height(), path=output_path)
        self.button_thumbnail.setToolTip(output_path)
 
    def set_current_caption(self):
        caption = self.combobox_caption.currentText()
        if not caption:
            self.combobox_dependency.clear()
            self.textedit_description.clear()
            self.combobox_latest_version.clear()
            self.combobox_next_version.clear()
            return
        if not self.source_maya:
            QtWidgets.QMessageBox.warning(
                self,
                'warning',
                'Load the maya file and try!...',
                QtWidgets.QMessageBox.Ok
                )
            self.combobox_caption.setCurrentIndex(0)           
            return            
        self.set_dependency(caption)
        self.set_current_version()
     
    def set_current_version(self):
        caption = self.combobox_caption.currentText()
        subfield = self.combobox_subfield.currentText()
        semantic_version = self.combobox_version.currentIndex()
        # disable type and tag
        type_data = self.spipe.get_caption_type()
        self.combobox_type.setEnabled(True)
        self.combobox_tag.setEnabled(True)
        if caption in type_data:
            types = self.spipe.pipe_inputs['type']['values']
            self.combobox_type.setCurrentIndex(types.index(type_data[caption][0]))
            self.combobox_type.setEnabled(False)
        tag_data = self.spipe.get_caption_tag()
        if caption in tag_data:
            tags = self.spipe.pipe_inputs['tag']['values']
            self.combobox_tag.setCurrentIndex(tags.index(tag_data[caption][0]))
            self.combobox_tag.setEnabled(False)
        versions = self.spipe.get_versions(caption, subfield)
        if not versions:
            versions = [None]
        self.combobox_latest_version.clear()        
        self.combobox_latest_version.addItems(versions)
        next_version = self.spipe.get_next_version(caption, semantic_version, subfield)
        self.combobox_next_version.clear()        
        self.combobox_next_version.addItem(next_version)
 
    def set_dependency(self, caption):
        self.combobox_dependency.clear()
        dependency, dependencies = self.get_dependencies(caption, self.pipe_ids)
        icon_path = os.path.join(resource.getIconPath(), 'tick.png')
        for each in dependencies:
            if each == dependency:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.combobox_dependency.addItem(icon, each)
            else:
                self.combobox_dependency.addItem(each)        
     
    def get_dependencies(self, caption, id_data):
        dependencies = self.spipe.get_dependencies(caption)
        if not id_data:
            return None, dependencies
        if 'ssubfield' not in id_data:
            return None, dependencies
        current_subfield = id_data['ssubfield']['value']
        if current_subfield == 'model':
            dependency = id_data['sversion']['value']
        else:
            dependency = id_data['sdependency']['value']
        return dependency, dependencies
 
    def get_widget_data(self):
        widgets = {
            'caption': self.combobox_caption,
            'subfield': self.combobox_subfield,
            'type': self.combobox_type,
            'tag': self.combobox_tag,
            'dependency': self.combobox_dependency,
            'thumbnail': self.button_thumbnail,
            'description': self.textedit_description,
            'version': self.combobox_next_version,
            }
        widget_data = {}        
        for key, widget in widgets.items():
            widget_value = None
            if isinstance(widget, QtWidgets.QComboBox):
                widget_value = widget.currentText().encode()
            if isinstance(widget, QtWidgets.QTextEdit):
                widget_value = widget.toPlainText().encode()
            if isinstance(widget, QtWidgets.QPushButton):
                widget_value = widget.toolTip().encode()
            if not widget_value:
                widget_value = None
            widget_data.setdefault(key, widget_value)        
        widget_data['user'] = getpass.getuser()
        return widget_data
     
    def do_publish(self):
        input_data = self.get_widget_data()
        if not self.source_maya:
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'load the maya file and try!...', QtWidgets.QMessageBox.Ok)
            return            
        if None in input_data.values():
            QtWidgets.QMessageBox.warning(
                self, 'Warning', 'Empty inputs!...', QtWidgets.QMessageBox.Ok)
            return  
        print '\n#header: inputs'
        input_data['subfield'] = input_data['subfield']
        input_data['source'] = self.source_maya
        input_data['standalone'] = self.standalone
        input_data['application'] = self.application
        print json.dumps(input_data, indent=4)

        push = studioPush.Push(self.current_show, self.pipe)
        if self.standalone:
            valid, message = push.do_standalone_publish(repair=True, **input_data)
        else:
            valid, message = push.do_publish(repair=True, **input_data)
        if not valid:
            QtWidgets.QMessageBox.critical(
                self, 'critical', message, QtWidgets.QMessageBox.Ok)
            return 
        self.set_default()
        self.set_current_version()       
        QtWidgets.QMessageBox.information(
            self, 'Success', 'Done!...', QtWidgets.QMessageBox.Ok)
         
  
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window(parent=None, standalone=True)
    window.show()
    sys.exit(app.exec_()) 

