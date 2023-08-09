import os
import shutil

def organize_files(source_directory):
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            if file.lower().endswith(('.mp4', '.mp3')):
                move_to_directory(file_path, 'videos')
                
            elif file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                move_to_directory(file_path, 'images', subfolder=True)
                
            elif 'installer' in file.lower():
                move_to_directory(file_path, 'installers')
                
            elif 'gaming' in file.lower():
                trash_file(file_path)
                
def move_to_directory(file_path, category, subfolder=False):
    destination_directory = os.path.join(os.getcwd(), category)
    if subfolder:
        file_name = os.path.basename(file_path)
        folder_name = os.path.splitext(file_name)[0]
        destination_directory = os.path.join(destination_directory, folder_name)
    
    os.makedirs(destination_directory, exist_ok=True)
    shutil.move(file_path, os.path.join(destination_directory, os.path.basename(file_path)))

def trash_file(file_path):
    # You can customize this function to move files to a "Trash" directory instead of permanently deleting them
    trash_directory = os.path.join(os.getcwd(), "Trash")
    os.makedirs(trash_directory, exist_ok=True)
    shutil.move(file_path, os.path.join(trash_directory, os.path.basename(file_path)))

if __name__ == "__main__":
    source_directory = "/path/to/source/directory"  # Replace with your source directory
    organize_files(source_directory)
