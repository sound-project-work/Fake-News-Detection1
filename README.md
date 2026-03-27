 Project Name:
Real-Time Fake News Detection System Using Keyword Analysis and OCR

Project Overview:
This project is a web-based application that identifies whether news content is likely fake or real. Users can either:
Enter or paste news text directly.
Upload a news image (like screenshots from Instagram, WhatsApp, or websites) containing news headlines or content.
The system analyzes the input using a combination of keyword detection and OCR (Optical Character Recognition) to provide a real-time verdict on the credibility of the news.

Key Features:
Text Input Detection
Users can paste a news headline or full article into a web form.
The system checks for fake vs real keywords and displays the result instantly.

Image Upload Detection:
Users can upload images of news content (e.g., Instagram screenshots, WhatsApp forwards).
OpenCV + pytesseract extracts the text from the image.
Extracted text is analyzed using the same keyword detection logic.

Real-Time Detection:
The system provides immediate feedback:
⚠️ Likely Fake
✅ Likely Real
ℹ️ Inconclusive
User-Friendly Web Interface
Web-based, works on any modern browser.
Clear and simple layout with text input, image upload, and result display.

Technologies, Tools, and Concepts Used:
HTML-Web page structure: input textarea, upload button, result display
CSS-Styling and layout of the web page for readability and interface design
JavaScript-Keyword detection logic for real-time text analysis, DOM manipulation, conditional feedback
Python 3.13+-Backend programming for image processing and OCR
Flask-Web server to handle image upload and backend processing
OpenCV-Image preprocessing: grayscale conversion, thresholding, resizing for better OCR results
pytesseract-Optical Character Recognition: extracting text from uploaded images
Keyword Analysis-Detecting fake or real news by checking for predefined fake/real keywords in text
DOM Manipulation (JS)-Accessing HTML elements, reading input, writing output dynamically
Conditional Logic (JS / Python)-Comparing keyword counts to classify news as fake or real
Image Preprocessing Concepts-Grayscale conversion, thresholding, resizing, noise reduction to improve OCR accuracy
Text Processing Concepts-Lowercasing, keyword matching, counting occurrences, simple scoring mechanism,Sample Inputs,Fake News Example,Copy code

BREAKING: Miracle cure hidden from public exposed by anonymous source!
Real News Example
Copy code

According to BBC, new COVID-19 guidelines published today for vaccine distribution
Images
High-resolution screenshots of news headlines or social media posts work best.
Avoid blurred or heavily compressed images (WhatsApp compression may reduce OCR accuracy).
