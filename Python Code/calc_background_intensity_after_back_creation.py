import os
import numpy as np
from PIL import Image
from rembg import remove


def calculate_average_background_intensity(file_path):
    try:
        with Image.open(file_path) as img:
            # Ensure the image is in grayscale mode
            img = img.convert('L')
            
            # Convert the images to numpy arrays
            original_array = np.array(img)
            
            # Calculate the average intensity of the background
            background_pixels = original_array[(original_array > 0) & (original_array < 255)] # Consider only non-zero pixels
            if len(background_pixels) > 0:
                average_intensity = np.mean(background_pixels)
            else:
                average_intensity = 0
            
            return average_intensity
    except Exception as e:
        print(f'Error processing {file_path}: {e}')
        return None

def average_background_intensity_folder(directory, folders_results):
    total_intensity = 0
    count = 0
    
    # Walk through all files in the directory
    for root, dirs, files in os.walk(directory):
        folder = []
        for file in files:
            if file.lower().endswith(('.jpg', '.png')):
                file_path = os.path.join(root, file)
                
                # Calculate the average background intensity
                avg_intensity = calculate_average_background_intensity(file_path)
                
                if avg_intensity is not None:
                    folder.append(avg_intensity)
                    
                    # Split file name and extension
                    # file_name, ext = os.path.splitext(file)
                    
                    # # Construct new file path with average intensity
                    # new_file_name = f"{file_name}_{int(avg_intensity)}{ext}"
                    # new_file_path = os.path.join(root, new_file_name)
                    
                    # try:
                    #     # Rename the file
                    #     os.rename(file_path, new_file_path)
                    #     print(f"File renamed from {file_path} to {new_file_path}")
                    # except FileNotFoundError:
                    #     print(f"File not found: {file_path}")
                    # except PermissionError:
                    #     print(f"Permission denied: {file_path}")
                    # except Exception as e:
                    #     print(f"Error renaming file {file_path}: {e}")
                    
        folders_results.append(folder)

    
    # Calculate the overall average intensity for the folder    

def calculate_statistics(data):
    statistics = []
    for sublist in data:
        array = np.array(sublist)
        mean = np.average(array)
        median = np.median(array)
        std_dev = np.std(array)
        variance = np.var(array)
        stats = {
            'mean': mean,
            'median': median,
            'std_dev': std_dev,
            'variance': variance
        }
        statistics.append(stats)
    return statistics  

folders_names = [r"som\cluster 1 of 4",r"som\cluster 2 of 4",r"som\cluster 3 of 4",r"som\cluster 4 of 4",r"som\cluster 4 of 4",r"kmeans\cluster 1 of 4",r"kmeans\cluster 2 of 4",r"kmeans\cluster 3 of 4",r"kmeans\cluster 4 of 4",r"birch\cluster 1 of 4",r"birch\cluster 2 of 4",r"birch\cluster 3 of 4",r"birch\cluster 4 of 4"]
# folders_names = [r"birch\cluster 1 of 4",r"birch\cluster 2 of 4",r"birch\cluster 3 of 4",r"birch\cluster 4 of 4"]

folders_results = []

for folder in folders_names:
    # average_background_intensity_folder(fr'Results\Gray_Backgroundless\{folder}',folders_results)
    # average_background_intensity_folder(fr'Results\Gray\{folder}',folders_results)
    average_background_intensity_folder(fr'Results\Backgroundless\{folder}',folders_results)
    # average_background_intensity_folder(fr'Results\Original\{folder}',folders_results)

stats = calculate_statistics(folders_results)
for i, stat in enumerate(stats):
    print(f"Folder name : {folders_names[i]}")
    print(f"  Mean: {stat['mean']}")
    print(f"  Median: {stat['median']}")
    print(f"  Standard Deviation: {stat['std_dev']}")
    print(f"  Variance: {stat['variance']}")
    print("\n\n\n\n")

