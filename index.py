import os
import shutil
from datetime import datetime
from tqdm import tqdm

# Define example source and destination directories
source_directory = r"C:\ExamplePath\source_folder"
backup_directory = r"C:\ExamplePath\backup_folder"
usb_drive = r"D:\backup_usb"

# Format the timestamp
timestamp = datetime.now().strftime("%d_%m_%y")
backup_directory_with_timestamp = os.path.join(backup_directory, f"backup_{timestamp}")

# Perform the Backup
def backup_files(source_dir, backup_dir):
    # Check if directory exists; if not, create it
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Perform the backup while preserving folder and directory structure
    total_files = sum(len(files) for _, _, files in os.walk(source_dir))
    with tqdm(total=total_files, desc="Backing up", unit="file") as pbar:
        for root, dirs, files in os.walk(source_dir):
            relative_path = os.path.relpath(root, source_dir)
            backup_path = os.path.join(backup_dir, relative_path)

            if not os.path.exists(backup_path):
                os.makedirs(backup_path)

            for file in files:
                source_file = os.path.join(root, file)
                destination_file = os.path.join(backup_path, file)
                shutil.copy2(source_file, destination_file)
                pbar.set_postfix(file=file)
                pbar.update(1)

    print(f"Backup completed to {backup_dir}!")

# Compress and copy the compressed file to the desired directory
def compress_backup(backup_dir):
    print("Starting backup compression...")
    zip_file_name = f"backup_{timestamp}.zip"
    zip_file_path = os.path.join(backup_dir, zip_file_name)
    shutil.make_archive(zip_file_path[:-4], 'zip', backup_dir)
    print(f"Backup compressed at: {zip_file_path}")
    return zip_file_path

# Create progress bar for copying
def copy_with_progress(src, dest):
    file_size = os.path.getsize(src)
    with tqdm(total=file_size, desc="Copying to USB drive", unit="B", unit_scale=True) as pbar:
        with open(src, 'rb') as fsrc, open(dest, 'wb') as fdest:
            while True:
                buffer = fsrc.read(1024 * 1024)
                if not buffer:
                    break
                fdest.write(buffer)
                pbar.update(len(buffer))

if __name__ == "__main__":
    print("Starting backup to the main directory...")
    backup_files(source_directory, backup_directory_with_timestamp)

    # Check if USB drive is connected and execute the second part if it is
    if os.path.exists(usb_drive):
        # Compress the file to zip
        zip_file_path = compress_backup(backup_directory_with_timestamp)
        print("Copying compressed backup to USB drive...")

        # Copy the compressed file to the USB drive
        zip_file_on_usb = os.path.join(usb_drive, os.path.basename(zip_file_path))
        copy_with_progress(zip_file_path, zip_file_on_usb)
        print(f"Compressed backup copied to USB drive: {usb_drive}")

        # Remove the zip file from the main backup directory after copying to USB
        if os.path.exists(zip_file_path):
            os.remove(zip_file_path)
            print("ZIP file removed from the main backup directory.")

    print("Backup successfully completed in both locations." if os.path.exists(usb_drive) else "Backup completed only in the main directory.")
