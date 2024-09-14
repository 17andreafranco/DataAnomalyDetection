import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Using PyOD
from pyod.utils.data import generate_data, get_outliers_inliers

class DataClass:

    def __init__(self):
        self.x_train = None
        self.y_train = None
        self.df_train = None

    def getXTrain(self):
        return self.x_train

    def getYTrain(self):
        return self.y_train

    def getDFTrain(self):
        return self.df_train

    def generateDataBase(self):
        # Start by creating a dataset using generate_data() from pyod
        self.x_train, self.y_train = generate_data(train_only=True)
        return self.x_train, self.y_train

    def generateDataFrame(self):
        # Create dataframe from Pandas using the generated data
        self.df_train = pd.DataFrame(self.x_train)
        self.df_train['y'] = self.y_train
        return self.df_train

    def dataVisualization(self):
        # Display first few rows
        self.df_train.head()

        sns.scatterplot(x=0, y=1, hue='y', data=self.df_train, palette="hls", legend="full")
        plt.title('Ground Truth')
        plt.show()