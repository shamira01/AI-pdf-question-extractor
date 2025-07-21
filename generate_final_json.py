import os
import json
from collections import defaultdict

# Folder where your cropped images are saved
crop_dir = "output/crops"
output_path = "output/final_questions.json"

# Group cropped images by page number
grouped = defaultdict(list)

for filename in sorted(os.listdir(crop_dir)):
    if filename.startswith("crop_") and filename.endswith(".png"):
        parts = filename.replace(".png", "").split("_")
        if len(parts) == 3:
            page_num = int(parts[1])
            grouped[page_num].append(filename)

# Prepare structured output
final_data = []

for page in sorted(grouped):
    images = grouped[page]
    if len(images) >= 1:
        question_img = os.path.join(crop_dir, images[0])
        option_imgs = [os.path.join(crop_dir, img) for img in images[1:]]
        final_data.append({
            "question": question_img,
            "option_images": option_imgs
        })

# Save to JSON file
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(final_data, f, indent=2)

print(" Final structured JSON saved to:", output_path)
