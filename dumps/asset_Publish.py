# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/source_code/subins_tutorials/dumps/asset_Publish.ui'
#
# Created: Sun May 17 02:35:54 2020
#      by: pyside-uic 0.2.13 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(623, 680)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticallayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticallayout.setObjectName("verticallayout")
        self.groupbox_source = QtGui.QGroupBox(self.centralwidget)
        self.groupbox_source.setObjectName("groupbox_source")
        self.horizontallayout_source = QtGui.QHBoxLayout(self.groupbox_source)
        self.horizontallayout_source.setSpacing(10)
        self.horizontallayout_source.setContentsMargins(10, 10, 10, 10)
        self.horizontallayout_source.setObjectName("horizontallayout_source")
        self.button_open = QtGui.QPushButton(self.groupbox_source)
        self.button_open.setObjectName("button_open")
        self.horizontallayout_source.addWidget(self.button_open)
        self.lineedit_source = QtGui.QLineEdit(self.groupbox_source)
        self.lineedit_source.setObjectName("lineedit_source")
        self.horizontallayout_source.addWidget(self.lineedit_source)
        self.verticallayout.addWidget(self.groupbox_source)
        self.groupbox_inputs = QtGui.QGroupBox(self.centralwidget)
        self.groupbox_inputs.setObjectName("groupbox_inputs")
        self.gridlayout_inputs = QtGui.QGridLayout(self.groupbox_inputs)
        self.gridlayout_inputs.setContentsMargins(5, 6, 19, 44)
        self.gridlayout_inputs.setHorizontalSpacing(10)
        self.gridlayout_inputs.setObjectName("gridlayout_inputs")
        self.label_thumbnail = QtGui.QLabel(self.groupbox_inputs)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_thumbnail.sizePolicy().hasHeightForWidth())
        self.label_thumbnail.setSizePolicy(sizePolicy)
        self.label_thumbnail.setAlignment(QtCore.Qt.AlignCenter)
        self.label_thumbnail.setObjectName("label_thumbnail")
        self.gridlayout_inputs.addWidget(self.label_thumbnail, 5, 0, 1, 1)
        self.label_description = QtGui.QLabel(self.groupbox_inputs)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_description.sizePolicy().hasHeightForWidth())
        self.label_description.setSizePolicy(sizePolicy)
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.gridlayout_inputs.addWidget(self.label_description, 5, 1, 1, 1)
        self.line_thumbnail = QtGui.QFrame(self.groupbox_inputs)
        self.line_thumbnail.setFrameShape(QtGui.QFrame.HLine)
        self.line_thumbnail.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_thumbnail.setObjectName("line_thumbnail")
        self.gridlayout_inputs.addWidget(self.line_thumbnail, 4, 0, 1, 1)
        self.label_subfield = QtGui.QLabel(self.groupbox_inputs)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_subfield.sizePolicy().hasHeightForWidth())
        self.label_subfield.setSizePolicy(sizePolicy)
        self.label_subfield.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_subfield.setObjectName("label_subfield")
        self.gridlayout_inputs.addWidget(self.label_subfield, 1, 0, 1, 1)
        self.combobox_tag = QtGui.QComboBox(self.groupbox_inputs)
        self.combobox_tag.setEnabled(True)
        self.combobox_tag.setEditable(False)
        self.combobox_tag.setInsertPolicy(QtGui.QComboBox.InsertAfterCurrent)
        self.combobox_tag.setObjectName("combobox_tag")
        self.gridlayout_inputs.addWidget(self.combobox_tag, 3, 1, 1, 1)
        self.combobox_palette = QtGui.QComboBox(self.groupbox_inputs)
        self.combobox_palette.setObjectName("combobox_palette")
        self.gridlayout_inputs.addWidget(self.combobox_palette, 0, 1, 1, 1)
        self.combobox_subfield = QtGui.QComboBox(self.groupbox_inputs)
        self.combobox_subfield.setEditable(False)
        self.combobox_subfield.setInsertPolicy(QtGui.QComboBox.InsertAfterCurrent)
        self.combobox_subfield.setObjectName("combobox_subfield")
        self.combobox_subfield.addItem("")
        self.gridlayout_inputs.addWidget(self.combobox_subfield, 1, 1, 1, 1)
        self.label_tag = QtGui.QLabel(self.groupbox_inputs)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_tag.sizePolicy().hasHeightForWidth())
        self.label_tag.setSizePolicy(sizePolicy)
        self.label_tag.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_tag.setObjectName("label_tag")
        self.gridlayout_inputs.addWidget(self.label_tag, 3, 0, 1, 1)
        self.label_palette = QtGui.QLabel(self.groupbox_inputs)
        self.label_palette.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_palette.setObjectName("label_palette")
        self.gridlayout_inputs.addWidget(self.label_palette, 0, 0, 1, 1)
        self.line_description = QtGui.QFrame(self.groupbox_inputs)
        self.line_description.setFrameShape(QtGui.QFrame.HLine)
        self.line_description.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_description.setObjectName("line_description")
        self.gridlayout_inputs.addWidget(self.line_description, 4, 1, 1, 1)
        self.button_thumbnail = QtGui.QPushButton(self.groupbox_inputs)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_thumbnail.sizePolicy().hasHeightForWidth())
        self.button_thumbnail.setSizePolicy(sizePolicy)
        self.button_thumbnail.setMinimumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setMaximumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setObjectName("button_thumbnail")
        self.gridlayout_inputs.addWidget(self.button_thumbnail, 6, 0, 1, 1)
        self.textedit_description = QtGui.QTextEdit(self.groupbox_inputs)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textedit_description.sizePolicy().hasHeightForWidth())
        self.textedit_description.setSizePolicy(sizePolicy)
        self.textedit_description.setMinimumSize(QtCore.QSize(0, 180))
        self.textedit_description.setMaximumSize(QtCore.QSize(16777215, 180))
        self.textedit_description.setObjectName("textedit_description")
        self.gridlayout_inputs.addWidget(self.textedit_description, 6, 1, 1, 1)
        self.label_type = QtGui.QLabel(self.groupbox_inputs)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_type.sizePolicy().hasHeightForWidth())
        self.label_type.setSizePolicy(sizePolicy)
        self.label_type.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_type.setObjectName("label_type")
        self.gridlayout_inputs.addWidget(self.label_type, 2, 0, 1, 1)
        self.combobox_type = QtGui.QComboBox(self.groupbox_inputs)
        self.combobox_type.setEditable(False)
        self.combobox_type.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.combobox_type.setObjectName("combobox_type")
        self.gridlayout_inputs.addWidget(self.combobox_type, 2, 1, 1, 1)
        self.verticallayout.addWidget(self.groupbox_inputs)
        self.groupbox_publish = QtGui.QGroupBox(self.centralwidget)
        self.groupbox_publish.setObjectName("groupbox_publish")
        self.gridlayout_publish = QtGui.QGridLayout(self.groupbox_publish)
        self.gridlayout_publish.setObjectName("gridlayout_publish")
        self.label_publishtype = QtGui.QLabel(self.groupbox_publish)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_publishtype.sizePolicy().hasHeightForWidth())
        self.label_publishtype.setSizePolicy(sizePolicy)
        self.label_publishtype.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_publishtype.setObjectName("label_publishtype")
        self.gridlayout_publish.addWidget(self.label_publishtype, 0, 0, 1, 1)
        self.combobox_publishtype = QtGui.QComboBox(self.groupbox_publish)
        self.combobox_publishtype.setObjectName("combobox_publishtype")
        self.gridlayout_publish.addWidget(self.combobox_publishtype, 0, 1, 1, 1)
        self.label_versions = QtGui.QLabel(self.groupbox_publish)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_versions.sizePolicy().hasHeightForWidth())
        self.label_versions.setSizePolicy(sizePolicy)
        self.label_versions.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_versions.setObjectName("label_versions")
        self.gridlayout_publish.addWidget(self.label_versions, 1, 0, 1, 1)
        self.combobox_versions = QtGui.QComboBox(self.groupbox_publish)
        self.combobox_versions.setObjectName("combobox_versions")
        self.gridlayout_publish.addWidget(self.combobox_versions, 1, 1, 1, 1)
        self.label_nextversion = QtGui.QLabel(self.groupbox_publish)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_nextversion.sizePolicy().hasHeightForWidth())
        self.label_nextversion.setSizePolicy(sizePolicy)
        self.label_nextversion.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_nextversion.setObjectName("label_nextversion")
        self.gridlayout_publish.addWidget(self.label_nextversion, 2, 0, 1, 1)
        self.combobox_nextversion = QtGui.QComboBox(self.groupbox_publish)
        self.combobox_nextversion.setObjectName("combobox_nextversion")
        self.gridlayout_publish.addWidget(self.combobox_nextversion, 2, 1, 1, 1)
        self.button_publish = QtGui.QPushButton(self.groupbox_publish)
        self.button_publish.setObjectName("button_publish")
        self.gridlayout_publish.addWidget(self.button_publish, 3, 1, 1, 1)
        self.verticallayout.addWidget(self.groupbox_publish)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 623, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupbox_source.setTitle(QtGui.QApplication.translate("MainWindow", "Source File", None, QtGui.QApplication.UnicodeUTF8))
        self.button_open.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.groupbox_inputs.setTitle(QtGui.QApplication.translate("MainWindow", "Inputs", None, QtGui.QApplication.UnicodeUTF8))
        self.label_thumbnail.setText(QtGui.QApplication.translate("MainWindow", "Thumbnail", None, QtGui.QApplication.UnicodeUTF8))
        self.label_description.setText(QtGui.QApplication.translate("MainWindow", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.label_subfield.setText(QtGui.QApplication.translate("MainWindow", "Subfield", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_subfield.setItemText(0, QtGui.QApplication.translate("MainWindow", "subin", "ssssssssssssss", QtGui.QApplication.UnicodeUTF8))
        self.label_tag.setText(QtGui.QApplication.translate("MainWindow", "Tag", None, QtGui.QApplication.UnicodeUTF8))
        self.label_palette.setText(QtGui.QApplication.translate("MainWindow", "Palette", None, QtGui.QApplication.UnicodeUTF8))
        self.button_thumbnail.setText(QtGui.QApplication.translate("MainWindow", "Image", None, QtGui.QApplication.UnicodeUTF8))
        self.label_type.setText(QtGui.QApplication.translate("MainWindow", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.groupbox_publish.setTitle(QtGui.QApplication.translate("MainWindow", "Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.label_publishtype.setText(QtGui.QApplication.translate("MainWindow", "Publish Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_versions.setText(QtGui.QApplication.translate("MainWindow", "Versions", None, QtGui.QApplication.UnicodeUTF8))
        self.label_nextversion.setText(QtGui.QApplication.translate("MainWindow", "Next Avilable Publish versions", None, QtGui.QApplication.UnicodeUTF8))
        self.button_publish.setText(QtGui.QApplication.translate("MainWindow", "Publish", None, QtGui.QApplication.UnicodeUTF8))

