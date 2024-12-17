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
def som_clustering(vectors_list,directories_names,som_width,som_height,files_names):
    
    ######################################
    ########MinSom####################

    # Parameters
    som_width = som_width
    som_height = som_height
    feature_count = len(vectors_list[0])

    # Initialize and train the SOM
    som = MiniSom(som_width, som_height, feature_count, sigma=0.5, learning_rate=0.5)  # Adjusted sigma as well
    som.random_weights_init(vectors_list)
    som.train_random(vectors_list, 1000)

    # Map each image vector to its closest neuron in the SOM grid
    winning_nodes = np.array([som.winner(v) for v in vectors_list])

    # Assuming a simple 2x1 grid, classify each vector into one of two clusters based on the winning node
    clusters = [node[0] * som_height + node[1] for node in winning_nodes]  # Maps (x, y) to a unique cluster label


    # Move files to their corresponding cluster directories
    for file, label in zip(files_names, clusters):
        source_file = join(SRC, file)
        destination_file = join(RESULTS_PATH,SRC, "som",directories_names[label], file)
        if exists(source_file) and exists(dirname(destination_file)):
            shutil.copy(source_file, destination_file)
        else:
            print(f"Missing file or directory: {source_file} -> {destination_file}")