import os
import shutil

path_to_organize = "C:/Users/user/Downloads"

file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Documents": [".pdf", ".txt", ".doc", ".docx", ".ppt", ".pptx"],
    "Archives": [".zip", ".tar", ".mxd", ".gpkg"],
    "Music": [".mp3", ".m4a"],
    "Files": [".json"]
}

for filename in os.listdir(path_to_organize):
    file_path = os.path.join(path_to_organize, filename)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    moved = False

    for folder, extensions in file_types.items():
        if filename.lower().endswith(tuple(extensions)):
            folder_path = os.path.join(path_to_organize, folder) 

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            destination = os.path.join(folder_path, filename)

            # Handle duplicates
            if os.path.exists(destination):
                base, ext = os.path.splitext(filename)
                counter = 1
                while True:
                    new_name = f"{base}_{counter}{ext}"
                    new_destination = os.path.join(folder_path, new_name)
                    if not os.path.exists(new_destination):
                        destination = new_destination
                        break
                    counter += 1

            shutil.move(file_path, destination)
            print(f"{filename} moved to {folder}")
            moved = True
            break

    # If no category matched
    if not moved: 
        other_path = os.path.join(path_to_organize, "Others")

        if not os.path.exists(other_path):
            os.makedirs(other_path)

        destination = os.path.join(other_path, filename)
        shutil.move(file_path, destination)
        print(f"{filename} moved to Others")
