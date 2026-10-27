"""
Goal 2.1 solution

Classification program to predict audiofiles
"""


#import Libraries
import numpy as np
from pydub import AudioSegment
import os
import glob
import tsfel
import pickle

#configuration
fs=44100        #audio sampling frequency

# Load the saved Orange model
with open('AudioModel.pkcls', 'rb') as model_file:
    model = pickle.load(model_file)

#classify all the wav audio tracks in validation folder
base_audio_folder = os.path.join('AudioDataset', 'validation')

#scan all sub folders
for n in range(10):
    audio_folder = os.path.join(base_audio_folder, str(n))
    wav_files = glob.glob(os.path.join(audio_folder, "*.wav"))

    #scan all wav files
    
    for files in wav_files: 
        features=[]
        # Load MP3 file
        audio = AudioSegment.from_file(files)

        #convert to mono
        audio = audio.set_channels(1)
        
        # Convert to NumPy array
        s = np.array(audio.get_array_of_samples())

        #extract features
        features.append(tsfel.feature_extraction.features.spectral_centroid(s, fs))
        features.append(tsfel.feature_extraction.features.spectral_decrease(s, fs))
        features.append(tsfel.feature_extraction.features.spectral_kurtosis(s, fs))
        features.append(tsfel.feature_extraction.features.spectral_skewness(s, fs))
        features.append(tsfel.feature_extraction.features.spectral_slope(s, fs))
        features.append(tsfel.feature_extraction.features.spectral_spread(s, fs))
        features.append(tsfel.feature_extraction.features.spectral_variation(s, fs))
                
        #print(features)
        prediction = model(features)
        print("Actual:" + str(n) + "\tPreciction:" + str(prediction) + "\twav file: " + files)
