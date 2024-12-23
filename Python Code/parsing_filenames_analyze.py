import os
import pandas as pd
import numpy as np
from config import *

def parse_file_name(file_name):
    # Split the file name and extension
    base_name, _ = os.path.splitext(file_name)
    # Split the base name into components
    parts = base_name.split('_')
    try:
        age = int(parts[0])
        gender = int(parts[1])
        race = int(parts[2])
        if age >120 or race >4 or gender >1:
            raise Exception()
        return age, gender, race
    except:
        return None, None, None

# Function to categorize age groups
def categorize_age(age):
    if age < 18:
        return '0-17'
    elif age < 30:
        return '18-29'
    elif age < 50:
        return '30-49'
    elif age < 70:
        return '50-69'
    else:
        return '70+'

# List of directories
folders_results = []
folders_names = []
for src in SRC_LIST:
    for clustering_type in CLUSTERING_TYPES_TO_RUN:
        for index in range(1, 5):
            file_root = os.path.join(RESULTS_PATH, src, clustering_type, f'cluster {index} of 4')
            folders_names.append(file_root)
            folder_data = []
            for file_name in os.listdir(file_root):
                if file_name.endswith(('.jpg', '.png')):
                    age, gender, race = parse_file_name(file_name)
                    if age is not None:
                        folder_data.append({
                            'file_name': file_name,
                            'age': age,
                            'gender': gender,
                            'race': race
                        })
            folders_results.append(folder_data)

for index, folder_results in enumerate(folders_results):
    # Convert list of dictionaries to DataFrame
    df = pd.DataFrame(folder_results)
    
    # Add age group
    df['age_group'] = df['age'].apply(categorize_age)

    # Simplify aggregation: Count occurrences by 'age_group', 'gender', and 'race'
    # First, just count occurrences within age groups
    age_group_counts = df.groupby('age_group').size()

    # Then, count occurrences within gender and race
    gender_counts = df['gender'].value_counts()
    race_counts = df['race'].value_counts()

    print(f'Folder name: {folders_names[index]}')
    print("Age Group Counts:")
    print(age_group_counts)
    print("Gender Counts:")
    print(gender_counts)
    print("Race Counts:")
    print(race_counts)

    # Additional analysis: overall counts by age group, gender, and race
    overall_counts = df.groupby(['gender', 'race']).size().unstack(fill_value=0)
    print("Overall Counts by Gender and Race:")
    print(overall_counts)
    print("\n\n\n")
