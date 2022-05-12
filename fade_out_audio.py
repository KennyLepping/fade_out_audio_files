import os
from pathlib import Path

from moviepy.audio.fx.all import audio_fadeout
from moviepy.editor import AudioFileClip


def fade_out_audio(dir_path):
    
    # Process audio files with fades to prevent a click at the end
    files = os.listdir(dir_path)
    dir_path = Path(dir_path)
    for file in files:
        audioclip = AudioFileClip(str(dir_path / file))
        faded_out = audio_fadeout(audioclip, 0.01)
        faded_out.write_audiofile(dir_path / file, logger=None)
        print(f'Fade out added to {file}')