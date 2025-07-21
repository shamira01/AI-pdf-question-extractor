import fitz  # PyMuPDF
import os
import json

# Set paths
pdf_path = "pdfs/sample.pdf"
output_image_dir = "output/images"
output_json_path = "output/data.json"

# Make sure output folders exist
os.makedirs(output_image_dir, exist_ok=True)

# Load the PDF
doc = fitz.open(pdf_path)

# Output JSON list
output_data = []

# Loop through pages
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text = page.get_text()

    image_paths = []

    # Extract and save all images from the page
    for img_index, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image_filename = f"page{page_num+1}_image{img_index+1}.{image_ext}"
        image_path = os.path.join(output_image_dir, image_filename)

        with open(image_path, "wb") as f:
            f.write(image_bytes)

        image_paths.append(image_path)

    # Add to JSON structure
    output_data.append({
        "page": page_num + 1,
        "text": text.strip(),
        "images": image_paths
    })

# Write JSON to file
with open(output_json_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, indent=2)

print("✅ Done! Text and images extracted.")
