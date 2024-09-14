import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.core.interchange.dataframe_protocol import DataFrame

# Using PyOD
from pyod.utils.data import generate_data, get_outliers_inliers
from pyod.models.pca import PCA
from pyod.utils.data import evaluate_print
from pyod.utils.example import visualize

class MyFunctions:

        def __init__(self):
                self.self = self
                self.x_trainy = None
                self.y_train = None
                self.df_train= None

        def dataBase(self):
                # Start by creating a dataset using generate_data() from pyod
                self.x_trainy, self.y_train = generate_data(train_only=True)

        def dataFrame(self):
                # Create dataframe from Pandas using the generated data
                df_train = pd.DataFrame(self.x_trainy)
                self.df_train['y'] = self.y_train

        # Display first few rows
                self.df_train.head()

                sns.scatterplot(x=0, y=1, hue='y', data=self.df_train, palette="hls", legend="full")
                plt.title('Ground Truth')
