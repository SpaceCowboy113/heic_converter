import os
import sys
from PIL import Image
import pillow_heif

# Register pillow-heif as a HEIC opener
pillow_heif.register_heif_opener()


def convert_heic_to_format(output_format):
    """
    Convert HEIC files to the specified format (png or jpg)

    Args:
        output_format (str): The output format, either 'png' or 'jpg'
    """
    # Validate output format
    if output_format.lower() not in ['png', 'jpg']:
        print("Error: Format must be either 'png' or 'jpg'")
        print("Usage: python heic_converter.py [png|jpg]")
        return

    # Format-specific settings
    ext = output_format.lower()
    save_format = "PNG" if ext == "png" else "JPEG"
    save_kwargs = {} if ext == "png" else {"quality": 95, "optimize": True}

    # Define source and destination directories relative to this script's location
    base_dir = os.path.dirname(os.path.abspath(__file__))
    source_dir = os.path.join(base_dir, "original")
    dest_dir = os.path.join(base_dir, "converted")

    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        print(
            f"Please create a folder named 'original' in the same directory as this script.")
        return

    # Create destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)

    # Get list of files in source directory
    try:
        files = os.listdir(source_dir)
    except Exception as e:
        print(f"Error accessing source directory: {e}")
        return

    # Check if source directory is empty
    if not files:
        print(f"No files found in '{source_dir}'.")
        print("Please add HEIC files to convert.")
        return

    # Count for reporting
    heic_files_found = 0
    files_converted = 0
    files_skipped = 0

    # Process each HEIC file in the source directory
    for filename in files:
        if filename.lower().endswith(".heic"):
            heic_files_found += 1
            heic_path = os.path.join(source_dir, filename)
            output_filename = os.path.splitext(filename)[0] + f".{ext}"
            output_path = os.path.join(dest_dir, output_filename)

            # Skip if file already exists in destination folder
            if os.path.exists(output_path):
                print(
                    f"Skipping {filename} - {output_filename} already exists.")
                files_skipped += 1
                continue

            try:
                # Open and convert the image using Pillow (pillow-heif handles HEIC decoding)
                with Image.open(heic_path) as image:
                    image.save(output_path, save_format, **save_kwargs)
                print(f"Converted {filename} to {output_filename}")
                files_converted += 1
            except Exception as e:
                print(f"Error converting {filename}: {e}")

    # Summary report
    if heic_files_found == 0:
        print("No HEIC files found in the source directory.")
    else:
        print(f"\nConversion complete!")
        print(f"HEIC files found: {heic_files_found}")
        print(f"Files converted to {ext.upper()}: {files_converted}")
        print(f"Files skipped: {files_skipped}")


if __name__ == "__main__":
    # Check if format argument is provided
    if len(sys.argv) != 2:
        print("Error: Output format not specified")
        print("Usage: python heic_converter.py [png|jpg]")
        sys.exit(1)

    # Get output format from command line argument
    output_format = sys.argv[1].lower()
    convert_heic_to_format(output_format)
