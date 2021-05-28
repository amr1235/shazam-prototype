from lib.sound import soundfileUtility
import os
class Mix() :
    def __init__(self,song_1_path = None,song_2_path = None) -> None :
        self.data_1,self.samplinRate_1 = soundfileUtility.fn_ReadFile(song_1_path)
        self.data_2,self.samplinRate_2 = soundfileUtility.fn_ReadFile(song_2_path)

    def mix(self,weight) :
        total_data = (self.data_1 * weight) + (self.data_2 * (1 - weight))
        soundfileUtility.fn_CreateSoundFile(total_data,self.samplinRate_1,"mixedSong.wav")
        return os.path.abspath("mixedSong.wav")



