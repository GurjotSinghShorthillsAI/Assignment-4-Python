import os
import json
from dotenv import load_dotenv
from loaders.pdf_loader import PDFLoader
from loaders.docx_loader import DOCXLoader
from loaders.ppt_loader import PPTLoader
from data_extractor import DataExtractor
from storage.sql_storage import SQLStorage

class FileProcessor:
    """
    This class processes files by extracting their content (text, links, images, tables) using different file loaders
    and stores the extracted data in JSON files. It also connects to a MySQL database for further storage if required.

    Attributes:
        base_output_folder (str): The base directory where the output will be saved.
        config_file (str): The configuration file for loading environment variables.
        db_credentials (dict): Dictionary containing database credentials loaded from the .env file.
        loaders (dict): Dictionary mapping file extensions to their respective loader classes.
        file_paths (dict): Dictionary containing the paths of files to be processed.
    """

    def __init__(self, base_output_folder="output", config_file="config.env"):
        """
        Initializes the FileProcessor class by loading environment variables, setting up file loaders,
        and creating the necessary output directories.

        Args:
            base_output_folder (str): Directory where output files will be saved.
            config_file (str): The path to the configuration file for loading environment variables.
        """
        load_dotenv(config_file)  # Load environment variables from the config file.
        self.base_output_folder = base_output_folder
        # Load database credentials from environment variables.
        self.db_credentials = {
            'host': os.getenv("DB_HOST"),
            'user': os.getenv("DB_USER"),
            'password': os.getenv("DB_PASSWORD"),
            'database': os.getenv("DB_NAME")
        }
        # Initialize file loaders for PDF, DOCX, and PPTX files.
        self.loaders = {
            'pdf': PDFLoader(),
            'docx': DOCXLoader(),
            'pptx': PPTLoader()
        }
        # Set file paths for the files to be processed.
        self.file_paths = {
            'pdf': "test_files/pdf/small.pdf",
            'docx': "test_files/docx/small.docx",
            'pptx': "test_files/pptx/small.pptx"
        }
        # Ensure the base output directory exists.
        self.ensure_directory(self.base_output_folder)

    def ensure_directory(self, path):
        """
        Ensures that the given directory exists. If not, it creates the directory.

        Args:
            path (str): The directory path to be checked or created.
        """
        if not os.path.exists(path):
            os.makedirs(path)  # Create the directory if it does not exist.

    def save_to_file(self, data, filename):
        """
        Saves the extracted data to a JSON file.

        Args:
            data (dict): The extracted content to be saved.
            filename (str): The path where the JSON file will be saved.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)  # Save data as a JSON file.

    def process_file(self, loader, base_output_folder):
        """
        Processes a file using the specified loader by extracting text, links, images, and tables.
        The extracted data is saved in separate JSON files for each type of content.

        Args:
            loader (FileLoader): The loader responsible for loading and extracting content from the file.
            base_output_folder (str): The base directory where the output will be saved.
        """
        extractor = DataExtractor(loader)  # Initialize the DataExtractor with the loader.
        content_types = ['text', 'links', 'images', 'tables']  # Define the types of content to extract.
        extraction_methods = {
            'text': extractor.extract_text,
            'links': extractor.extract_links,
            'images': extractor.extract_images,
            'tables': extractor.extract_tables
        }
        
        for content in content_types:
            # Call the appropriate extraction method and get the data.
            data = extraction_methods[content]()
            file_type = loader.file_extension.lstrip('.')  # Get the file extension without the dot.
            output_folder = os.path.join(base_output_folder, content, file_type)  # Define the output folder path.
            self.ensure_directory(output_folder)  # Ensure the output directory exists.
            # Save the extracted data to a JSON file.
            self.save_to_file(data, os.path.join(output_folder, f"{file_type}_{content}.json"))

    def run(self):
        """
        Main function that runs the file processing logic. It connects to the database, loads each file,
        processes it using the appropriate loader, and extracts the required content.
        """
        storage = SQLStorage(**self.db_credentials)  # Initialize SQL storage with database credentials.
        if storage.connection.is_connected():
            print("Successfully connected to the MySQL database")
        else:
            print("Failed to connect to the MySQL database")

        # Process each file type (pdf, docx, pptx) using the respective loader.
        for file_type, loader in self.loaders.items():
            loader.filepath = self.file_paths[file_type]  # Set the file path for the loader.
            self.process_file(loader, self.base_output_folder)  # Process the file and extract its content.

if __name__ == "__main__":
    processor = FileProcessor()  # Create a FileProcessor instance.
    processor.run()  # Run the file processing.
