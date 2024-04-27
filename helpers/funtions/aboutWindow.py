import sys
sys.path.append("helpers")
from ui.AboutWindow import Ui_Dialog
from PyQt5.QtWidgets import QDialog


class AboutWindow(QDialog):
    def __init__(self):
        super(AboutWindow, self).__init__(parent=None)
        self.dialog = Ui_Dialog()
        self.dialog.setupUi(self)
        
    def showWindow(self, app_name, app_version, ffmpeg_version, author):
        '''
        ウインドウを描画
        '''
        self.setWindowTitle(f"{app_name}について")
        self.dialog.appName.setText(app_name)
        self.dialog.appVersion.setText(app_version)
        self.dialog.ffmpegVersion.setText(ffmpeg_version)
        self.dialog.author.setText(author)
        self.show()
        