# PDF and Image Merger

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?logo=buy-me-a-coffee&logoColor=black)](<https://buymeacoffee.com/jromero132> "Buy Me a Coffee - jromero132")
[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](<https://python.org> "Go to Python homepage")
![Last commit](https://img.shields.io/github/last-commit/jromero132/pdf-merger "Last commit")
---

This project provides a `Python` script to **merge all PDF files and images in a directory into a single PDF file**.
PDFs and images are centered on custom-page-sized pages (defaults to `A4`) while maintaining their aspect ratio.

## Features

- Merge multiple `PDF` files into a single `PDF`
- Convert and add images (`BMP`, `GIF`, `JPEG`, `JPG`, `PNG`, `TIF`, `TIFF`, `WEBP`) to the merged `PDF`
- Center images on custom-page-sized pages (defaults to `A4`) while maintaining aspect ratio
- Recursively process files in directories

## Requirements

- Python 3.6+
- Dependencies listed in `requirements.txt`

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/jromero132/pdf-merger.git
   cd pdf-merger
   pip install -r requirements.txt```

## Usage

Run the script from the command line, providing the paths to the files or directories you want to merge:  
`python main.py /path/to/file1.pdf /path/to/image_directory /path/to/file2.jpg`

The script will create a merged `PDF` file named output.pdf in the current directory.

## Supported File Types

- PDF files (`*.pdf`)
- Images: `BMP`, `GIF`, `JPEG`, `JPG`, `PNG`, `TIF`, `TIFF`, `WEBP`

## How It Works

1. The script iterates through all provided paths.
2. For each path:
   - If it's a file, it processes the file.
   - If it's a directory, it recursively processes all files in the directory.
3. `PDF` files are directly inserted into the output `PDF`.
4. Images are converted to `PDF` pages:
   - Each image is centered on an custom-page-sized page (defaults to `A4`).
   - The aspect ratio of the image is maintained.
5. All processed pages are combined into a single output `PDF` file.

## Support

If you encounter any problems or have any questions, please open an issue in the GitHub repository.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the terms of the license file included in this repository.

### Happy Coding! 🚀
