import sys
from collections.abc import Iterable
from pathlib import Path

import pymupdf  # PyMuPDF
from PIL import Image

# A4 dimensions in inches (8.27 x 11.69) and in points (1 point = 1/72 inch)
PAGE_WIDTH = int(8.27 * 72)  # Width in points: 595
PAGE_HEIGHT = int(11.69 * 72)  # Height in points: 841


def get_files(path: Path) -> Iterable[Path]:
    if path.is_file():
        yield path

    else:
        for p in sorted(path.iterdir()):
            yield from get_files(p)


def add_pdf_to_pdf(doc: pymupdf.Document, pdf_file: Path) -> None:
    """Resizes PDF pages to A4 and adds them to the final document"""
    pdf_doc = pymupdf.open(pdf_file)

    for page_num in range(len(pdf_doc)):
        pdf_page = pdf_doc[page_num]
        a4_page = doc.new_page(width=PAGE_WIDTH, height=PAGE_HEIGHT)

        # Scale and center the existing page content into A4
        rect = pdf_page.rect
        scale = min(PAGE_WIDTH / rect.width, PAGE_HEIGHT / rect.height)
        new_width = rect.width * scale
        new_height = rect.height * scale

        x_offset = (PAGE_WIDTH - new_width) / 2
        y_offset = (PAGE_HEIGHT - new_height) / 2

        # Insert scaled PDF content
        a4_page.show_pdf_page(
            pymupdf.Rect(x_offset, y_offset, x_offset + new_width, y_offset + new_height),
            pdf_doc,
            page_num,
        )


def add_image_to_pdf(doc: pymupdf.Document, image_path: Path) -> None:
    """Add an image centered on an A4-sized PDF page while maintaining aspect ratio"""
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure it's in RGB mode

    # Get original image size
    img_width, img_height = img.size

    # Scale image to fit within A4 while maintaining aspect ratio
    scale = min(PAGE_WIDTH / img_width, PAGE_HEIGHT / img_height)
    new_width = int(img_width * scale)
    new_height = int(img_height * scale)

    # Calculate centering position
    x_offset = (PAGE_WIDTH - new_width) // 2
    y_offset = (PAGE_HEIGHT - new_height) // 2

    # Create a blank A4 PDF page
    page = doc.new_page(width=PAGE_WIDTH, height=PAGE_HEIGHT)

    # Insert the image centered on the A4 page
    img_rect = pymupdf.Rect(x_offset, y_offset, x_offset + new_width, y_offset + new_height)
    page.insert_image(img_rect, filename=image_path)


def merge_pdfs_and_images(output_pdf: Path, input_paths: Path) -> None:
    print("Starting to merge pdf and image files...")
    doc = pymupdf.open()

    for path in input_paths:
        for f in get_files(path):
            if f.suffix == ".pdf":
                print(f"  > merging pdf file: {f.name}")
                # Insert PDF pages
                add_pdf_to_pdf(doc, f)
                print("    > done!")

            elif f.suffix in (".bmp", ".gif", ".jpeg", ".jpg", ".png", ".tif", ".tiff", ".webp"):
                print(f"  > merging image file: {f.name}")
                # Process image file and add it as an A4 page
                add_image_to_pdf(doc, f)
                print("    > done!")

    print("All files merged!")
    print("Saving the merged pdf...")

    # Save the final merged PDF
    doc.save(output_pdf)
    doc.close()

    print("  > done!")


def main() -> None:
    paths = [Path(path) for path in sys.argv[1:]]
    merge_pdfs_and_images(Path("output.pdf"), paths)


if __name__ == "__main__":
    main()
