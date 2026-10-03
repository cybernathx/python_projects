import os
import shutil

folder = input("Enter the name of the folder to organize: ")
images = f"{folder}/images"
documents = f"{folder}/documents"
music = f"{folder}/music"
videos = f"{folder}/videos"
python = f"{folder}/python"
others = f"{folder}/others"

def move_files(source_path, destination_folder, file):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"{destination_folder} folder created")

    destination_path = os.path.join(destination_folder, file)
    if os.path.exists(destination_path):
        print(f"{file} file already exists, skipped")
        return
    
    shutil.move(source_path, destination_path)
    print(f"Moved: {file}")

if os.path.exists(folder):
    for file in os.listdir(folder):
        source_path = os.path.join(folder, file)      

        if os.path.isfile(source_path):
            if file.lower().endswith((".jpg", ".png", ".jpeg")):
                move_files(source_path, images, file)
            elif file.lower().endswith((".pdf", ".txt", ".docx")):
                move_files(source_path, documents, file)
            elif file.lower().endswith((".mp3", ".wav")):
                move_files(source_path, music, file)
            elif file.lower().endswith((".mp4", ".mkv")):
                move_files(source_path, videos, file)
            elif file.lower().endswith((".py")):
                move_files(source_path, python, file)
            else:
                move_files(source_path, others, file)
    print("Organization complete!")
else:
    print("Folder does not exist.")
                

