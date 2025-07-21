# 🧠 AI PDF Question Extractor

An AI-driven Python tool that extracts visual questions from educational PDFs. This system converts pages into images, allows manual cropping of question and option regions, and generates a structured JSON file. Ideal for building training datasets, MCQ interfaces, or automated test engines.

---

## 📌 Key Features

- 📄 Convert PDF pages to high-resolution images  
- ✂️ Manually crop questions and options using an OpenCV UI  
- 🗃 Organize visual question-answer pairs in a clean JSON structure  
- 🖼 Command-line viewer for quick visual verification  
- 💼 Designed for academic, research, and educational tech use  

---

## 🧰 Tech Stack

- **Language:** Python 3.x  
- **Libraries:** PyMuPDF, pdfplumber, Pillow, OpenCV, pdf2image  
- **Tools:** Poppler for Windows (for PDF rendering)  

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

###📄 License
This project is intended for educational, academic, and demonstration purposes only.

### Acknowledgements
Special thanks to the developers of open-source tools like PyMuPDF, OpenCV, and pdf2image that made this project possible.
