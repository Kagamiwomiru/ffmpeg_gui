# 概要
ffmpegの一部機能をGUIで使えるようにする。

動作確認はmacOS10.14(sonoma)でしか行っていない。

# 環境構築
```
$ python -m venv ffmpeg_gui
$ . ./ffmepg_gui/bin/activate
$ pip install pyqt5
$ brew install ffmpeg
```

# 実行
```
$ . ./ffmepg_gui/bin/activate
$ python /path/to/ffmpeg_gui.py
```
# TODO
- [] ドラッグ&ドロップでファイル入力
- [X] ダイアログでファイル入力
- [X] 音楽ファイル対応
  - aacだけ未対応
- [] UIの改善
- [] 動画ファイルから音声データ抜き出し