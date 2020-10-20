'''
Delete duplicate files

Forked from: https://github.com/matthewrenze/rename-images
Not used for the same purpose but I used it as the base 

Usage: python.exe Rename.py input-folder
  - input-folder = the directory containing the image files to be renamed

Example: python Deletion.py C:\Photos

Behavior:  
 - Given a filed named "foobar.jpg" and "foobar (1).jpg"   
 - Delete "foobar (1).jpg"

Notes:
  - For safety, please make a backup before running this script
'''

# Import the Libraries
import os
import sys
import re

# Set list of valid file extensions
valid_extensions = [".jpg", ".JPG"]

# If folder path argument exists then use it
# Else use the current running folder
if len(sys.argv) > 1:
    folder_path = sys.argv[1]
else:
    folder_path = os.getcwd()

# Get all files from folder
file_names = os.listdir(folder_path)

# Set the regular expression
regex_exp = re.compile('\([\d]+\)')

for file_name in file_names:
    # If the file does not have a valid file extension
    # or does not have the regex expression
    # skip this loop
    file_ext = os.path.splitext(file_name)[1]
    if (file_ext not in valid_extensions):
        continue

    if (not regex_exp.search(file_name)):
        continue

    # Get the path to the file
    file_path = os.path.join(folder_path, file_name)

    # Delete the file
    print(f'Deleting {file_path}')
    os.remove(file_path)

