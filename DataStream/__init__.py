from DataStream.DataGeneration import DataClass
from DataStream.DataDetection import MyFunctions

def main():
    data = DataClass()

    data.generateDataBase()
    data.generateDataFrame()
    data.dataVisualization()


    detection = MyFunctions(data.getXTrain(), data.getYTrain(), data.getDFTrain())

    detection.pcaModel()
    detection.savePrediction()
    detection.anomaliesDetection()


if __name__ == '__main__':
    main()
