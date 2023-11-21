from PIL import Image
import os

def change_dpi(file_path, dpi):
    try:
        # Open the image
        image = Image.open(file_path)

        # Set DPI
        image.info['dpi'] = (dpi, dpi)

        # Save the image, overwriting the original file
        image.save(file_path, format="PNG", dpi=(dpi, dpi))

        print(f"Changed DPI of {file_path} to {dpi} DPI")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def process_folder(folder_path, dpi):
    # Walk through the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if the file is a PNG
            if file.lower().endswith(".png"):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")
                change_dpi(file_path, dpi)

if __name__ == "__main__":
    # Specify the folder to process (current directory in this case)
    folder_to_process = "."

    # Specify the DPI (e.g., 72)
    dpi = 72

    # Process the folder and its subfolders
    process_folder(folder_to_process, dpi)
