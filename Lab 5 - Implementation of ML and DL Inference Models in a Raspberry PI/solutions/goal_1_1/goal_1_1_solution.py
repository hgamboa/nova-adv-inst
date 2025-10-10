# -*- coding: utf-8 -*-
"""
Goal 1.1 Solution

Inference program to classify audio files used in Lab2
"""

# imports
#import Libraries
import numpy as np
from pydub import AudioSegment
import os
import glob
import tsfel
import csv
import pickle

#configuration
fs=44100        #audio sampling frequency
t=2             #total time of music sample

# Load the saved Orange model
with open('model_audio.pkcls', 'rb') as model_file:
    model = pickle.load(model_file)
    
# Print or use the model
print(model)

#list all the mp3 in audio_files folder:
audio_folder = "./audio_files/"
mp3_files = glob.glob(audio_folder+"*.mp3")
mp3_files.sort() #by default file list is not sorted.

print('\n'.join('{} -> {}'.format(*k) for k in enumerate(mp3_files)))

#request user to selesct file
audio_n=input('Select the number of the audio file:')

#extract features
features=[]     #list of features

# Load MP3 file
print('Loading' + mp3_files[int(audio_n)])
audio = AudioSegment.from_file(mp3_files[int(audio_n)])

#convert to mono
audio = audio.set_channels(1)

# Convert to NumPy array
signal = np.array(audio.get_array_of_samples())

#extract part of the signal
#this is important speedup the process
n=3
s=signal[n*fs*t:(n+1)*(fs*t)]

#extract features
features.append(tsfel.feature_extraction.features.spectral_centroid(s, fs))
features.append(tsfel.feature_extraction.features.spectral_decrease(s, fs))
features.append(tsfel.feature_extraction.features.spectral_kurtosis(s, fs))
features.append(tsfel.feature_extraction.features.spectral_skewness(s, fs))
features.append(tsfel.feature_extraction.features.spectral_slope(s, fs))
features.append(tsfel.feature_extraction.features.spectral_spread(s, fs))
features.append(tsfel.feature_extraction.features.spectral_variation(s, fs))

print(features)

#classification
prediction = model(features)
print("Predicted class:", prediction)
print("Predicted class verbose:", mp3_files[prediction.astype(float).astype(int)])
