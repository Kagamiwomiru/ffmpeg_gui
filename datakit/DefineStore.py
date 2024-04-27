# 定義
import os
import subprocess
APP_NAME = "FFmpeg GUI"
APP_VERSION = "1.0"
# ffmpegのバージョン情報を取得
result = subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, text=True)
# 出力から最初の行を取得し、スペースで分割
output = result.stdout.split('\n')[0].split()
# バージョン番号が通常3番目に来るので、それを表示
FFMPEG_VERSION = output[2] if len(output) > 2 else "Version not found"
APP_ROOT_PATH = os.getcwd()
AUTHOR = "kagamiwomiru"
AUDIO_CODEC_DICT = {
    "mp3":  "libmp3lame",
    # "aac":  "libfdk_aac", # aacだけうまくいかない
    "ogg":  "libvorbis",
    "flac": "flac",
    "wav":  "pcm_s16le"
}