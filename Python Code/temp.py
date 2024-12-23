import os
import shutil

def move_contents_to_main_folder(main_folder):
    """
    Move all contents from subfolders of the main folder to the main folder.
    Renames subfolders to a temporary name before moving their contents, then deletes the temp subfolders.

    :param main_folder: Path to the main folder.
    """
    # Get the absolute path of the main folder
    main_folder = os.path.abspath(main_folder)
    
    # Check if the main folder exists
    if not os.path.isdir(main_folder):
        raise FileNotFoundError(f"The folder {main_folder} does not exist.")
    
    # Iterate over each item in the main folder
    for item in os.listdir(main_folder):
        item_path = os.path.join(main_folder, item)
        
        if os.path.isdir(item_path):
            # Create a temporary folder name
            temp_folder_name = f"{item}_temp"
            temp_folder_path = os.path.join(main_folder, temp_folder_name)
            
            # Rename the subfolder to a temporary name
            os.rename(item_path, temp_folder_path)
            
            # Move the contents from the temporary folder to the main folder
            for sub_item in os.listdir(temp_folder_path):
                sub_item_path = os.path.join(temp_folder_path, sub_item)
                dest_path = os.path.join(main_folder, sub_item)
                
                # Handle file conflicts
                if os.path.exists(dest_path):
                    base, extension = os.path.splitext(sub_item)
                    counter = 1
                    new_sub_item = f"{base}_{counter}{extension}"
                    dest_path = os.path.join(main_folder, new_sub_item)
                    while os.path.exists(dest_path):
                        counter += 1
                        new_sub_item = f"{base}_{counter}{extension}"
                        dest_path = os.path.join(main_folder, new_sub_item)
                
                shutil.move(sub_item_path, dest_path)
            
            # Remove the temporary folder after moving contents
            os.rmdir(temp_folder_path)
    
    print(f"All contents have been moved to {main_folder}.")

# Example usage
if __name__ == "__main__":
    # Specify the path to the main folder
    main_folder_path = r"C:\Users\Niv.Arad\Desktop\Project\Results\Gray_Backgroundless\birch\cluster 4 of 4"
    
    # Call the function
    move_contents_to_main_folder(main_folder_path)
