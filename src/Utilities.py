import csv

class DataReader(object):
    def __init__(self):
        return None

    def statReader(self, fileName):
        """Reads in stats data for NFLModel

        :fileName: name of file to read in
        :returns: data read in

        """
        dataDict = {}
        with open(fileName) as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                dataDict[row[0]] = map(float, row[1:])
        return dataDict

    def playReader(self, fileName):
        """Reads in play data for NFLModel

        :fileName: name of file to read in
        :returns: data read in

        """
        dataDict = {}
        with open(fileName) as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                if row[0] in dataDict.keys():
                    dataDict[row[0]].append(float(row[2]))
                else:
                    dataDict[row[0]] = [float(row[2])]
        return dataDict
