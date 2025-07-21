# 🧠 AI PDF Question Extractor

![GitHub Repo stars](https://img.shields.io/github/stars/shamira01/AI-pdf-question-extractor?style=social)
![GitHub forks](https://img.shields.io/github/forks/shamira01/AI-pdf-question-extractor?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/shamira01/AI-pdf-question-extractor)
![Python](https://img.shields.io/badge/language-Python-blue?logo=python)

<p align="center">
  <img src="assets/banner.png" alt="Project Banner" width="600"/>
</p>

---

## 📖 Overview

**AI PDF Question Extractor** is a Python-based tool designed to extract visual question-answer pairs from educational PDFs.  
It converts each page into an image, allows users to manually crop questions and options using a simple UI, and outputs a clean, structured JSON format.

This project is perfect for:

- Creating datasets for AI/ML models
- Automating MCQ generation for EdTech apps
- Visual data labeling and content structuring

---

## 📌 Features

- 📄 Convert PDF pages to high-resolution images  
- ✂️ Manually crop questions and options via OpenCV UI  
- 🗃 Organize cropped image data into structured JSON  
- 👀 Simple CLI tool to view and verify extracted content  
- 🧪 Suitable for academic, EdTech, or research use  

---

## 🧰 Tech Stack

- **Language:** Python 3.x
- **Libraries:** 
  - PyMuPDF
  - pdfplumber
  - pdf2image
  - OpenCV (cv2)
  - Pillow (PIL)
- **Tool:** Poppler (required for pdf2image)


---

## 📁 Directory Structure

pdf_question_extractor/
├── pdfs/ # Original input PDF
│ └── sample.pdf
├── output/
│ ├── pages/ # Rendered full-page images
│ ├── crops/ # Manually cropped question/option images
│ └── final_questions.json # Structured image metadata
├── convert_pdf_to_images.py # Converts PDF to page images
├── crop_images.py # OpenCV UI to crop and label images
├── generate_final_json.py # Maps cropped images to JSON
├── view_questions_and_options.py # CLI viewer for verification
├── README.md # Project documentation

---

## 🚀 How to Run the Project

### 1️ Install Required Dependencies

```bash
pip install pymupdf pdfplumber pdf2image pillow opencv-python
⚠️ Additionally, install Poppler for Windows
and add its /bin directory to your system PATH.

2️ Convert PDF to Images
python convert_pdf_to_images.py

3️ Crop Questions and Options (Manual)
python crop_images.py

Use your mouse to draw bounding boxes around questions and options
Press s to save the crop
Press q to go to the next page

4️ Generate Structured JSON Output
python generate_final_json.py

5️ View Questions and Options (Optional)
python view_questions_and_options.py

📌 Sample JSON Output

{
  "question": "output/crops/crop_1_1.png",
  "option_images": [
    "output/crops/crop_1_2.png",
    "output/crops/crop_1_3.png",
    "output/crops/crop_1_4.png"
  ]
}
```
---

### 👩‍💻 Author
Shamira Anjum
Computer Science Engineer | Python Developer | AI Enthusiast
🔗 GitHub: @shamira01

### 📄 License
This project is intended for educational, academic, and demonstration purposes only.

### Acknowledgements
Special thanks to the developers of open-source tools like PyMuPDF, OpenCV, and pdf2image that made this project possible.
