# For each folder in this directory, run the script.py file in that folder
# This script will read all images in the folder and combine them into a single image
# The combined image will be saved in the same folder as the combined.png file

import os
import sys
import cv2
import numpy as np


def combine_images(folder):
        
    # Get the current directory
    current_dir = folder

    # Get the list of folders in the current directory
    folders = os.listdir(current_dir)

    # Remove any files from the list of folders
    folders = [folder for folder in folders if os.path.isdir(os.path.join(current_dir, folder))]

    # For each folder in the list of folders
    for folder in folders:
        # Get the path to the folder
        folder_path = os.path.join(current_dir, folder)
        
        # Get the list of files in the folder
        files = os.listdir(folder_path)
        
        # Create an empty list to store the images
        images = []

        # For each file in the list of files
        for file in files:
            # Get the path to the file
            file_path = os.path.join(folder_path, file)
            # Read the image
            image = cv2.imread(file_path)
            # Append the image to the list of images
            images.append(image)

        # remove combined.png if it exists
        if os.path.exists(os.path.join(folder_path, 'combined.png')):
            os.remove(os.path.join(folder_path, 'combined.png'))

        # select largest image in width and  and fill other images with white pixels so they have the same width
        max_width = 0
        for image in images:
            height, width, channels = image.shape
            if width > max_width:
                max_width = width
        # Set to index
        i = 0
        for image in images:
            height, width, channels = image.shape
            if width < max_width:
                # Calculate how many pixels to add
                pixels_to_add = max_width - width
                # Calculate how many pixels to add on each side
                pixels_to_add_left = pixels_to_add // 2
                pixels_to_add_right = pixels_to_add - pixels_to_add_left
                # Add the pixels
                image = cv2.copyMakeBorder(image, 0, 0, pixels_to_add_left, pixels_to_add_right, cv2.BORDER_CONSTANT, value=[255,255,255])
                # Replace the image in the list of images
                images[i] = image
            # Increment the index
            i += 1

        # Combine the images into a single image
        combined = np.vstack(images)


        # Save the combined image
        cv2.imwrite(os.path.join(folder_path, 'combined.png'), combined)

        # Print the path to the combined image
        print(os.path.join(folder_path, 'combined.png'))

    # Print a message to the console
    print('Done')

# Create new folder for combined images and move them there, rename them to the name of the folder
def move_images(folder, destination):
    # Get the current directory
    current_dir = folder

    # Ensure the destination folder exists
    if not os.path.exists(destination):
        os.mkdir(destination)

    # Get the list of folders in the current directory
    folders = os.listdir(current_dir)

    # Remove any files from the list of folders
    folders = [folder for folder in folders if os.path.isdir(os.path.join(current_dir, folder))]
    

    # For each folder in the list of folders
    for folder in folders:
        # Get the path to the folder
        folder_path = os.path.join(current_dir, folder)
        
        # Get the list of files in the folder
        files = os.listdir(folder_path)

        # For each file in the list of files
        for file in files:
            # Select only the combined image
            if file != 'combined.png':
                continue
            # Get the path to the file
            file_path = os.path.join(folder_path, file)
            # Move the file to the destination, if file with the same name exists, rewrite it
            os.replace(file_path, os.path.join(destination, folder + '.png'))
            

    # Print a message to the console
    print('Done')
 
combine_images(os.getcwd())
move_images(os.getcwd(), os.path.join(os.getcwd(), 'combined'))





