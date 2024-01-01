import whisper
import os
from pathlib import Path

model = None
def init():
    global model
    if model is not None:
        return
    
    model = whisper.load_model("small")

def transcribe_whisper(filename):
    init()
    result = model.transcribe(filename)
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
