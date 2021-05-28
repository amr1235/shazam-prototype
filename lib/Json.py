import json

class Json():
    @staticmethod
    def writer(data,filename):
        """Write data into Json file
        Args:
            data (any) : data to be written
            filename (string): filename
            mode (str, optional): "w" for overwriting, "a" for appending. Defaults to "w".
        """        
        if not isinstance(filename,str):
            raise Exception("filename must be string!")

        with open(filename,"w") as file:
            file.write(json.dumps(data,separators=(",",":")))

    @staticmethod
    def reader(filename=None):
        """Read data from Json file

        Args:
            filename (string): filename.

        Returns:
            any: data from file
        """
        if not isinstance(filename,str):
            raise Exception("filename must be string!")
        
        with open(filename,"r") as file:
            data = json.loads(file.read())
        return data

# if __name__ == "__main__":
#     demo_data = [
#         {
#             "one":1,
#             "two":2
#         },
#         {
#             "three":3,
#             "four":4
#         }
#     ]
#     Json.writer("jncjkzcnm","demo.json")
#     data = Json.reader("demo.json")
#     print(data)