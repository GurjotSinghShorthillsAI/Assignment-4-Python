import os
import json
from dotenv import load_dotenv
from loaders.pdf_loader import PDFLoader
from loaders.docx_loader import DOCXLoader
from loaders.ppt_loader import PPTLoader
from data_extractor import DataExtractor
from storage.sql_storage import SQLStorage

class FileProcessor:
    def __init__(self, base_output_folder="output", config_file="config.env"):
        load_dotenv(config_file)
        self.base_output_folder = base_output_folder
        self.db_credentials = {
            'host': os.getenv("DB_HOST"),
            'user': os.getenv("DB_USER"),
            'password': os.getenv("DB_PASSWORD"),
            'database': os.getenv("DB_NAME")
        }
        self.loaders = {
            'pdf': PDFLoader(),
            'docx': DOCXLoader(),
            'pptx': PPTLoader()
        }
        self.file_paths = {
            'pdf': "test_files/pdf/small.pdf",
            'docx': "test_files/docx/small.docx",
            'pptx': "test_files/pptx/small.pptx"
        }
        self.ensure_directory(self.base_output_folder)

    def ensure_directory(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def save_to_file(self, data, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def process_file(self, loader, base_output_folder):
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
            self.ensure_directory(output_folder)
            self.save_to_file(data, os.path.join(output_folder, f"{file_type}_{content}.json"))

    def run(self):
        storage = SQLStorage(**self.db_credentials)
        if storage.connection.is_connected():
            print("Successfully connected to the MySQL database")
        else:
            print("Failed to connect to the MySQL database")

        for file_type, loader in self.loaders.items():
            loader.filepath = self.file_paths[file_type]
            self.process_file(loader, self.base_output_folder)

if __name__ == "__main__":
    processor = FileProcessor()
    processor.run()
