import os
from pathlib import Path

from moviepy.audio.fx.all import audio_fadeout
from moviepy.editor import AudioFileClip


# Fade out end of audio files preventing clicks at the end of a file
def fade_out_audio(dir_path):
    
    files = os.listdir(dir_path)
    dir_path = Path(dir_path)
    for file in files:
        # Process audio file with fades to prevent a click at the end
        audioclip = AudioFileClip(str(dir_path / file))
        faded_out = audio_fadeout(audioclip, 0.01)
        faded_out.write_audiofile(dir_path / file, logger=None)
        print(f'Fade out added to {file}')