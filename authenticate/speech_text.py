#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import wave
import subprocess
import json
from rating.settings import BASE_DIR


def speech_to_text():
    SetLogLevel(0)

    if not os.path.exists("model"):
        print(
            "Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
        exit(1)

    sample_rate = 16000
    model = Model("model")
    rec = KaldiRecognizer(model, sample_rate)

    AUDIO_BOOKS = os.path.join(BASE_DIR, 'audiobooks')
    # get the first file
    filename_with_extension = os.listdir(AUDIO_BOOKS)[0]
    filename, extension = filename_with_extension.split('.')
    filename_with_json = filename + '.json'

    FILE_PATH = os.path.join(AUDIO_BOOKS, filename_with_json)
    f = open(FILE_PATH)
    data = json.load(f)
    audible_key = data["key"]
    audible_iv = data["iv"]

    FILE_PATH_EXT = os.path.join(AUDIO_BOOKS, filename_with_extension)
    print(FILE_PATH_EXT)
    process = subprocess.Popen(
        ['ffmpeg', '-audible_key', audible_key, '-audible_iv', audible_iv, '-loglevel', 'quiet', '-i',
         FILE_PATH_EXT,
         # sys.argv[1],
         '-ar', str(sample_rate), '-ac', '1', '-f', 's16le', '-'],
        stdout=subprocess.PIPE)
    text = ""
    while True:
        data = process.stdout.read(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            # print(rec.Result())
            res = json.loads(rec.Result())
            print(res['text'])
            text = text + " " + str(res['text'])
        # else:
        #     print(rec.PartialResult())

    # print(rec.FinalResult())

    res = json.loads(rec.FinalResult())
    text = text + " " + str(res['text'])

    print(text)
    return text
