import os
import shutil

# Define file extensions and corresponding folders
file_extensions = {
    "pdf": "PDF's",
    "png": "Images",
    "jpg": "Images",
    "jpeg": "Images",
    "gif": "Images",
    "mp3": "Music",
    "wav": "Music",
    "mp4": "Video",
    "avi": "Video",
    "mkv": "Video",
    "doc": "Documents",
    "docx": "Documents",
    "txt": "Documents",
    "md": "Documents",
    "csv": "Data",
    "xlsx": "Data",
    "zip": "Archives",
    "rar": "Archives",
    "exe": "Executables",
    "bat": "Executables",
    "py": "Executables"
}

def main():
    # Get the folder location from the user
    path = input("Folder location: ")

    try:
        # Check if the specified path exists
        os.listdir(path)
    except FileNotFoundError:
        print("Path not found")
        return

    # Iterate through files in the specified folder
    for i in os.listdir(path):
        tmp_file_path = path + "/" + i

        # Check if the item is a file
        if os.path.isfile(tmp_file_path):
            # Split file name and extension
            name, extension = i.split(".")
            # Determine the destination folder based on the file extension
            folder = file_extensions[extension]

            # Check if the destination folder exists, if not create it
            if os.path.isdir(path + f"/{folder}"):
                dest = f"{path}" + "/" + f"{folder}" + \
                    "/" + f"{name}" + "." + f"{extension}"
                # Move the file to its designated folder
                shutil.move(tmp_file_path, dest)
            else:
                os.mkdir(path + f"/{folder}")
                dest = f"{path}" + "/" + f"{folder}" + \
                    "/" + f"{name}" + "." + f"{extension}"
                # Move the file to its designated folder
                shutil.move(tmp_file_path, dest)

# Call the main function
main()