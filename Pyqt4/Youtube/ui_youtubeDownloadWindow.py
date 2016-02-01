# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\youtubeDownloadWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_YoutubeDownloadWindow(object):
    def setupUi(self, YoutubeDownloadWindow):
        YoutubeDownloadWindow.setObjectName(_fromUtf8("YoutubeDownloadWindow"))
        YoutubeDownloadWindow.resize(804, 347)
        self.centralwidget = QtGui.QWidget(YoutubeDownloadWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 300))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.search_box = QtGui.QLineEdit(self.centralwidget)
        self.search_box.setObjectName(_fromUtf8("search_box"))
        self.horizontalLayout.addWidget(self.search_box)
        self.search_btn = QtGui.QPushButton(self.centralwidget)
        self.search_btn.setObjectName(_fromUtf8("search_btn"))
        self.horizontalLayout.addWidget(self.search_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.video_list = QtGui.QListWidget(self.centralwidget)
        self.video_list.setObjectName(_fromUtf8("video_list"))
        self.verticalLayout.addWidget(self.video_list)
        YoutubeDownloadWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(YoutubeDownloadWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        YoutubeDownloadWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(YoutubeDownloadWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        YoutubeDownloadWindow.setStatusBar(self.statusbar)
        self.videoDockWidget = QtGui.QDockWidget(YoutubeDownloadWindow)
        self.videoDockWidget.setMinimumSize(QtCore.QSize(400, 300))
        self.videoDockWidget.setObjectName(_fromUtf8("videoDockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.videoDockWidget.setWidget(self.dockWidgetContents)
        YoutubeDownloadWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.videoDockWidget)

        self.retranslateUi(YoutubeDownloadWindow)
        QtCore.QMetaObject.connectSlotsByName(YoutubeDownloadWindow)

    def retranslateUi(self, YoutubeDownloadWindow):
        YoutubeDownloadWindow.setWindowTitle(_translate("YoutubeDownloadWindow", "MainWindow", None))
        self.search_btn.setText(_translate("YoutubeDownloadWindow", "Tìm Kiếm", None))

