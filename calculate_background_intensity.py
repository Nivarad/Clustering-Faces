import os
import numpy as np
from PIL import Image
from rembg import remove

def calculate_average_background_intensity(file_path,output_directory):
    try:
        with Image.open(file_path) as img:
            # Ensure the image is in grayscale mode
            img = img.convert('L')
            
            # Remove background to get the foreground with alpha channel
            img_no_bg = remove(img.convert('RGBA'))
            
            # Convert the images to numpy arrays
            original_array = np.array(img)
            no_bg_array = np.array(img_no_bg)
            
            # Extract the alpha channel from the image with no background
            alpha_channel = no_bg_array[:, :, 3]
            
            # Create a mask where the foreground (non-transparent) is 1 and the background is 0
            mask = np.where(alpha_channel > 0, 1, 0)
            
            # Extract the background using the mask
            background_array = original_array * (1 - mask)
            
            # Calculate the average intensity of the background
            background_pixels = background_array[(background_array > 0) & (background_array < 255)] # Consider only non-zero pixels
            if len(background_pixels) > 0:
                average_intensity = np.mean(background_pixels)
            else:
                average_intensity = 0
            
            background_img = Image.fromarray(background_array)
            background_img = background_img.convert('L')  # Ensure it's in grayscale mode
            
            # Construct the output file path
            base_name = os.path.basename(file_path)
            name, ext = os.path.splitext(base_name)
            output_file_path = os.path.join(output_directory, f"{name}_background{ext}")
            background_img.save(output_file_path)
            print(f'Saved background for {file_path} to {output_file_path}')
            
            return average_intensity
    except Exception as e:
        print(f'Error processing {file_path}: {e}')
        return None

def average_background_intensity_folder(directory,output_path):
    total_intensity = 0
    count = 0
    
    # Walk through all files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.jpg', '.png')):
                file_path = os.path.join(root, file)
                avg_intensity = calculate_average_background_intensity(file_path,output_path)
                if avg_intensity is not None:
                    total_intensity += avg_intensity
                    count += 1
                    print(f'Average background intensity for {file_path}: {avg_intensity}')
    
    # Calculate the overall average intensity for the folder
    if count > 0:
        overall_average_intensity = total_intensity / count
        print(f'Overall average background intensity for folder {directory}: {overall_average_intensity}')
        
        # Add the average intensity to the folder name
        parent_dir, current_folder_name = os.path.split(directory)
        new_folder_name = f"{current_folder_name}_avg_intensity_{overall_average_intensity:.2f}"
        new_folder_path = os.path.join(parent_dir, new_folder_name)
        
        os.rename(directory, new_folder_path)
        print(f'Folder renamed to {new_folder_path}')
    else:
        print(f'No valid images found in folder {directory}')
        overall_average_intensity = None
    
    return overall_average_intensity

# Replace 'your_directory_path' with the path to your folder containing images
folders = [r"som\cluster 1 of 4",r"som\cluster 2 of 4",r"som\cluster 3 of 4",r"som\cluster 4 of 4",r"som\cluster 4 of 4",r"kmeans\cluster 1 of 4",r"kmeans\cluster 2 of 4",r"kmeans\cluster 3 of 4",r"kmeans\cluster 4 of 4",r"birch\cluster 1 of 4",r"birch\cluster 2 of 4",r"birch\cluster 3 of 4",r"birch\cluster 4 of 4"]
for folder in folders:
    average_background_intensity_folder(fr'Results\Gray\{folder}',fr"calc_background/Gray/{folder}")