from librosa.core import spectrum
from numpy.core.numeric import full
from lib.sound import soundfileUtility
from lib.hash import Hash
from lib.stringDistance import StringDistance
from lib.Json import Json

class Compare() :

    def __init__(self,songPath) -> None:
        data,samplingRate = soundfileUtility.fn_ReadFile(songPath)
        # get spectrogram
        spect = soundfileUtility.get_spectrogram(data)
        # hash spectrogram
        self.spectrogram_hash = Hash.generate_hash_code(spect)
        features = soundfileUtility.get_features(data,spect,samplingRate)
        self.feature_1 = Hash.generate_hash_code(features[0])
        self.feature_2 = Hash.generate_hash_code(features[1])
        # self.feature_3 = Hash.generate_hash_code(features[2])

    def get_similarty_indices(self) :
        songs_names = []
        songs_indices = [] 
        songs = self.__get_songs()
        #  loop throw Database
        for song in songs :
            count = 0
            for component in song :
                sim_arr = []
                for key in component : 
                    if (key == "songName") : continue
                    # compare hash of spectrogram
                    sim = StringDistance(component[key],getattr(self,key)).get_similarity_index()
                    sim_arr.append(sim)
                # get av 
                av = sum(sim_arr) / len(sim_arr)
                songs_names.append((song[count]["songName"]))
                songs_indices.append(av)
                count += 1
        sorted_sim = sorted(zip(songs_names,songs_indices),key = lambda x : x[1],reverse=True)
        return sorted_sim

    def __get_songs(self) :
        return Json.reader("DB.json")

