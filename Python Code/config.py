BIRCH_CLUSTERS = 4
KMEANS_CLUSTERS = 4
SOM_CLUSTERS = 4
SOM_WIDTH = 2
SOM_HEIGHT = 2
# Path to the directory containing the grayscale images which are without background
GRAY_PICTURES_PATH = r"./Gray"  # Use forward slashes or raw string literals for paths
ORIGINAL_PICTURES_PATH = r"./Original"
BACKGROUNDLESS_PICTURES_PATH = r"./Backgroundless"
BACK_GRAY_PICTURES_PATH = r"./Gray_Backgroundless"

CLUSTERING_TYPES_TO_RUN = ["kmeans","som","birch"]
SRC = "Original"
SRC_LIST = ["Original","Gray","Backgroundless","Gray_Backgroundless"]
RESULTS_PATH = "Results"