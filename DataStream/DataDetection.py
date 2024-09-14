import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Using PyOD
from pyod.utils.data import generate_data, get_outliers_inliers
from pyod.models.pca import PCA

class MyFunctions:

        def __init__(self, x_train, y_train, df_train):

                self.x_train = x_train
                self.y_train = y_train
                self.df_train= df_train
                self.y_train_pred = None
                self.y_train_scores = None
                self.clf = None

        def pcaModel(self):
                # Create PCA model
                self.clf = PCA()
                # Trains PCA model
                self.clf.fit(self.x_train)

        def savePrediction(self):
                # Store predictions for inlier and outlier in array as 0s and 1s
                self.y_train_pred = self.clf.labels_
                self.y_train_scores = self.clf.decision_scores_

        def anomaliesDetection(self):
                ax = sns.scatterplot(x=0, y=1, hue=self.y_train_scores, data=self.df_train, palette="RdBu_r")

                # Using legends, results look bit varied
                legend_labels = [f"{score:.2f}" for score in
                                 np.unique(self.y_train_scores)]  # Format scores up to 2 decimal places
                ax.legend(title="Anomaly Scores", labels=legend_labels)  # Create legend with title and labels
                plt.title('Anomaly Scores by PCA')
                plt.show()

