import json
import cv2
import os

#  Toggle this to True if you want to view images visually
show_images = True

# Load the JSON
with open("output/final_questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Go through each question block
for i, item in enumerate(data, start=1):
    print(f"\n🔹 Question {i}")
    print(f" Question image: {item['question']}")

    if item["option_images"]:
        print(" Options:")
        for opt in item["option_images"]:
            print(f"  - {opt}")
    else:
        print(" No options available.")

    #  If enabled, display the question and options visually
    if show_images:
        # Show question image
        q_img = cv2.imread(item["question"])
        if q_img is not None:
            cv2.imshow(f"Question {i}", q_img)
            cv2.waitKey(1000)
            cv2.destroyWindow(f"Question {i}")

        # Show option images
        for idx, opt_path in enumerate(item["option_images"], start=1):
            o_img = cv2.imread(opt_path)
            if o_img is not None:
                cv2.imshow(f"Q{i} - Option {idx}", o_img)
                cv2.waitKey(1000)
                cv2.destroyWindow(f"Q{i} - Option {idx}")
