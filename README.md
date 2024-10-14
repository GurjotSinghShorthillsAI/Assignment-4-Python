# PDF, DOCX, and PPTX Data Extractor
This project provides a modular Python solution to extract text, hyperlinks, images, and tables from PDF, DOCX, and PPTX files while capturing metadata such as file type, page/slide numbers, font styles, and more. The project also includes functionality to store the extracted data in both files and a MySQL database.
## Project Structure
```
|-- loaders/
    |-- file_loader.py        # Abstract class for file loaders
    |-- pdf_loader.py         # PDF file loader
    |-- docx_loader.py        # DOCX file loader
    |-- ppt_loader.py         # PPTX file loader
|-- storage/
    |-- storage.py            # Abstract class for data storage
    |-- sql_storage.py        # SQL storage for extracted data
|-- tests/
    |-- test_extractor.py     #pytest test cases for functionality
|-- data_extractor.py         # Main class to extract text, links, images, and tables from files
|-- main.py                   # Main script to run the extraction and storage process
|-- config.env                # Environment variables for MySQL connection
|-- output/                   # Folder to store extracted data (text, links, images, tables)
|-- test_files/               # Test files (PDF, DOCX, PPTX) used for manual and unit testing
    |-- pdf/
    |-- docx/
    |-- pptx/
```
## Features
- Text Extraction: Extracts plain text from PDF, DOCX, and PPTX files along with metadata (font style, page number, slide number, headings).
- Hyperlink Extraction: Extracts URLs and linked text from PDF, DOCX, and PPTX files.
- Image Extraction: Extracts images and metadata (resolution, format, page/slide number) and stores them in separate folders.
- Table Extraction: Extracts tables and stores them in CSV format for each file type.
- Storage Options:
  - File Storage: Saves text, links, images, and tables into separate files.
  - SQL Storage: Stores extracted data into a MySQL database.
## Installation
- Clone the repo:
```
git clone https://github.com/your_username/pdf-docx-pptx-extractor.git
cd pdf-docx-pptx-extractor
```
- Set up a Python virtual environment and install dependencies:
```
python -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```
- Set up your MySQL database and create a .env file for MySQL credentials:
```
DB_HOST=your_host
DB_USER=your_user
DB_PASSWORD=your_password
DB_NAME=your_database
```
## Usage
- Run the main script:
```
python main.py
```
- The extracted data will be saved in the output/ folder and organized into subfolders based on file type (PDF, DOCX, PPTX). Additionally, data will be stored in the MySQL database if configured correctly.
- To change the files you want to extract data from, put your file in `test_files` folder in the intended folder, and change the path in `main.py` and run the code!
## Manual Testing
Test cases have been manually prepared and provided in the Excel file and can be tested with different file types and scenarios:
- PDF: Small, large, corrupted, annotated, and multilingual PDFs.
- DOCX: Small, large, corrupted annotated, and multilingual DOCX files.
- PPTX: Small, large, corrupted annotated, and multilingual PPTX files.
Please refer to the `test_files/` folder for these files.
## Unit Testing
I automated some of the manual test cases using `pytest`. So most of the file loading and validation logic is handled by automated tests.
To run unit tests:
```
pytest tests/test_extractor.py -v
```
