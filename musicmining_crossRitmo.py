import matplotlib.pyplot as plt

# and IPython.display for audio output
import IPython.display

# Librosa for audio
import librosa as bro
import numpy as np
import librosa.display 
import os
import shutil
import operator



def cargarSong(a) :
        
    y, sr = bro.load(a)

    
    #---------------------------------------------------------------------
    C= bro.feature.chroma_cqt(y=y,sr=sr)

    hop_length = 512
    plt.figure(figsize=(8, 4))
    onset_env = bro.onset.onset_strength(y, sr=sr,aggregate=np.median)
    tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env,sr=sr)
    times = bro.frames_to_time(np.arange(len(onset_env)),sr=sr, hop_length=hop_length)
    plt.plot(times, bro.util.normalize(onset_env),label='Onset strength')
    plt.vlines(times[beats], 0, 1, alpha=0.5, color='r',linestyle='--', label='Beats')
    plt.legend(frameon=True, framealpha=0.75)

    
    plt.xlim(15, 30)
    plt.gca().xaxis.set_major_formatter(librosa.display.TimeFormatter())
    plt.tight_layout()
    plt.show()
    tempo,beats = bro.beat.beat_track(y=y, sr=sr)
    print("tempo",tempo)
    return tempo

def calcularError(a:int ,b:int):
    print("error:")
    print((a-b)/a)
    return abs((a-b)/a)
    

    
origin = os.getcwd()+'/';
dirsa=[]
i=0
ind=0
ordenar={}
song="09 LUST.ogg"
dirs = os.listdir(origin);
for audio in dirs:
    if(audio.endswith(".ogg")):
        dirsa.append(audio)
print(dirsa)

i=cargarSong(song)

for audio in dirsa:
    ordenar[audio] = calcularError(cargarSong(audio),i)
    
ordenar = sorted(ordenar.items(), key=operator.itemgetter(1), reverse=False)
print(ordenar,"\n")

for song in ordenar:
    ind=ind+1
    print(song)
    newNombre=str(ind)+"__"+ song[0]
    print("nombre nuevo  ", newNombre)
    os.rename(song[0],newNombre)
    