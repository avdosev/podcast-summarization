import whisper
import os
from pathlib import Path

model = whisper.load_model("medium")

def transcribe_whisper(filename):
    result = model.transcribe(filename, temperature=0.0)
    return result['text']


def transcribe(audio_file):
    filename = os.path.join('tmp', 'transcribe', *audio_file.replace('mp4', 'txt').split('/')[-2::])

    txt_file = Path(filename)
    if txt_file.exists():
        return txt_file.read_text('utf-8')
    
    txt = transcribe_whisper(audio_file)

    txt_file.parent.resolve().mkdir(parents=True, exist_ok=True)
    txt_file.write_text(txt, 'utf-8')

    return txt
