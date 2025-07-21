from pdf2image import convert_from_path
import os

# Path to your PDF
pdf_path = "pdfs/sample.pdf"

# Output folder
output_dir = "output/pages"
os.makedirs(output_dir, exist_ok=True)

# Convert PDF pages to images (each at 300 DPI)
pages = convert_from_path(pdf_path, dpi=300)

# Save each page as a separate PNG
for i, page in enumerate(pages):
    image_path = os.path.join(output_dir, f"page_{i+1}.png")
    page.save(image_path, "PNG")

print("All pages converted to images in output/pages/")
