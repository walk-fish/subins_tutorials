# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/source_code/subins_tutorials/dumps/publish_01.ui'
#
# Created: Sun May 17 02:35:55 2020
#      by: pyside-uic 0.2.13 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(744, 598)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupbox_label = QtGui.QGroupBox(Form)
        self.groupbox_label.setObjectName("groupbox_label")
        self.horizontallayout_data = QtGui.QHBoxLayout(self.groupbox_label)
        self.horizontallayout_data.setSpacing(10)
        self.horizontallayout_data.setContentsMargins(10, 12, 10, 10)
        self.horizontallayout_data.setObjectName("horizontallayout_data")
        self.button_label = QtGui.QPushButton(self.groupbox_label)
        self.button_label.setMinimumSize(QtCore.QSize(100, 100))
        self.button_label.setMaximumSize(QtCore.QSize(100, 100))
        self.button_label.setObjectName("button_label")
        self.horizontallayout_data.addWidget(self.button_label)
        self.label_2 = QtGui.QLabel(self.groupbox_label)
        self.label_2.setStyleSheet("background-color: rgb(188, 188, 188);\n"
"font: 14pt \"Sans Serif\";")
        self.label_2.setObjectName("label_2")
        self.horizontallayout_data.addWidget(self.label_2)
        self.button_open = QtGui.QPushButton(self.groupbox_label)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_open.sizePolicy().hasHeightForWidth())
        self.button_open.setSizePolicy(sizePolicy)
        self.button_open.setObjectName("button_open")
        self.horizontallayout_data.addWidget(self.button_open)
        self.verticalLayout.addWidget(self.groupbox_label)
        self.groupbox_input = QtGui.QGroupBox(Form)
        self.groupbox_input.setObjectName("groupbox_input")
        self.verticallayout_input = QtGui.QVBoxLayout(self.groupbox_input)
        self.verticallayout_input.setSpacing(10)
        self.verticallayout_input.setContentsMargins(10, 10, 10, 10)
        self.verticallayout_input.setObjectName("verticallayout_input")
        self.gridlayout_input = QtGui.QGridLayout()
        self.gridlayout_input.setObjectName("gridlayout_input")
        self.button_thumbnail = QtGui.QPushButton(self.groupbox_input)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_thumbnail.sizePolicy().hasHeightForWidth())
        self.button_thumbnail.setSizePolicy(sizePolicy)
        self.button_thumbnail.setMinimumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setMaximumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setObjectName("button_thumbnail")
        self.gridlayout_input.addWidget(self.button_thumbnail, 1, 0, 1, 1)
        self.label_thumbnail = QtGui.QLabel(self.groupbox_input)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_thumbnail.sizePolicy().hasHeightForWidth())
        self.label_thumbnail.setSizePolicy(sizePolicy)
        self.label_thumbnail.setObjectName("label_thumbnail")
        self.gridlayout_input.addWidget(self.label_thumbnail, 0, 0, 1, 1)
        self.label_description = QtGui.QLabel(self.groupbox_input)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_description.sizePolicy().hasHeightForWidth())
        self.label_description.setSizePolicy(sizePolicy)
        self.label_description.setObjectName("label_description")
        self.gridlayout_input.addWidget(self.label_description, 0, 1, 1, 1)
        self.textedit_description = QtGui.QTextEdit(self.groupbox_input)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textedit_description.sizePolicy().hasHeightForWidth())
        self.textedit_description.setSizePolicy(sizePolicy)
        self.textedit_description.setMinimumSize(QtCore.QSize(0, 180))
        self.textedit_description.setMaximumSize(QtCore.QSize(16777215, 180))
        self.textedit_description.setObjectName("textedit_description")
        self.gridlayout_input.addWidget(self.textedit_description, 1, 1, 1, 1)
        self.verticallayout_input.addLayout(self.gridlayout_input)
        self.gridlayout_inputs = QtGui.QGridLayout()
        self.gridlayout_inputs.setContentsMargins(4, 4, 3, 10)
        self.gridlayout_inputs.setHorizontalSpacing(5)
        self.gridlayout_inputs.setVerticalSpacing(10)
        self.gridlayout_inputs.setObjectName("gridlayout_inputs")
        self.label_category = QtGui.QLabel(self.groupbox_input)
        self.label_category.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_category.setObjectName("label_category")
        self.gridlayout_inputs.addWidget(self.label_category, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridlayout_inputs.addItem(spacerItem, 0, 2, 1, 1)
        self.combobox_category = QtGui.QComboBox(self.groupbox_input)
        self.combobox_category.setMinimumSize(QtCore.QSize(150, 0))
        self.combobox_category.setEditable(False)
        self.combobox_category.setInsertPolicy(QtGui.QComboBox.InsertAfterCurrent)
        self.combobox_category.setObjectName("combobox_category")
        self.combobox_category.addItem("")
        self.gridlayout_inputs.addWidget(self.combobox_category, 0, 1, 1, 1)
        self.label_tag = QtGui.QLabel(self.groupbox_input)
        self.label_tag.setObjectName("label_tag")
        self.gridlayout_inputs.addWidget(self.label_tag, 1, 0, 1, 1)
        self.combobox_tag = QtGui.QComboBox(self.groupbox_input)
        self.combobox_tag.setObjectName("combobox_tag")
        self.gridlayout_inputs.addWidget(self.combobox_tag, 1, 1, 1, 1)
        self.verticallayout_input.addLayout(self.gridlayout_inputs)
        self.horizontallayout_input = QtGui.QHBoxLayout()
        self.horizontallayout_input.setObjectName("horizontallayout_input")
        self.verticallayout_input.addLayout(self.horizontallayout_input)
        self.verticalLayout.addWidget(self.groupbox_input)
        self.groupbox_publish = QtGui.QGroupBox(Form)
        self.groupbox_publish.setObjectName("groupbox_publish")
        self.horizontallayout_publish = QtGui.QHBoxLayout(self.groupbox_publish)
        self.horizontallayout_publish.setSpacing(10)
        self.horizontallayout_publish.setContentsMargins(10, 10, 10, 10)
        self.horizontallayout_publish.setObjectName("horizontallayout_publish")
        self.label_publish = QtGui.QLabel(self.groupbox_publish)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_publish.sizePolicy().hasHeightForWidth())
        self.label_publish.setSizePolicy(sizePolicy)
        self.label_publish.setObjectName("label_publish")
        self.horizontallayout_publish.addWidget(self.label_publish)
        self.combobox_publish = QtGui.QComboBox(self.groupbox_publish)
        self.combobox_publish.setObjectName("combobox_publish")
        self.combobox_publish.addItem("")
        self.combobox_publish.addItem("")
        self.combobox_publish.addItem("")
        self.horizontallayout_publish.addWidget(self.combobox_publish)
        self.label_version = QtGui.QLabel(self.groupbox_publish)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_version.sizePolicy().hasHeightForWidth())
        self.label_version.setSizePolicy(sizePolicy)
        self.label_version.setAlignment(QtCore.Qt.AlignCenter)
        self.label_version.setObjectName("label_version")
        self.horizontallayout_publish.addWidget(self.label_version)
        self.button_publish = QtGui.QPushButton(self.groupbox_publish)
        self.button_publish.setObjectName("button_publish")
        self.horizontallayout_publish.addWidget(self.button_publish)
        self.verticalLayout.addWidget(self.groupbox_publish)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupbox_label.setTitle(QtGui.QApplication.translate("Form", "Input File", None, QtGui.QApplication.UnicodeUTF8))
        self.button_label.setText(QtGui.QApplication.translate("Form", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", None, QtGui.QApplication.UnicodeUTF8))
        self.button_open.setText(QtGui.QApplication.translate("Form", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupbox_input.setTitle(QtGui.QApplication.translate("Form", "Inputs", None, QtGui.QApplication.UnicodeUTF8))
        self.button_thumbnail.setText(QtGui.QApplication.translate("Form", "Image", None, QtGui.QApplication.UnicodeUTF8))
        self.label_thumbnail.setText(QtGui.QApplication.translate("Form", "Thumbnail", None, QtGui.QApplication.UnicodeUTF8))
        self.label_description.setText(QtGui.QApplication.translate("Form", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.label_category.setText(QtGui.QApplication.translate("Form", "Cat", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_category.setItemText(0, QtGui.QApplication.translate("Form", "Model", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tag.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupbox_publish.setTitle(QtGui.QApplication.translate("Form", "Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.label_publish.setText(QtGui.QApplication.translate("Form", "Next Avilable Publish versions", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_publish.setItemText(0, QtGui.QApplication.translate("Form", "Major", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_publish.setItemText(1, QtGui.QApplication.translate("Form", "Minor", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_publish.setItemText(2, QtGui.QApplication.translate("Form", "Patch", None, QtGui.QApplication.UnicodeUTF8))
        self.label_version.setText(QtGui.QApplication.translate("Form", "0.0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_publish.setText(QtGui.QApplication.translate("Form", "Publish", None, QtGui.QApplication.UnicodeUTF8))

