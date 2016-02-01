# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\youtubeItemWidget.ui'
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

class Ui_YoutubeItemWidget(object):
    def setupUi(self, YoutubeItemWidget):
        YoutubeItemWidget.setObjectName(_fromUtf8("YoutubeItemWidget"))
        YoutubeItemWidget.resize(569, 115)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(YoutubeItemWidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.thumbnail = QtGui.QLabel(YoutubeItemWidget)
        self.thumbnail.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thumbnail.sizePolicy().hasHeightForWidth())
        self.thumbnail.setSizePolicy(sizePolicy)
        self.thumbnail.setMinimumSize(QtCore.QSize(64, 64))
        self.thumbnail.setObjectName(_fromUtf8("thumbnail"))
        self.horizontalLayout_2.addWidget(self.thumbnail)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.title = QtGui.QLabel(YoutubeItemWidget)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName(_fromUtf8("title"))
        self.verticalLayout.addWidget(self.title)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.length = QtGui.QLabel(YoutubeItemWidget)
        self.length.setAlignment(QtCore.Qt.AlignCenter)
        self.length.setObjectName(_fromUtf8("length"))
        self.horizontalLayout.addWidget(self.length)
        self.author = QtGui.QLabel(YoutubeItemWidget)
        self.author.setAlignment(QtCore.Qt.AlignCenter)
        self.author.setObjectName(_fromUtf8("author"))
        self.horizontalLayout.addWidget(self.author)
        self.view = QtGui.QLabel(YoutubeItemWidget)
        self.view.setAlignment(QtCore.Qt.AlignCenter)
        self.view.setObjectName(_fromUtf8("view"))
        self.horizontalLayout.addWidget(self.view)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 5)

        self.retranslateUi(YoutubeItemWidget)
        QtCore.QMetaObject.connectSlotsByName(YoutubeItemWidget)

    def retranslateUi(self, YoutubeItemWidget):
        YoutubeItemWidget.setWindowTitle(_translate("YoutubeItemWidget", "Form", None))
        self.thumbnail.setText(_translate("YoutubeItemWidget", "TextLabel", None))
        self.title.setText(_translate("YoutubeItemWidget", "TextLabel", None))
        self.length.setText(_translate("YoutubeItemWidget", "TextLabel", None))
        self.author.setText(_translate("YoutubeItemWidget", "TextLabel", None))
        self.view.setText(_translate("YoutubeItemWidget", "TextLabel", None))

