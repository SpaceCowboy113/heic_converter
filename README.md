# HEIC Image Converter

A simple Python utility that converts HEIC image files to PNG or JPEG format.  Useful for converting
iphone/ipad images to a more common format in bulk.  Just drop your HEIC files into the original folder,
run the script, and voila, your images are converted and ready to use.

## Description

This script automatically converts all HEIC image files from an "original" folder to your chosen format (PNG or JPEG) and saves them in a "converted" folder. It includes error handling, skips already converted files, and provides informative user feedback.

## Features

- Convert HEIC files to either PNG or JPEG format
- Creates necessary folders if they don't exist
- Skips files that have already been converted
- Provides helpful error messages and conversion statistics
- Simple to use with minimal setup

## Requirements

- Python 3.6 or higher
- Pillow library
- pillow_heif library

## Installation

1. Clone this repository or download the script
2. Install the required dependencies:

```bash
pip3 install Pillow pillow-heif
```

## Setup

1. Place the script in a directory of your choice
2. Create a folder named "original" in the same directory as the script
3. Place your HEIC files in the "original" folder

## Usage

Run the script from the command line with your desired output format (mandatory):

```bash
# For PNG conversion:
python heic_converter.py png

# For JPEG conversion:
python heic_converter.py jpg
```

The script will:
1. Check if the "original" folder exists and contains files
2. Create a "converted" folder if it doesn't exist
3. Convert all HEIC files to the specified format
4. Skip any files that have already been converted
5. Display a summary of the conversion process

## Example Output

```
Converting image1.heic to image1.jpg
Converting image2.heic to image2.jpg
Skipping image3.heic - image3.jpg already exists

Conversion complete!
HEIC files found: 3
Files converted to JPG: 2
Files skipped: 1
```

## Format Notes

- **PNG**: Best for lossless quality, but results in larger file sizes
- **JPEG**: Better for sharing and reduced file size, with minimal quality loss (uses 95% quality setting)

## Troubleshooting

- **"No files found in 'original'"**: Add HEIC files to the "original" folder
- **"Source directory does not exist"**: Create an "original" folder in the same directory as the script
- **"Output format not specified"**: Make sure to include either "png" or "jpg" when running the script
- **Import errors**: Make sure you've installed the required dependencies

## License

This project is open source and available under the [MIT License](LICENSE).