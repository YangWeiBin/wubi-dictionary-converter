# Form implementation generated from reading ui file 'update_word.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_update_word(object):
    def setupUi(self, update_word):
        update_word.setObjectName("update_word")
        update_word.resize(658, 395)
        update_word.setMinimumSize(QtCore.QSize(0, 370))
        self.verticalLayout = QtWidgets.QVBoxLayout(update_word)
        self.verticalLayout.setObjectName("verticalLayout")
        self.apathConfBox_3 = QtWidgets.QGroupBox(parent=update_word)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apathConfBox_3.sizePolicy().hasHeightForWidth())
        self.apathConfBox_3.setSizePolicy(sizePolicy)
        self.apathConfBox_3.setMinimumSize(QtCore.QSize(0, 0))
        self.apathConfBox_3.setMaximumSize(QtCore.QSize(16777215, 1000000))
        self.apathConfBox_3.setObjectName("apathConfBox_3")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.apathConfBox_3)
        self.verticalLayout_14.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_14.setSpacing(4)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.codeEdit = QtWidgets.QLineEdit(parent=self.apathConfBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.codeEdit.sizePolicy().hasHeightForWidth())
        self.codeEdit.setSizePolicy(sizePolicy)
        self.codeEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.codeEdit.setText("")
        self.codeEdit.setObjectName("codeEdit")
        self.verticalLayout_14.addWidget(self.codeEdit)
        self.verticalLayout.addWidget(self.apathConfBox_3)
        self.bpathConfBox_2 = QtWidgets.QGroupBox(parent=update_word)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bpathConfBox_2.sizePolicy().hasHeightForWidth())
        self.bpathConfBox_2.setSizePolicy(sizePolicy)
        self.bpathConfBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.bpathConfBox_2.setMaximumSize(QtCore.QSize(16777215, 1000000))
        self.bpathConfBox_2.setObjectName("bpathConfBox_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.bpathConfBox_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.rankCombo = QtWidgets.QComboBox(parent=self.bpathConfBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rankCombo.sizePolicy().hasHeightForWidth())
        self.rankCombo.setSizePolicy(sizePolicy)
        self.rankCombo.setMinimumSize(QtCore.QSize(55, 35))
        self.rankCombo.setMaximumSize(QtCore.QSize(65, 45))
        self.rankCombo.setObjectName("rankCombo")
        self.rankCombo.addItem("")
        self.rankCombo.addItem("")
        self.rankCombo.addItem("")
        self.rankCombo.addItem("")
        self.rankCombo.addItem("")
        self.rankCombo.addItem("")
        self.rankCombo.addItem("")
        self.verticalLayout_10.addWidget(self.rankCombo)
        self.verticalLayout.addWidget(self.bpathConfBox_2)
        self.cpathConfBox = QtWidgets.QGroupBox(parent=update_word)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cpathConfBox.sizePolicy().hasHeightForWidth())
        self.cpathConfBox.setSizePolicy(sizePolicy)
        self.cpathConfBox.setMinimumSize(QtCore.QSize(0, 0))
        self.cpathConfBox.setMaximumSize(QtCore.QSize(16777215, 1000000))
        self.cpathConfBox.setObjectName("cpathConfBox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.cpathConfBox)
        self.verticalLayout_9.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_9.setSpacing(4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.wordEdit = QtWidgets.QLineEdit(parent=self.cpathConfBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wordEdit.sizePolicy().hasHeightForWidth())
        self.wordEdit.setSizePolicy(sizePolicy)
        self.wordEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.wordEdit.setText("")
        self.wordEdit.setObjectName("wordEdit")
        self.verticalLayout_9.addWidget(self.wordEdit)
        self.verticalLayout.addWidget(self.cpathConfBox)
        self.dpathConfBox_2 = QtWidgets.QGroupBox(parent=update_word)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dpathConfBox_2.sizePolicy().hasHeightForWidth())
        self.dpathConfBox_2.setSizePolicy(sizePolicy)
        self.dpathConfBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.dpathConfBox_2.setMaximumSize(QtCore.QSize(16777215, 1000000))
        self.dpathConfBox_2.setTitle("")
        self.dpathConfBox_2.setObjectName("dpathConfBox_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.dpathConfBox_2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label = QtWidgets.QLabel(parent=self.dpathConfBox_2)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_11.addWidget(self.label)
        self.verticalLayout.addWidget(self.dpathConfBox_2)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.yesPbn = QtWidgets.QPushButton(parent=update_word)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yesPbn.sizePolicy().hasHeightForWidth())
        self.yesPbn.setSizePolicy(sizePolicy)
        self.yesPbn.setMinimumSize(QtCore.QSize(140, 50))
        self.yesPbn.setMaximumSize(QtCore.QSize(16777215, 70))
        self.yesPbn.setObjectName("yesPbn")
        self.horizontalLayout_8.addWidget(self.yesPbn)
        self.cancelPbn = QtWidgets.QPushButton(parent=update_word)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelPbn.sizePolicy().hasHeightForWidth())
        self.cancelPbn.setSizePolicy(sizePolicy)
        self.cancelPbn.setMinimumSize(QtCore.QSize(140, 50))
        self.cancelPbn.setMaximumSize(QtCore.QSize(16777215, 70))
        self.cancelPbn.setObjectName("cancelPbn")
        self.horizontalLayout_8.addWidget(self.cancelPbn)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.verticalLayout_8)

        self.retranslateUi(update_word)
        QtCore.QMetaObject.connectSlotsByName(update_word)

    def retranslateUi(self, update_word):
        _translate = QtCore.QCoreApplication.translate
        update_word.setWindowTitle(_translate("update_word", "更新短语"))
        self.apathConfBox_3.setTitle(_translate("update_word", "编码"))
        self.bpathConfBox_2.setTitle(_translate("update_word", "候选词的位置"))
        self.rankCombo.setItemText(0, _translate("update_word", "1"))
        self.rankCombo.setItemText(1, _translate("update_word", "2"))
        self.rankCombo.setItemText(2, _translate("update_word", "3"))
        self.rankCombo.setItemText(3, _translate("update_word", "4"))
        self.rankCombo.setItemText(4, _translate("update_word", "5"))
        self.rankCombo.setItemText(5, _translate("update_word", "6"))
        self.rankCombo.setItemText(6, _translate("update_word", "7"))
        self.cpathConfBox.setTitle(_translate("update_word", "短语"))
        self.yesPbn.setText(_translate("update_word", "确认"))
        self.cancelPbn.setText(_translate("update_word", "取消"))
