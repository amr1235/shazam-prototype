import imagehash
from PIL import Image
from imagehash import hex_to_hash


class Hash():
    @staticmethod
    def generate_hash_code(array) :
        arr = Image.fromarray(array)
        hash = imagehash.phash(arr,hash_size=16).__str__()
        return hash

    @staticmethod
    def getHammingDistance(hash1: str, hash2: str) -> int:
        return hex_to_hash(hash1) - hex_to_hash(hash2)

    @staticmethod
    def mapRanges(inputValue: float, inMin: float, inMax: float, outMin: float, outMax: float):
        slope = (outMax-outMin) / (inMax-inMin)
        return outMin + slope*(inputValue-inMin)


# v = Hash.getHammingDistance("c3c3c38383878f8f","89898d8d9cd45757")
# print(abs(1 - Hash.mapRanges(v, 0, 255, 0, 1)) * 100)

