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
def birch_clustering(vectors_list,directories_names,files_names, num_clusters):
    # Ensure vectors_list is a 2D array
    vectors_list = vectors_list[0:15000]
    if len(vectors_list) == 0 or not isinstance(vectors_list[0], (list, np.ndarray)):
        raise ValueError("vectors_list should be a list of lists or a 2D numpy array.")

    # Initialize and fit BIRCH
    birch = Birch(n_clusters=num_clusters)
    birch.fit(vectors_list)

    # Get the cluster labels
    labels = birch.labels_

    # Move files to their corresponding cluster directories
    for file, label in zip(files_names, labels):
        source_file = join(SRC, file)
        destination_file = join(RESULTS_PATH,SRC,"birch", directories_names[label],file)

        # Ensure destination directory exists
        if exists(source_file) and exists(dirname(destination_file)):
            shutil.copy(source_file, destination_file)
        else:
            print(f"Missing file or directory: {source_file} -> {destination_file}")


def birch_clustering_incremental(vectors_list,files_names, directories_names, num_clusters, batch_size=3000):
    # Initialize BIRCH
    birch = Birch(n_clusters=num_clusters)

    # Fit BIRCH incrementally
    for i in range(0, len(files_names), batch_size):
        batch = vectors_list[i:i+batch_size]
        birch.partial_fit(batch)
    labels = birch.predict(vectors_list)

    # Move files to their corresponding cluster directories
    for file, label in zip(files_names, labels):
        source_file = join(SRC, file)
        destination_dir = join(RESULTS_PATH,SRC, "birch", directories_names[label],file)
        destination_file = join(destination_dir, file)

        # Ensure destination directory exists
        if not exists(destination_dir):
            os.makedirs(destination_dir)

        if exists(source_file):
            shutil.copy(source_file, destination_file)
        else:
            print(f"Missing file: {source_file}")