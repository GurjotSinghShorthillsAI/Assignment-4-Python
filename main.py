import os
import json
from storage.sql_storage import SQLStorage
from loaders.pdf_loader import PDFLoader
from loaders.docx_loader import DOCXLoader
from loaders.ppt_loader import PPTLoader
from data_extractor import DataExtractor
from dotenv import load_dotenv

# Load environment variables from 'config.env'
load_dotenv("config.env")

def ensure_directory(path):
    """
    Ensures that the specified directory exists. If the directory does not exist,
    it is created.

    Args:
        path (str): Path to the directory to be ensured.
    """
    if not os.path.exists(path):
        os.makedirs(path)

def save_to_file(data, filename):
    """
    Serializes data to a JSON file.

    Args:
        data: Data to be serialized.
        filename (str): Path to the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def process_file(loader, base_output_folder):
    """
    Processes a file for extracting text, links, images, and tables, and then saves them
    to JSON files.

    Args:
        loader: An instance of a FileLoader subclass (PDFLoader, DOCXLoader, PPTLoader).
        base_output_folder (str): Base directory to store the output files.
    """
    extractor = DataExtractor(loader)
    content_types = ['text', 'links', 'images', 'tables']
    extraction_methods = {
        'text': extractor.extract_text,
        'links': extractor.extract_links,
        'images': extractor.extract_images,
        'tables': extractor.extract_tables
    }
    
    for content in content_types:
        data = extraction_methods[content]()
        file_type = loader.file_extension.lstrip('.')
        output_folder = os.path.join(base_output_folder, content, file_type)
        ensure_directory(output_folder)
        save_to_file(data, os.path.join(output_folder, f"{file_type}_{content}.json"))

def main():
    """
    Main execution function that sets up file paths, initializes loaders, extracts data,
    and connects to a MySQL database to store extracted data.
    """
    # Retrieve database credentials from environment variables
    db_credentials = {
        'host': os.getenv("DB_HOST"),
        'user': os.getenv("DB_USER"),
        'password': os.getenv("DB_PASSWORD"),
        'database': os.getenv("DB_NAME")
    }
    
    # Create the base directory structure for outputs
    base_output_folder = "output"
    ensure_directory(base_output_folder)
    
    # Setup file paths for different types of documents
    file_paths = {
        'pdf': "test_files/pdf/large.pdf",
        'docx': "test_files/docx/large.docx",
        'pptx': "test_files/pptx/large.pptx"
    }

    # Initialize loaders for handling different file types
    loaders = {
        'pdf': PDFLoader(),
        'docx': DOCXLoader(),
        'pptx': PPTLoader()
    }
    
    # Process each file type using its respective loader
    for file_type, loader in loaders.items():
        loader.filepath = file_paths[file_type]
        process_file(loader, base_output_folder)
    
    # Initialize SQLStorage with the provided credentials and connect to the database
    storage = SQLStorage(**db_credentials)
    if storage.connection.is_connected():
        print("Successfully connected to the MySQL database")
    else:
        print("Failed to connect to the MySQL database")

if __name__ == "__main__":
    main()
