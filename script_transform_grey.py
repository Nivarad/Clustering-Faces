import os
from PIL import Image

def convert_to_grayscale(directory):
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.realpath(__file__))
    # Create a "Gray" folder in the same directory as the script
    gray_dir = os.path.join(script_dir, 'Gray')
    os.makedirs(gray_dir, exist_ok=True)
    
    # Walk through all files in the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.jpg', '.png')):
                # Construct full file path
                file_path = os.path.join(root, file)
                
                # Open an image file
                try:
                    with Image.open(file_path) as img:
                        # Convert image to grayscale
                        grayscale_img = img.convert('L')
                        
                        # Split the file name and extension
                        file_name, file_extension = os.path.splitext(file)
                        
                        # Create new file name with "_gray" appended
                        new_file_name = f"{file_name}_gray{file_extension}"
                        new_file_path = os.path.join(gray_dir, new_file_name)
                        
                        # Save the grayscale image with the new file name
                        grayscale_img.save(new_file_path)
                    print(f'Converted {file_path} to grayscale and saved as {new_file_path}')
                except Exception as e:
                    print(f'Error processing {file_path}: {e}')
                    os.remove(file_path)
                    print(f'Deleted {file_path} due to the error')

# Replace 'your_directory_path' with the path to your folder containing images
convert_to_grayscale('Original')
