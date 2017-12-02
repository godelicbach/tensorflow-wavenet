import librosa
import os
import numpy as np
import scipy.io.wavfile

target_sr = 16000
hop_length = 512
fmin = librosa.core.note_to_hz('A0')
n_bins=264
bins_per_octave = 36

files = os.listdir(os.getcwd())
wavs = []

for f in files:
    if f.endswith('.wav'):
        wavs.append(f)
i=0
for f in wavs:
    print('{}/{}'.format(i,len(wavs)))
    w,sr = librosa.core.load(f,target_sr)
    w = w[:hop_length*(len(w)/hop_length)] # Cut remainder.
    librosa.output.write_wav(f,w,target_sr,True)

    cqt=np.abs(librosa.core.cqt(y=w,sr=target_sr,
        hop_length=hop_length,fmin=fmin,
        n_bins=n_bins,bins_per_octave=bins_per_octave))
    cqt_log = np.log(cqt+1)
    cqt_log -= cqt_log.std()
    cqt_log /= cqt_log.std()
    cqt_f = os.path.splitext(f)[0]+'.npy'
    np.save(cqt_f,cqt_log)
    i+=1
