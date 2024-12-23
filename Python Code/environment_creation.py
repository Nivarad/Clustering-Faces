import os

# Define the base folder and subfolders
base_folder = 'Results'
subfolders = ['Original', 'Gray', 'Backgroundless', 'Gray_Backgroundless']
subsubfolders = ['kmeans', 'birch', 'som']

# Create the main subfolders and their respective subfolders
for folder in subfolders:
    # Path for the current main folder
    folder_path = os.path.join(base_folder, folder)
    
    # Create the main folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Create the subfolders within the main folder
    for subfolder in subsubfolders:
        subfolder_path = os.path.join(folder_path, subfolder)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)

print("Folder structure created successfully.")