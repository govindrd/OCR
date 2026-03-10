📄 OCR Text Recognition using Tesseract
This project implements Optical Character Recognition (OCR) to extract text from images using Tesseract OCR and Python. The system processes input images, detects characters, and converts them into machine-readable text.
The project demonstrates how OCR technology can be used for digitizing printed documents, extracting text from images, and automating data entry tasks.

🚀 Features
Extracts text from images using Tesseract OCR
Supports different image formats
Image preprocessing for better recognition
GUI support using Python
Uses a CRNN deep learning model for improved text recognition
Simple and easy-to-use interface

🛠️ Technologies Used
Python
Tesseract OCR
OpenCV
TensorFlow / Keras
Pillow
NumPy

📂 Project Structure
OCR/

│
├── Images/                       # Sample images for OCR
├── Textemage.py                  # Main OCR processing script
├── ex.py                         # Execution script
├── icon.png                      # Application icon
├── Text_recognizer_Using_CRNN.h5 # Pretrained CRNN model
└── README.md

⚙️ Installation
1. Clone the repository
   git clone https://github.com/govindrd/OCR.git
   cd OCR
2. Install required libraries
  pip install opencv-python
  pip install pytesseract
  pip install numpy
  pip install pillow
  pip install tensorflow
3. Install Tesseract OCR
   Download and install Tesseract:

4. How to Run
   Run the main script: python Textemage.py

📸 Example
Input Image → OCR Processing → Extracted Text Output
Example use cases:
Document digitization
Text extraction from scanned images
Automating data entry
Image-based text analysis

