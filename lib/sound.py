from librosa.feature.spectral import mfcc
from numpy.lib.arraypad import pad
from scipy import signal
import soundfile as sff
from soundfile import SoundFile as sf
import numpy as np
import winsound
import os
import librosa
import matplotlib.pyplot as plt


class soundfileUtility():
    # read wav file
    # returns sampling rate and sound data 
    @staticmethod
    def fn_ReadFile(file_name):
        data, samplerate = librosa.load(file_name,duration = 60)
        # get first min
        return data , samplerate
    @staticmethod
    def get_spectrogram(data) : 
        X = librosa.stft(data)
        Xdb = librosa.power_to_db(abs(X) ** 2)
        # frequancyArr,timeArr,sxx = signal.spectrogram(data, fs=samplerate, window='hann')
        return Xdb
    @staticmethod
    def get_features(data,spectrum,samplingRate) :
        feature_1 = librosa.feature.melspectrogram(y=data, S=spectrum, sr=samplingRate, window="hann")
        feature_2 = librosa.feature.mfcc(y=data.astype('float64'), sr=samplingRate)
        return [feature_1,feature_2]

    @staticmethod
    def fn_CreateSoundFile(arr_of_realNum, samplrate,fileName):
        file_handle = sf(fileName, mode='w' ,samplerate= samplrate
        ,channels=1, subtype=None, endian='FILE', format='WAV', closefd=True)
        file_handle.write(arr_of_realNum)
        file_handle.close()

    @staticmethod
    def fn_PlaySoundFile(file_name="Tdfgjdli.wav"):
        winsound.PlaySound(file_name, winsound.SND_FILENAME)
        os.remove(file_name)