# Step 1: Take folder path as input
# Step 2: Loop through all files in that folder
# Step 3: Detect file extension
# Step 4: Move file into the correct category folder

import os
folder_path = input("Enter the folder path to organize: ")
for root, dirs, files in os.walk(folder_path):
    for file in files:
        print(file)
file_ext = os.path.splitext(file)[1].lower()
