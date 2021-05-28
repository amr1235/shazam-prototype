# algo 
# first split strings into words 
# compute the chars frequancy (string vector)
# compute dot product of two vectors (two strings)
import numpy as np
class StringDistance() :
    def __init__(self,string_1 : str,string_2 : str) -> None:
        self.string_1 = string_1 
        self.string_2 = string_2
        if string_1 == "" or string_2 == "" : 
            raise Exception("strings are empty !")

    def get_similarity_index(self) :
        vectors = self.__get_string_vectors()
        # compute dot product
        dot_product = np.dot(vectors[0],vectors[1])
        vector_1_magnitude = self.__vector_magnitude(vectors[0])
        vector_2_magnitude = self.__vector_magnitude(vectors[1])
        similarty_index = (dot_product) / (vector_1_magnitude * vector_2_magnitude)
        return similarty_index
        
    
    # count chars in string (get strings veectors)
    def __get_string_vectors(self) :
        vector_1 = dict()
        vector_2 = dict()

        for chr in self.string_1 : 
            vector_1[chr] = vector_1.get(chr,0) + 1

        for chr in self.string_2 : 
            vector_2[chr] = vector_2.get(chr,0) + 1 
        # fill common chars with zero frequancies
        for key in vector_1 : 
            value = vector_2.get(key,-1)
            if value == -1 : 
                vector_2[key] = 0

        for key in vector_2 : 
            value = vector_1.get(key,-1)
            if value == -1 :
                vector_1[key] = 0

        # sort dic by keys
        vector_1_items = sorted(vector_1.items())
        vector_2_items = sorted(vector_2.items())

        # get freqs
        v_1 = [item[1] for item in vector_1_items]
        v_2 = [item[1] for item in vector_2_items]

        return (v_1,v_2)

    
    def __vector_magnitude(self,vector) :
        power =  np.array(vector) ** 2
        s = sum(list(power))
        return np.sqrt(s)
    

# s = StringDistance("c3c3c38383878f8f","89898d8d9cd45757").get_similarity_index()
# print(s)
