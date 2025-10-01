import os
import shutil

print("📂 File Organizer - Day 26")

# Create folders for file types
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
    "Others": []
}

# Folder to organize (you can change this path)
source_folder = "C:/Users/YourName/Downloads"

# Organize files
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if os.path.isfile(file_path):
        moved = False
        for folder, extensions in folders.items():
            if filename.lower().endswith(tuple(extensions)):
                folder_path = os.path.join(source_folder, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"✅ Moved {filename} → {folder}")
                moved = True
                break
        if not moved:
            folder_path = os.path.join(source_folder, "Others")
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(file_path, os.path.join(folder_path, filename))
            print(f"📦 Moved {filename} → Others")
