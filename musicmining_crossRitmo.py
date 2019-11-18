# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:54:07 2019

@author: arval
"""
import matplotlib.pyplot as plt# Is a libreri to put the info in a graph
import librosa as bro#Music manipulation librery
import numpy as np
import librosa.display #Librery to management of data to pass by to ptl lib
#filename: file that sabe a sample of music
filename = bro.util.example_audio_file()
filess = bro.util.find_files('~/Sampler', ext='mp3')# por que no me corre esta wea ??


print(len(filess))
# 2. Load the audio as a waveform `y`

#    Store the sampling rate as `sr`
y, sr = bro.load(filename)
print(sr)
# 3. Run the default beat tracker
tempo, beat_frames = bro.beat.beat_track(y=y, sr=sr)

plt.figure(figsize=(25, 25))

CQT= bro.amplitude_to_db(np.abs(bro.cqt(y,sr=sr)), ref=np.max)
plt.subplot(4, 2, 3)
bro.display.specshow(CQT, y_axis='cqt_note')
plt.colorbar(format='%+2.0f dB')
plt.title('Constant-Q power spectrogram (note)')

#---------------------------------------------------------------------
C= bro.feature.chroma_cqt(y=y,sr=sr)
plt.subplot(4,2,5)
bro.display.specshow(CQT, y_axis='chroma')

plt.colorbar()
plt.title("chromagram")