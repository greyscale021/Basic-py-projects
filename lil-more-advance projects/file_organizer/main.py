# Step 1: Take folder path as input
# Step 2: Loop through all files in that folder
# Step 3: Detect file extension
# Step 4: Move file into the correct category folder

import os

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Audio': ['.mp3', '.wav'],
    'Code': ['.py', '.js', '.html', '.css'],
    'Archives': ['.zip', '.rar']
}

folder_path = input("Enter the folder path to organize: ")

for path, subfolder, files in os.walk(folder_path):
    for file in files:
        file_ext = os.path.splitext(file)[1].lower()
        for category, extensions in file_types.items():
            if file_ext in extensions:
                category_folder = os.path.join(folder_path, category)
                os.makedirs(category_folder, exist_ok=True)

                source = os.path.join(path, file)
                destination = os.path.join(category_folder, file)
                os.rename(source, destination)
                print(f"Moved: {file} → {category}")
