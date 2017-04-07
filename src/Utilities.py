import csv

class Utilities(object):
    def __init__(self):
        return None

    def dataReader(self, fileName):
        """Reads in data for NFLModel

        :fileName: name of file to read in
        :returns: data read in

        """
        dataDict = {}
        with open(fileName) as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                dataDict[row[0]] = row[1:]
        return dataDict
