# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/venture/source_code/subins_tutorials/dumps/builder.ui'
#
# Created: Tue May 12 10:45:35 2020
#      by: pyside-uic 0.2.13 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(926, 648)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treewidget = QtGui.QTreeWidget(self.splitter)
        self.treewidget.setAlternatingRowColors(True)
        self.treewidget.setObjectName("treewidget")
        item_0 = QtGui.QTreeWidgetItem(self.treewidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.treewidget)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.treewidget.header().setVisible(False)
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticallayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticallayout.setContentsMargins(0, 0, 0, 0)
        self.verticallayout.setObjectName("verticallayout")
        self.groupbox_input = QtGui.QGroupBox(self.layoutWidget)
        self.groupbox_input.setObjectName("groupbox_input")
        self.groupbox_publish = QtGui.QGroupBox(self.groupbox_input)
        self.groupbox_publish.setGeometry(QtCore.QRect(10, 380, 573, 225))
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
        self.horizontallayout_publish.addWidget(self.combobox_publish)
        self.button_publish = QtGui.QPushButton(self.groupbox_publish)
        self.button_publish.setObjectName("button_publish")
        self.horizontallayout_publish.addWidget(self.button_publish)
        self.widget = QtGui.QWidget(self.groupbox_input)
        self.widget.setObjectName("widget")
        self.gridlayout_input = QtGui.QGridLayout(self.widget)
        self.gridlayout_input.setContentsMargins(0, 0, 0, 0)
        self.gridlayout_input.setObjectName("gridlayout_input")
        self.button_thumbnail = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_thumbnail.sizePolicy().hasHeightForWidth())
        self.button_thumbnail.setSizePolicy(sizePolicy)
        self.button_thumbnail.setMinimumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setMaximumSize(QtCore.QSize(256, 180))
        self.button_thumbnail.setObjectName("button_thumbnail")
        self.gridlayout_input.addWidget(self.button_thumbnail, 1, 0, 1, 1)
        self.label_thumbnail = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_thumbnail.sizePolicy().hasHeightForWidth())
        self.label_thumbnail.setSizePolicy(sizePolicy)
        self.label_thumbnail.setObjectName("label_thumbnail")
        self.gridlayout_input.addWidget(self.label_thumbnail, 0, 0, 1, 1)
        self.label_description = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_description.sizePolicy().hasHeightForWidth())
        self.label_description.setSizePolicy(sizePolicy)
        self.label_description.setObjectName("label_description")
        self.gridlayout_input.addWidget(self.label_description, 0, 1, 1, 1)
        self.textedit_description = QtGui.QTextEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textedit_description.sizePolicy().hasHeightForWidth())
        self.textedit_description.setSizePolicy(sizePolicy)
        self.textedit_description.setMinimumSize(QtCore.QSize(0, 180))
        self.textedit_description.setMaximumSize(QtCore.QSize(16777215, 180))
        self.textedit_description.setObjectName("textedit_description")
        self.gridlayout_input.addWidget(self.textedit_description, 1, 1, 1, 1)
        self.verticallayout.addWidget(self.groupbox_input)
        self.verticalLayout_2.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.action_add = QtGui.QAction(MainWindow)
        self.action_add.setObjectName("action_add")
        self.action_remove = QtGui.QAction(MainWindow)
        self.action_remove.setObjectName("action_remove")
        self.action_reload = QtGui.QAction(MainWindow)
        self.action_reload.setObjectName("action_reload")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.treewidget.isSortingEnabled()
        self.treewidget.setSortingEnabled(False)
        self.treewidget.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "Assets", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "Hero", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.topLevelItem(0).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "Demon", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.topLevelItem(0).child(2).setText(0, QtGui.QApplication.translate("MainWindow", "Girl", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.topLevelItem(1).setText(0, QtGui.QApplication.translate("MainWindow", "Scene", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("MainWindow", "Shot_001", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.topLevelItem(1).child(1).setText(0, QtGui.QApplication.translate("MainWindow", "Shot_002", None, QtGui.QApplication.UnicodeUTF8))
        self.treewidget.setSortingEnabled(__sortingEnabled)
        self.groupbox_input.setTitle(QtGui.QApplication.translate("MainWindow", "Inputs", None, QtGui.QApplication.UnicodeUTF8))
        self.groupbox_publish.setTitle(QtGui.QApplication.translate("MainWindow", "Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.label_publish.setText(QtGui.QApplication.translate("MainWindow", "Next Avilable Publish versions", None, QtGui.QApplication.UnicodeUTF8))
        self.button_publish.setText(QtGui.QApplication.translate("MainWindow", "Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.button_thumbnail.setText(QtGui.QApplication.translate("MainWindow", "Image", None, QtGui.QApplication.UnicodeUTF8))
        self.label_thumbnail.setText(QtGui.QApplication.translate("MainWindow", "Thumbnail", None, QtGui.QApplication.UnicodeUTF8))
        self.label_description.setText(QtGui.QApplication.translate("MainWindow", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.action_add.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.action_add.setToolTip(QtGui.QApplication.translate("MainWindow", "Add Items", None, QtGui.QApplication.UnicodeUTF8))
        self.action_add.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_remove.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.action_remove.setToolTip(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.action_remove.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))
        self.action_reload.setText(QtGui.QApplication.translate("MainWindow", "Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.action_reload.setToolTip(QtGui.QApplication.translate("MainWindow", "Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.action_reload.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))

