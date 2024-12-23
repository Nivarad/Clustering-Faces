import shutil
from os import listdir, makedirs
from os.path import isfile, join, exists , isdir , islink , dirname
from utilities import *
from kmeans import *
from config import *
from som import *
from birch import *


directories_names_all = {}

for type in CLUSTERING_TYPES_TO_RUN:
    direcotries_names_by_type_and_photo_src = directories_name__by_type_and_src(type,SRC)
    directories_names_all[type] = direcotries_names_by_type_and_photo_src
    for directory_name in direcotries_names_by_type_and_photo_src:
        folder_name=create_directory_if_not_exist(directory_name,type,SRC)
        # clean_directory_content(folder_name)

# Get all file names in the directory
files_names = [f for f in listdir(SRC) if isfile(join(SRC, f))]



vectors_list = get_vectors_for_pictures(files_names)
# scaler = StandardScaler()
# vectors_list = scaler.fit_transform(vectors_list)
# n_components = 800
# pca = PCA(n_components=n_components)
# vectors_list = pca.fit_transform(vectors_list)

for type in CLUSTERING_TYPES_TO_RUN:
    
    match type.upper():
        case 'KMEANS':
            kmeans_clustering(vectors_list,directories_names_all[type],num_clusters=KMEANS_CLUSTERS,files_names=files_names)
        case 'SOM':
            som_clustering(vectors_list,directories_names_all[type],som_width=SOM_WIDTH,som_height=SOM_HEIGHT,files_names=files_names)
        case "BIRCH":

            birch_clustering(vectors_list=vectors_list,directories_names=directories_names_all[type],num_clusters=BIRCH_CLUSTERS,files_names=files_names)
    
    print(f'{type} clustering finished')