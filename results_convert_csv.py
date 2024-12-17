import os
import csv
import pandas as pd
from config import *

def create_csv_from_images(folder_path, output_xlsx='output.csv'):
    # Define a list to store the extracted rows
    data = []

    # Supported image extensions
    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}

    # Iterate over each file in the given directory
    for filename in os.listdir(folder_path):
        # Get the file's absolute path
        file_path = os.path.join(folder_path, filename)

        # Check if it's a file and is an image (based on extension)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            if ext.lower() in image_extensions:
                # Remove extension from filename to extract details
                name_without_ext = os.path.splitext(filename)[0]

                # Split by underscore to get Age, Gender, Ethnicity
                parts = name_without_ext.split('_')
                if len(parts) >= 4:
                    age, gender, ethnicity , *garbage = parts
                    data.append([age, gender, ethnicity])
                else:
                    # If the format is not correct, you may choose to skip or print a warning
                    print(f"Warning: Filename '{filename}' does not match the format AGE_GENDER_ETHNICITY.")
    
    # Write the results to a CSV file
    df = pd.DataFrame(data, columns=['Age', 'Gender', 'Ethnicity'])

    # Write the DataFrame to an Excel file
    df.to_excel(output_xlsx, index=False, engine = 'openpyxl')
    print(f"Excel file '{output_xlsx}' created successfully.")

# Example usage:
# folder_path = "path/to/your/folder"
# create_csv_from_images(folder_path)


folders_results = []
results_folders_path = []
for src in SRC_LIST:
    for clustering_type in CLUSTERING_TYPES_TO_RUN:
        for index in range(1, 5):
            file_root = os.path.join(RESULTS_PATH, src, clustering_type, f'cluster {index} of 4')
            results_folders_path.append(file_root)


for index, path in enumerate(results_folders_path):
    create_csv_from_images(path , os.path.join("excels",(str(path).replace("\\","_")+".xlsx")))
    # Convert list of dictionaries to DataFrame
