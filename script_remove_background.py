import os
from PIL import Image
from rembg import remove

def remove_background(directory):
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # Create a "Backgroundless" folder in the same directory as the script
    backgroundless_dir = os.path.join(script_dir, 'Gray_Backgroundless')
    os.makedirs(backgroundless_dir, exist_ok=True)
    
    # Walk through all files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.jpg', '.png')):
                # Construct full file path
                file_path = os.path.join(root, file)
                
                # Open an image file
                try:
                    with Image.open(file_path) as img:
                        # Remove background
                        img_no_bg = remove(img)
                        img_no_bg = img_no_bg.convert("RGB")
                        
                        # Split the file name and extension
                        file_name, file_extension = os.path.splitext(file)
                        
                        # Create new file name for backgroundless image
                        new_file_name = f"{file_name}_backgroundless{file_extension}"
                        new_file_path = os.path.join(backgroundless_dir, new_file_name)
                        
                        # Save the backgroundless image with the new file name
                        img_no_bg.save(new_file_path)
                    print(f'Removed background from {file_path} and saved as {new_file_path}')
                except Exception as e: 
                    print(f'Error processing {file_path}: {e}')

# Replace 'your_directory_path' with the path to your folder containing images
remove_background('Gray')
