# Django Text Analyzer

## Project Overview
Django Text Analyzer is a web-based application that allows users to analyze text by performing various operations such as removing punctuation, removing extra spaces, capitalizing text, converting text to uppercase, and removing new lines.

## Features
- Remove Punctuations
- Remove Extra Spaces
- Capitalize First Letter of Each Word
- Convert Text to Uppercase
- Remove New Lines

## Installation

### Prerequisites
- Python 3.x
- Django

### Steps to Install and Run
1. Clone this repository:
   ```sh
   git clone https://github.com/Shivampanwar11/Text-Analyzer.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Text-Analyzer
   ```
3. Install dependencies:
   ```sh
   pip install django
   ```
4. Run the server:
   ```sh
   python manage.py runserver
   ```
5. Open your browser and go to:
   ```sh
   http://127.0.0.1:8000/
   ```

## Project Structure
```
Text-Analyzer/
│── manage.py
│── textanalyzer/       # Main Django app
│   ├── templates/      # HTML templates
│   │   ├── index.html  # Main UI
│   │   ├── analyzed.html # Results Page
│   ├── views.py        # Django Views
│   ├── urls.py         # URL routing
│   ├── settings.py     # Django settings
│── static/             # CSS and JS files
```

## Usage
1. Open the web application.
2. Enter the text you want to analyze.
3. Select the desired operations.
4. Click the "Analyze" button to process your text.

## Author
**Shivam Panwar**  
GitHub: [Shivampanwar11](https://github.com/Shivampanwar11)

## License
This project is open-source and free to use.

## Contributions
Feel free to contribute! You can fork the repository, make changes, and submit a pull request.

