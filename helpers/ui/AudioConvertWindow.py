# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blueprint/AudioConvertWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(703, 358)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.outputPathLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Hiragino Kaku Gothic Pro")
        self.outputPathLabel.setFont(font)
        self.outputPathLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.outputPathLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputPathLabel.setObjectName("outputPathLabel")
        self.gridLayout.addWidget(self.outputPathLabel, 4, 0, 1, 1)
        self.inputPathLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Hiragino Kaku Gothic ProN")
        self.inputPathLabel.setFont(font)
        self.inputPathLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.inputPathLabel.setObjectName("inputPathLabel")
        self.gridLayout.addWidget(self.inputPathLabel, 3, 0, 1, 1)
        self.inputPathLine = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.inputPathLine.setFont(font)
        self.inputPathLine.setToolTip("")
        self.inputPathLine.setObjectName("inputPathLine")
        self.gridLayout.addWidget(self.inputPathLine, 3, 1, 1, 1)
        self.convertMethodLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Hiragino Kaku Gothic Pro")
        self.convertMethodLabel.setFont(font)
        self.convertMethodLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.convertMethodLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.convertMethodLabel.setObjectName("convertMethodLabel")
        self.gridLayout.addWidget(self.convertMethodLabel, 5, 0, 1, 1)
        self.outputDirPathLine = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.outputDirPathLine.setFont(font)
        self.outputDirPathLine.setObjectName("outputDirPathLine")
        self.gridLayout.addWidget(self.outputDirPathLine, 4, 1, 1, 1)
        self.selectFileButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Hiragino Kaku Gothic Pro")
        self.selectFileButton.setFont(font)
        self.selectFileButton.setObjectName("selectFileButton")
        self.gridLayout.addWidget(self.selectFileButton, 3, 2, 1, 1)
        self.selectDirButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Hiragino Kaku Gothic Pro")
        self.selectDirButton.setFont(font)
        self.selectDirButton.setObjectName("selectDirButton")
        self.gridLayout.addWidget(self.selectDirButton, 4, 2, 1, 1)
        self.ffmpeg_icon = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ffmpeg_icon.sizePolicy().hasHeightForWidth())
        self.ffmpeg_icon.setSizePolicy(sizePolicy)
        self.ffmpeg_icon.setText("")
        self.ffmpeg_icon.setPixmap(QtGui.QPixmap("blueprint/../assets/imgs/FFmpeg_Logo_new.png"))
        self.ffmpeg_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.ffmpeg_icon.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.ffmpeg_icon.setObjectName("ffmpeg_icon")
        self.gridLayout.addWidget(self.ffmpeg_icon, 1, 0, 1, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.methodDropbox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.methodDropbox.setFont(font)
        self.methodDropbox.setObjectName("methodDropbox")
        self.horizontalLayout_3.addWidget(self.methodDropbox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Hiragino Kaku Gothic Pro")
        self.runButton.setFont(font)
        self.runButton.setAutoDefault(False)
        self.runButton.setDefault(False)
        self.runButton.setFlat(False)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout_2.addWidget(self.runButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 6, 0, 1, 3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.typeFileRadio = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Hiragino Kaku Gothic Pro")
        self.typeFileRadio.setFont(font)
        self.typeFileRadio.setChecked(True)
        self.typeFileRadio.setObjectName("typeFileRadio")
        self.horizontalLayout_4.addWidget(self.typeFileRadio)
        self.typeDirRadio = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Hiragino Kaku Gothic Pro")
        self.typeDirRadio.setFont(font)
        self.typeDirRadio.setObjectName("typeDirRadio")
        self.horizontalLayout_4.addWidget(self.typeDirRadio)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.inputTypeLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Hiragino Kaku Gothic Pro")
        font.setKerning(True)
        self.inputTypeLabel.setFont(font)
        self.inputTypeLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.inputTypeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.inputTypeLabel.setObjectName("inputTypeLabel")
        self.gridLayout.addWidget(self.inputTypeLabel, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 703, 24))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.aboutItem = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Hiragino Kaku Gothic Pro")
        self.aboutItem.setFont(font)
        self.aboutItem.setObjectName("aboutItem")
        self.menu.addAction(self.aboutItem)
        self.menuBar.addAction(self.menu.menuAction())
        self.outputPathLabel.setBuddy(self.outputDirPathLine)
        self.inputPathLabel.setBuddy(self.inputPathLine)
        self.convertMethodLabel.setBuddy(self.methodDropbox)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.inputPathLine, self.selectFileButton)
        MainWindow.setTabOrder(self.selectFileButton, self.outputDirPathLine)
        MainWindow.setTabOrder(self.outputDirPathLine, self.selectDirButton)
        MainWindow.setTabOrder(self.selectDirButton, self.methodDropbox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.outputPathLabel.setText(_translate("MainWindow", "出力先: "))
        self.inputPathLabel.setText(_translate("MainWindow", "変換元: "))
        self.convertMethodLabel.setText(_translate("MainWindow", "変換形式: "))
        self.selectFileButton.setText(_translate("MainWindow", "変換元を選択"))
        self.selectDirButton.setText(_translate("MainWindow", "出力先を選択"))
        self.ffmpeg_icon.setToolTip(_translate("MainWindow", "<html><head/><body><p>やっほー</p></body></html>"))
        self.methodDropbox.setToolTip(_translate("MainWindow", "<html><head/><body><p>変換する形式を選択します。</p></body></html>"))
        self.runButton.setText(_translate("MainWindow", "変換開始"))
        self.typeFileRadio.setText(_translate("MainWindow", "ファイル"))
        self.typeDirRadio.setText(_translate("MainWindow", "ディレクトリ"))
        self.inputTypeLabel.setText(_translate("MainWindow", "パス指定"))
        self.menu.setTitle(_translate("MainWindow", "メニュー"))
        self.aboutItem.setText(_translate("MainWindow", "このアプリについて"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
