# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/subins_tutorials/dumps/publish_01.ui',
# licensing of '/venture/subins_tutorials/dumps/publish_01.ui' applies.
#
# Created: Mon Feb  3 02:27:12 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(744, 598)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupbox_label = QtWidgets.QGroupBox(Form)
        self.groupbox_label.setObjectName("groupbox_label")
        self.horizontallayout_data = QtWidgets.QHBoxLayout(self.groupbox_label)
        self.horizontallayout_data.setSpacing(10)
        self.horizontallayout_data.setContentsMargins(10, 12, 10, 10)
        self.horizontallayout_data.setObjectName("horizontallayout_data")
        self.button_label = QtWidgets.QPushButton(self.groupbox_label)
        self.button_label.setMinimumSize(QtCore.QSize(100, 100))
        self.button_label.setMaximumSize(QtCore.QSize(100, 100))
        self.button_label.setObjectName("button_label")
        self.horizontallayout_data.addWidget(self.button_label)
        self.label_2 = QtWidgets.QLabel(self.groupbox_label)
        self.label_2.setStyleSheet("background-color: rgb(188, 188, 188);\n"
"font: 14pt \"Sans Serif\";")
        self.label_2.setObjectName("label_2")
        self.horizontallayout_data.addWidget(self.label_2)
        self.button_open = QtWidgets.QPushButton(self.groupbox_label)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_open.sizePolicy().hasHeightForWidth())
        self.button_open.setSizePolicy(sizePolicy)
        self.button_open.setObjectName("button_open")
        self.horizontallayout_data.addWidget(self.button_open)
        self.verticalLayout.addWidget(self.groupbox_label)
        self.groupbox_input = QtWidgets.QGroupBox(Form)
        self.groupbox_input.setObjectName("groupbox_input")
        self.verticallayout_input = QtWidgets.QVBoxLayout(self.groupbox_input)
        self.verticallayout_input.setSpacing(10)
        self.verticallayout_input.setContentsMargins(10, 10, 10, 10)
        self.verticallayout_input.setObjectName("verticallayout_input")
        self.gridlayout_input = QtWidgets.QGridLayout()
        self.gridlayout_input.setObjectName("gridlayout_input")
        self.button_thumbnail = QtWidgets.QPushButton(self.groupbox_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_thumbnail.sizePolicy().hasHeightForWidth())
        self.button_thumbnail.setSizePolicy(sizePolicy)
        self.button_thumbnail.setMinimumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setMaximumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setObjectName("button_thumbnail")
        self.gridlayout_input.addWidget(self.button_thumbnail, 1, 0, 1, 1)
        self.label_thumbnail = QtWidgets.QLabel(self.groupbox_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_thumbnail.sizePolicy().hasHeightForWidth())
        self.label_thumbnail.setSizePolicy(sizePolicy)
        self.label_thumbnail.setObjectName("label_thumbnail")
        self.gridlayout_input.addWidget(self.label_thumbnail, 0, 0, 1, 1)
        self.label_description = QtWidgets.QLabel(self.groupbox_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_description.sizePolicy().hasHeightForWidth())
        self.label_description.setSizePolicy(sizePolicy)
        self.label_description.setObjectName("label_description")
        self.gridlayout_input.addWidget(self.label_description, 0, 1, 1, 1)
        self.textedit_description = QtWidgets.QTextEdit(self.groupbox_input)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textedit_description.sizePolicy().hasHeightForWidth())
        self.textedit_description.setSizePolicy(sizePolicy)
        self.textedit_description.setMinimumSize(QtCore.QSize(0, 180))
        self.textedit_description.setMaximumSize(QtCore.QSize(16777215, 180))
        self.textedit_description.setObjectName("textedit_description")
        self.gridlayout_input.addWidget(self.textedit_description, 1, 1, 1, 1)
        self.verticallayout_input.addLayout(self.gridlayout_input)
        self.gridlayout_inputs = QtWidgets.QGridLayout()
        self.gridlayout_inputs.setContentsMargins(4, 4, 3, 10)
        self.gridlayout_inputs.setHorizontalSpacing(5)
        self.gridlayout_inputs.setVerticalSpacing(10)
        self.gridlayout_inputs.setObjectName("gridlayout_inputs")
        self.label_category = QtWidgets.QLabel(self.groupbox_input)
        self.label_category.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_category.setObjectName("label_category")
        self.gridlayout_inputs.addWidget(self.label_category, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout_inputs.addItem(spacerItem, 0, 2, 1, 1)
        self.combobox_category = QtWidgets.QComboBox(self.groupbox_input)
        self.combobox_category.setMinimumSize(QtCore.QSize(150, 0))
        self.combobox_category.setEditable(False)
        self.combobox_category.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.combobox_category.setObjectName("combobox_category")
        self.combobox_category.addItem("")
        self.gridlayout_inputs.addWidget(self.combobox_category, 0, 1, 1, 1)
        self.label_tag = QtWidgets.QLabel(self.groupbox_input)
        self.label_tag.setObjectName("label_tag")
        self.gridlayout_inputs.addWidget(self.label_tag, 1, 0, 1, 1)
        self.combobox_tag = QtWidgets.QComboBox(self.groupbox_input)
        self.combobox_tag.setObjectName("combobox_tag")
        self.gridlayout_inputs.addWidget(self.combobox_tag, 1, 1, 1, 1)
        self.verticallayout_input.addLayout(self.gridlayout_inputs)
        self.horizontallayout_input = QtWidgets.QHBoxLayout()
        self.horizontallayout_input.setObjectName("horizontallayout_input")
        self.verticallayout_input.addLayout(self.horizontallayout_input)
        self.verticalLayout.addWidget(self.groupbox_input)
        self.groupbox_publish = QtWidgets.QGroupBox(Form)
        self.groupbox_publish.setObjectName("groupbox_publish")
        self.horizontallayout_publish = QtWidgets.QHBoxLayout(self.groupbox_publish)
        self.horizontallayout_publish.setSpacing(10)
        self.horizontallayout_publish.setContentsMargins(10, 10, 10, 10)
        self.horizontallayout_publish.setObjectName("horizontallayout_publish")
        self.label_publish = QtWidgets.QLabel(self.groupbox_publish)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_publish.sizePolicy().hasHeightForWidth())
        self.label_publish.setSizePolicy(sizePolicy)
        self.label_publish.setObjectName("label_publish")
        self.horizontallayout_publish.addWidget(self.label_publish)
        self.combobox_publish = QtWidgets.QComboBox(self.groupbox_publish)
        self.combobox_publish.setObjectName("combobox_publish")
        self.combobox_publish.addItem("")
        self.combobox_publish.addItem("")
        self.combobox_publish.addItem("")
        self.horizontallayout_publish.addWidget(self.combobox_publish)
        self.label_version = QtWidgets.QLabel(self.groupbox_publish)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_version.sizePolicy().hasHeightForWidth())
        self.label_version.setSizePolicy(sizePolicy)
        self.label_version.setAlignment(QtCore.Qt.AlignCenter)
        self.label_version.setObjectName("label_version")
        self.horizontallayout_publish.addWidget(self.label_version)
        self.button_publish = QtWidgets.QPushButton(self.groupbox_publish)
        self.button_publish.setObjectName("button_publish")
        self.horizontallayout_publish.addWidget(self.button_publish)
        self.verticalLayout.addWidget(self.groupbox_publish)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.groupbox_label.setTitle(QtWidgets.QApplication.translate("Form", "Input File", None, -1))
        self.button_label.setText(QtWidgets.QApplication.translate("Form", "PushButton", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", None, -1))
        self.button_open.setText(QtWidgets.QApplication.translate("Form", "...", None, -1))
        self.groupbox_input.setTitle(QtWidgets.QApplication.translate("Form", "Inputs", None, -1))
        self.button_thumbnail.setText(QtWidgets.QApplication.translate("Form", "Image", None, -1))
        self.label_thumbnail.setText(QtWidgets.QApplication.translate("Form", "Thumbnail", None, -1))
        self.label_description.setText(QtWidgets.QApplication.translate("Form", "Description", None, -1))
        self.label_category.setText(QtWidgets.QApplication.translate("Form", "Cat", None, -1))
        self.combobox_category.setItemText(0, QtWidgets.QApplication.translate("Form", "Model", None, -1))
        self.label_tag.setText(QtWidgets.QApplication.translate("Form", "TextLabel", None, -1))
        self.groupbox_publish.setTitle(QtWidgets.QApplication.translate("Form", "Publish", None, -1))
        self.label_publish.setText(QtWidgets.QApplication.translate("Form", "Next Avilable Publish versions", None, -1))
        self.combobox_publish.setItemText(0, QtWidgets.QApplication.translate("Form", "Major", None, -1))
        self.combobox_publish.setItemText(1, QtWidgets.QApplication.translate("Form", "Minor", None, -1))
        self.combobox_publish.setItemText(2, QtWidgets.QApplication.translate("Form", "Patch", None, -1))
        self.label_version.setText(QtWidgets.QApplication.translate("Form", "0.0.0", None, -1))
        self.button_publish.setText(QtWidgets.QApplication.translate("Form", "Publish", None, -1))

