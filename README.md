# Morse Code Converter

A seamless, interactive web application built with Python and Flask that translates standard text into Morse code and decodes Morse code back into readable text. 

## Features
* **Two-Page Interface:** Features a clean, welcoming intro page that routes users to the main converter tool.
* **Bi-directional Translation:** 
  * Text ➔ Morse Code
  * Morse Code ➔ Text
* **Modern UI/UX:** Responsive design with a dark mode color palette, custom styling, and intuitive navigation.
* **One-Click Copy:** Easily copy your translated results to the clipboard with visual success feedback.

## Project Structure
```text
morse-code-converter/
│
├── templates/
│   ├── intro.html         # The welcome/landing page
│   └── converter.html     # The main translation interface
│
├── app.py                 # Flask routing and web server
├── morse_converter.py     # Core translation logic and dictionaries
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation