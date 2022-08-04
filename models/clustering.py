import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import pairwise_distances_argmin
from kneed import KneeLocator

class visualize():
    def __init__(self):
        print("init")

    # load dataset
    def dataset(self):
        df = pd.read_csv("data/STUDENT_DATA_CLUSTERING_FULL_RAW.CSV")
        return df

    # generate info statistic
    def info_statistic(self):
        df = self.dataset()

        student = len(df["id"].unique())
        test = len(df["session_type"].unique())
        session = len(df["session"].unique())
        return student, test, session

    # generate scatter
    def cluster_scatter_plot(self):
        df = self.dataset()

        # create dataframe for clustering based on two features values
        df_1 = df.copy()
        df_1 = df_1[["id", "score"]][df["session_type"]=="pretest"] 
        df_1 = df_1.groupby(["id"], sort=True)["score"].mean().reset_index()
        df_2 = df.copy()
        df_2 = df_2[["id", "score"]][df["session_type"]=="posttest"] 
        df_2 = df_2.groupby(["id"], sort=True)["score"].mean().reset_index()
        df_clustering = df_1[["id", "score"]].merge(df_2[["id", "score"]], how="inner", on=["id"])

        # set the data values
        df_clustering_x = df_clustering[["score_x", "score_y"]]
        # standarization the values with array form
        x_array = np.array(df_clustering_x)
        scaler = MinMaxScaler()
        x_scaled = scaler.fit_transform(x_array)
        # define the number of cluster
        wcss=[]
        for i in range(1,20):
            kmeans = KMeans(i)
            kmeans.fit(x_scaled)
            wcss_iter = kmeans.inertia_
            wcss.append(wcss_iter)
        kl = KneeLocator(range(1, 20), wcss, curve="convex", direction="decreasing")
        k = kl.elbow
        # process the clustering with the n cluster
        kmeans = KMeans(n_clusters = k)
        kmeans.fit(x_scaled)
        # load to dataframe
        df_clustering["kluster"] = kmeans.predict(x_scaled)

        return x_scaled, df_clustering

    # generate scatter
    def cluster_distribution_bar_plot(self):
        scaled, df = self.cluster_scatter_plot()

        n = len(df["kluster"].unique())
        df1 = df.loc[df["kluster"]==1]
        df2 = df.loc[df["kluster"]==2]
        df3 = df.loc[df["kluster"]==3]

        return df1, df2, df3
