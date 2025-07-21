import cv2
import os

# Input and output paths
input_dir = "output/pages"
output_dir = "output/crops"
os.makedirs(output_dir, exist_ok=True)

# Globals for cropping
refPt = []
cropping = False
crop_count = 1
current_image = None

def click_and_crop(event, x, y, flags, param):
    global refPt, cropping, current_image

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True

    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False

        cv2.rectangle(current_image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("Image", current_image)

        # Crop and save
        roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        filename = f"crop_{page_num+1}_{len(os.listdir(output_dir)) + 1}.png"
        cv2.imwrite(os.path.join(output_dir, filename), roi)
        print(f" Saved: {filename}")

# Loop through each page image
image_files = sorted(os.listdir(input_dir))
for page_num, filename in enumerate(image_files):
    image_path = os.path.join(input_dir, filename)
    image = cv2.imread(image_path)
    clone = image.copy()
    current_image = image

    print(f"\n Cropping from: {filename}")
    print(" INSTRUCTIONS: Drag mouse to crop. Press ESC to go to next page.\n")

    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", click_and_crop)

    while True:
        cv2.imshow("Image", current_image)
        key = cv2.waitKey(1) & 0xFF

        # ESC key to move to next image
        if key == 27:
            break

    cv2.destroyAllWindows()

print("\n Done cropping all pages!")
