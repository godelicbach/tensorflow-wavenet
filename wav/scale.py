import librosa
import os

wavs = os.listdir(os.getcwd())
wavs.remove('guitar_content_scale.wav')
wavs.remove('scale.py')
target_sr = 16000

import pdb; pdb.set_trace()
for f in wavs:
  w,sr = librosa.core.load(f)
  w = librosa.core.resample(w,sr,target_sr)
  librosa.output.write_wav(f,w,target_sr,True)

