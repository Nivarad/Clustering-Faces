import os
from PIL import Image

def resize_images(directory, size=(200, 200)):
    # Walk through all files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.jpg', '.png')):
                # Construct full file path
                file_path = os.path.join(root, file)
                
                try:
                    # Open an image file
                    with Image.open(file_path) as img:
                        # Resize image
                        resized_img = img.resize(size)
                        resized_img = resized_img.convert("RGB")
                        
                        # Save the resized image, overwriting the original file
                        resized_img.save(file_path)
                    print(f'Resized {file_path} to {size[0]}x{size[1]} pixels')
                except Exception as e: 
                    print(f'Error processing {file_path}: {e}')
                    os.remove(file_path)
                    print(f'Deleted {file_path} due to the error')
                    

# Replace 'your_directory_path' with the path to your folder containing images
resize_images('Original')