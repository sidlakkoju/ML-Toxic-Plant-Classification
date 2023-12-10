import os
import shutil
from pathlib import Path

def copy_and_rename_images(src_dir, dest_dir):
    # Create the destination directory if it doesn't exist
    Path(dest_dir).mkdir(parents=True, exist_ok=True)

    # Iterate through all files in the source directory and its subdirectories
    for root, dirs, files in os.walk(src_dir):
        for filename in files:
            # Check if the file is an image (you can extend this check based on your specific requirements)
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                # Generate a unique name for the file in the destination directory
                new_filename = get_unique_filename(dest_dir, filename)
                
                # Construct the full paths for the source and destination files
                src_path = os.path.join(root, filename)
                dest_path = os.path.join(dest_dir, new_filename)

                # Copy the file to the destination directory
                shutil.copy2(src_path, dest_path)

def get_unique_filename(directory, filename):
    # Generate a unique filename by appending a number to the base filename
    base_name, extension = os.path.splitext(filename)
    count = 1
    new_filename = filename
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base_name}_{count}{extension}"
        count += 1
    return new_filename

# Example usage
source_directory = '/Users/siddharthlakkoju/Documents/Semester 5/Machine Learning/Project/iNaturalist/nontoxic_images'
destination_directory = '/Users/siddharthlakkoju/Documents/Semester 5/Machine Learning/Project/virginia_data_reorg/non_toxic'

copy_and_rename_images(source_directory, destination_directory)
