import subprocess
from datakit import DefineStore
def run_ffmpeg(input_file_path, output_file_path, codec):
    args = ["ffmpeg", "-i", input_file_path, "-ar", "44100", "-ac", "2", "-acodec", DefineStore.AUDIO_CODEC_DICT[codec], "-f", codec, output_file_path]
    if codec == "aac":
        '''
        音質低下を下げる為のオプションを追加
        '''
        args = ["ffmpeg", "-i", input_file_path, "-ar", "44100", "-ac", "2", "-acodec", DefineStore.AUDIO_CODEC_DICT[codec], "-profile:a", "aac_he", "-afterburner", "1", "-f", codec, output_file_path]

    try:
        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            raise Exception(f"FFmpeg failed: {result.stderr}")
        return 0
    except Exception as e:
        return str(e)