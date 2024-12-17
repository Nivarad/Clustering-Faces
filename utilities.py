
import shutil
from os import listdir, makedirs
from os.path import isfile, join, exists , isdir , islink , dirname
import os
from config import *
from PIL import Image
import numpy as np
def directories_name__by_type_and_src(clustering_type,src):
    directories_name = []
    clustering_type = str(clustering_type).upper()
    
    type_range = 0
    
    match clustering_type:
        case "SOM":
            type_range = SOM_WIDTH * SOM_HEIGHT
        case "BIRCH":
            type_range = BIRCH_CLUSTERS
        case "KMEANS":
            type_range = KMEANS_CLUSTERS
    
    for i in range(1,type_range+1):
        name = f"cluster {str(i)} of {str(type_range)}"
        directories_name.append(name)
    
    return directories_name

def create_directory_if_not_exist(direcotry_name,type,src):
    dir_path = join(os.getcwd(), RESULTS_PATH, src,type,str(direcotry_name))
    is_exist = exists(dir_path)
    if not is_exist:
        os.mkdir(dir_path)
    return dir_path
        
def clean_directory_content(direcotry_name) : 
    dir_path = join(os.getcwd(), 'Pictures and Results', 'GrayPictures',"Clustering Results",str(direcotry_name))
    for filename in os.listdir(dir_path):
        file_path = join(dir_path, filename)
        try:
            if isfile(file_path) or islink(file_path):
                os.unlink(file_path)
            elif isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def get_vectors_for_pictures(files):
    
    vectors_list = []
    for counter, file in enumerate(files):
        if counter % 400 == 0:
            print(counter)
            
        try:
            # Load the image
            image = Image.open(join(SRC, file))
            
            # Ensure the image is in RGB or Grayscale mode
            if image.mode not in ['L', 'RGB']:
                image = image.convert('RGB')
            
            # Check image size and convert to grayscale
            if image.size != (200, 200):
                print(f"Warning: Image {file} is not 200x200 pixels. Resizing...")
                image = image.resize((200, 200), resample=Image.LANCZOS)
            
            
            
            # Convert image to numpy array and flatten it
            image_array = np.array(image,dtype = np.float16)
            
            if image_array.shape[0]!= 200 and image_array.shape[1]!=200:
                raise ValueError(f"Unexpected image array shape: {image_array.shape}")
            
            image_vector = image_array.flatten()
            
            vectors_list.append(image_vector)
        
        except Exception as e:
            print(f"Error processing file {file}: {e}")
            continue
        
    vectors_list = np.array(vectors_list)
    return vectors_list

def get_vectors_for_picture(file):
    vectors_list = []
    image_gray = Image.open(join(PICTURES_PATH, file))
    image_array = np.array(image_gray)
    image_vector = image_array.flatten()
    vectors_list.append(image_vector)
        
    vectors_list = np.array(vectors_list, dtype=np.float32)
    return vectors_list
