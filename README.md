# Backup Script

This project is a Python script designed to perform backups of specified directories and compress them for storage. 

## Requirements

To get started, you need to install the necessary dependencies. You can do this easily by using the `requirements.txt` file provided in the repository.

### Installation

1. Clone the repository (or download the ZIP file):
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - **Windows:**
      ```bash
      venv\Scripts\activate
      ```
    - **macOS/Linux:**
      ```bash
      source venv/bin/activate
      ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

5. Update the script with your preferred directory paths:
    - Open the `index.py` script and replace the example directories with your desired source and backup paths.

    ```python
    # Example paths to modify
    source_directory = r"C:\ExamplePath\source_folder"
    backup_directory = r"C:\ExamplePath\backup_folder"
    usb_drive = r"D:\backup_usb"
    ```

6. Configure the batch file:
    - Open the `.bat` file and ensure that the paths to your virtual environment and Python script are correct.

## Usage

Once you have installed the requirements and set the directories, you can run the script to perform the backup.

### Creating a Shortcut

1. **Create a shortcut** to the `.bat` file:
    - Right-click the `.bat` file and select **Create shortcut**.
    - Move the shortcut to a convenient location, such as your Desktop.

2. **Running the Script**:
    - After creating the shortcut, you can easily execute the backup script by double-clicking the shortcut you created. It will execute everything automatically.

## Notes

- Make sure that the paths you provide in both the Python script and batch file are valid and accessible.
- If you wish to customize further, check the script comments for more options.
