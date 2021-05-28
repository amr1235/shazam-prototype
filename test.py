from lib.sound import soundfileUtility


data_1,samplinRate_1 = soundfileUtility.fn_ReadFile("C:\Task4_Shazam\songs\Group18_Song1_Full.mp3")
data_2,samplinRate_2 = soundfileUtility.fn_ReadFile("C:\Task4_Shazam\songs\Group18_Song2_Full.mp3")

weight = 0.5
# print(samplinRate_1,samplinRate_2)
# print(len(data_1) , len(data_2))
total_data = (data_1 * weight) + (data_2 * (1 - weight))
file_handle = sf("test.wav", mode='w' ,samplerate= samplinRate_1
        ,channels=1, subtype=None, endian='FILE', format='WAV', closefd=True)
file_handle.write(total_data)
file_handle.close()
