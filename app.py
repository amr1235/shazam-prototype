from librosa import feature
from numpy.lib.function_base import append
from lib.stringDistance import StringDistance
from lib.sound import soundfileUtility
from lib.hash import Hash
import os
import librosa as l
from lib.Json import Json

# iterate over songs paths
songs = []
strings = ["Full","Music","Vocals"]
# groups = [24]
groups = [18,25,24,17,14]
for group_number in groups : 
    count = 1
    for i in range(0,4) :
        arr = []
        for j in strings :
            path = os.path.join("Group" + str(group_number),"Group"+str(group_number)+"_Song"+ str(count)) + "_" + j + ".mp3"
            # print(path)
            # read file
            data,samplingRate = soundfileUtility.fn_ReadFile(path)
            # get spectrogram
            spectrum = soundfileUtility.get_spectrogram(data)
            # hash spectrogram
            specto_hash = Hash.generate_hash_code(spectrum)
            features = soundfileUtility.get_features(data,spectrum,samplingRate)

            feature_1_hash = Hash.generate_hash_code(features[0])
            feature_2_hash = Hash.generate_hash_code(features[1])

            song = {
                "songName" : "Group" + str(group_number) + "_Song" + str(count) + "_" + j,
                "spectrogram_hash" : specto_hash,
                "feature_1" : feature_1_hash,
                "feature_2" : feature_2_hash
            }
            arr.append(song)        
        count += 1
        songs.append(arr)
        print(i)
    print(group_number)

Json.writer(songs,"DB.json")

