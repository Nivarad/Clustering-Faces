import shutil
from os import listdir, makedirs
from os.path import isfile, join, exists , isdir , islink , dirname
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans , Birch
import os
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from minisom import MiniSom
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA 
from config import *

# cluster_range = range(2, 11)  # for example, from 2 to 10 clusters
def kmeans_clustering(vectors_list,directories_names,num_clusters,files_names):
    
    # # Initialize and fit KMeans
    kmeans = KMeans(n_clusters=num_clusters, random_state=0)
    kmeans.fit(vectors_list)

    # Get the cluster labels
    labels = kmeans.labels_

    # Debug: Verify paths before copying
    for file, label in zip(files_names, labels):
        source_file = join(SRC, file)
        destination_file = join(RESULTS_PATH,SRC,"kmeans", directories_names[label], file)
        if exists(source_file) and exists(dirname(destination_file)):
            shutil.copy(source_file, destination_file)  # Corrected to copy to a full file path
        else:
            print(f"Missing file or directory: {source_file} -> {destination_file}")