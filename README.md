# Face Clustering Research

### Mentor: Dr. Sharon Yalov-Handzel

---

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Preprocessing](#preprocessing)
- [Clustering Algorithms](#clustering-algorithms)
- [Experiments](#experiments)
- [Results](#results)
- [Python Scripts](#python-scripts)
- [Conclusion](#conclusion)
- [References](#references)

---

## Introduction
As part of my final project for my computer science degree, I worked as a research assistant to Dr. Sharon Yalov-Handzel. My task was to conduct various experiments on the UTKFace dataset using different clustering algorithms including K-Means, BIRCH, and SOM. This project explores the application and performance of these algorithms on facial images to understand how they cluster data based on age, gender, and race.

---

## Dataset
The UTKFace dataset consists of approximately 24,000 photos, each labeled in the format: `age_gender_race_date&time.jpg`. The dataset includes diverse facial images varying in age, gender, and race.

---

## Preprocessing
To prepare the data for clustering, the following preprocessing steps were performed:

1. **Resizing:** All images were resized to a fixed size.
2. **Grayscaling:** Images were converted to grayscale.
3. **Background Removal:** Backgrounds were removed from the images.
4. **Vectorization:** Images were converted into vectors for clustering.

Four different datasets were created from the original dataset:
- Original Photos
- Grayscaled Photos
- Backgroundless Photos
- Grayscaled & Backgroundless Photos

---

## Clustering Algorithms
The following clustering algorithms were utilized in this research:

#### K-Means
A centroid-based algorithm that divides the dataset into K distinct, non-overlapping clusters based on similarity or distance measures.

#### BIRCH
(Balanced Iterative Reducing and Clustering using Hierarchies) A hierarchical clustering algorithm designed to handle large datasets efficiently by creating a compact summary of the data.

#### SOM
(Self-Organizing Maps) An unsupervised artificial neural network used for clustering and dimensionality reduction, mapping high-dimensional data onto a lower-dimensional grid.

---

## Experiments
Each of the clustering algorithms was applied to the four different datasets created:

- **Original Photos**
- **Grayscaled Photos**
- **Backgroundless Photos**
- **Grayscaled & Backgroundless Photos**

Due to the large size of the original dataset, not all algorithms could complete learning on it, especially when requiring more than 32GB of RAM. The BIRCH algorithm, being memory-intensive, was applied to a subset of 10,000 photos.

---
## Python Scripts
This project includes several Python scripts for preprocessing, clustering, and managing the environment:

#### Preprocessing Scripts
- **script_transform_gray.py:** Converts images to grayscale.
- **script_remove_background.py:** Removes the background from images.
- **script_resize_photos.py:** Resizes images to a fixed size.
- **utilities.py:** Contains utility functions for vectorizing images.

#### Environment Setup
- **environment_creation.py:** Creates the directory structure for storing the results of the clustering algorithms.

#### Clustering Algorithms
- **kmeans.py:** Implementation of the K-Means clustering algorithm.
- **som.py:** Implementation of the Self-Organizing Maps (SOM) clustering algorithm.
- **birch.py:** Implementation of the BIRCH clustering algorithm.


#### Configuration
- **config.py:** Contains configuration settings for running the clustering algorithms. Below are the key configuration parameters:
  ```python BIRCH_CLUSTERS = 4
  KMEANS_CLUSTERS = 4
  SOM_CLUSTERS = 4
  SOM_WIDTH = 2
  SOM_HEIGHT = 2
  CLUSTERING_TYPES_TO_RUN = ["birch"] 
  DATASET_SRC = "Original"
  RESULTS_PATH = "Results"

---

## References
For more detailed information, please refer to the academic paper "A Comparative Study of Clustering Approaches: Algorithmic Performance Influential Factors and Correspondence to Human Facial Categorization" by Dr. Sharon Yalov-Handzel and collaborators.

---

This README provides a comprehensive overview of the Face Clustering Research project, detailing the methodology, experiments, and findings. For more detailed code and results, please refer to the [repository](https://github.com/yourusername/face-clustering-research).
