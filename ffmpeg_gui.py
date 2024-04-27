import sys
import os
import glob
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog , QDialog , QMessageBox
from datakit import ValueStore, DefineStore
from helpers.funtions.aboutWindow import AboutWindow
from helpers.funtions import runFFmpeg

# UIファイル
from helpers.ui.AudioConvertWindow import Ui_MainWindow
from helpers.ui.RunningDialog import Ui_Dialog

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=None)
        # UI定義ファイルからUI定義を読み込み
        self.ui = Ui_MainWindow()
        self.ui_dialog = Ui_Dialog()
        self.runningDialog = QDialog(self)
        self.ui.setupUi(self)
        self.ui_dialog.setupUi(self.runningDialog)
        self.ui.methodDropbox.addItems(list(DefineStore.AUDIO_CODEC_DICT.keys()))
        self.ui.methodDropbox.setCurrentText(list(DefineStore.AUDIO_CODEC_DICT.keys())[0])
        self.setCodec()
        
        # マーキースタイル
        self.ui_dialog.progressBar.setMinimum(0)
        self.ui_dialog.progressBar.setMaximum(0)

        # メニューバー
        self.aboutWindow = AboutWindow()
        self.ui.aboutItem.triggered.connect(lambda: self.aboutWindow.showWindow(DefineStore.APP_NAME,
                                                                                DefineStore.APP_VERSION,
                                                                                DefineStore.FFMPEG_VERSION,
                                                                                DefineStore.AUTHOR))

        # signal設定
        self.ui.runButton.clicked.connect(self.runConvert)
        self.ui.selectFileButton.clicked.connect(self.openFileSelectDialog)
        self.ui.inputPathLine.textChanged.connect(self.setInputPath)
        self.ui.outputDirPathLine.textChanged.connect(self.setOutputDirPath)
        self.ui.selectDirButton.clicked.connect(self.saveDirSelectDialog)
        self.ui.methodDropbox.currentTextChanged.connect(self.setCodec)
        self.aboutWindow.dialog.closeButton.clicked.connect(self.aboutWindow.close)

    def runConvert(self):
        '''
        変換を実行
        '''
        self.runningDialog.show()
        if self.ui.typeFileRadio.isChecked():
            '''
            パス指定形式：ファイル
            '''
            output_file_path = f"{os.path.join(ValueStore.output_dir_path, os.path.basename(ValueStore.input_file_path).split('.')[0]) + '.' + ValueStore.codec}"
            result = runFFmpeg.run_ffmpeg(ValueStore.input_file_path, output_file_path, ValueStore.codec)
            if type(result) == str:
                self.handle_error(result)
        elif self.ui.typeDirRadio.isChecked():
            '''
            パス指定形式：ディレクトリ
            '''
            input_dir_path = ValueStore.input_file_path
            for extension in list(DefineStore.AUDIO_CODEC_DICT.keys()):
                for input_file_path in glob.glob(os.path.join(input_dir_path, f"*.{extension}"), recursive=True):
                    print(input_file_path)
                    output_file_path = f"{os.path.join(ValueStore.output_dir_path, os.path.basename(input_file_path).split('.')[0]) + '.' + ValueStore.codec}"
                    result = runFFmpeg.run_ffmpeg(input_file_path, output_file_path, ValueStore.codec)
                    if type(result) == str:
                        self.handle_error(result)
        else:
            raise AssertionError("ラジオボタンが指定されていません")
        self.runningDialog.close()

    def openFileSelectDialog(self):
        '''
        ファイル選択ダイアログを表示し、ファイルパスを返す
        '''
        if self.ui.typeFileRadio.isChecked():
            file, _ = QFileDialog.getOpenFileName(None,"ファイルを選択してください。",ValueStore.input_file_path,"Oggファイル (*.ogg);;Mp3ファイル (*.mp3);;AACファイル (*.aac);;FLACファイル (*.flac)","Oggファイル (*.ogg)")
        elif self.ui.typeDirRadio.isChecked():
            file = QFileDialog.getExistingDirectory(None,"ディレクトリを選択してください。",ValueStore.input_file_path)
        else:
            raise AssertionError("ラジオボタンが指定されていません。")
        

        if file != "":
            # inputPathLineにセット
            self.ui.inputPathLine.setText(file)

    def saveDirSelectDialog(self):
        '''
        保存先ディレクトリダイアログを指定し、保存先ディレクトリパスを返す
        '''
        dir_path = QFileDialog.getExistingDirectory(None,"保存先ディレクトリを選択してください。",ValueStore.output_dir_path)

        if dir_path != "":
            # outputDirPathLineにセット
            self.ui.outputDirPathLine.setText(dir_path)

    
    def setCodec(self):
        '''
        変換方式をセット
        '''
        ValueStore.codec = self.ui.methodDropbox.currentText()

    def setInputPath(self):
        '''
        ファイルパスをセット（LineText)
        '''
        ValueStore.input_file_path = self.ui.inputPathLine.text()
        print(ValueStore.input_file_path)

    def setOutputDirPath(self):
        '''
        保存先ディレクトリをセット
        '''
        ValueStore.output_dir_path = self.ui.outputDirPathLine.text()
        print(ValueStore.output_dir_path)

    def handle_error(self, message):
        # エラーダイアログを作成して表示
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("実行エラー")
        msg.setText("実行失敗")
        msg.setDetailedText(message)
        msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle(DefineStore.APP_NAME)
    window.show()
    sys.exit(app.exec_())