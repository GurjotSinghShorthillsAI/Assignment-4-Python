from .file_loader import FileLoader
from docx import Document
import logging
import sys

class DOCXLoader(FileLoader):
    """
    Loader class for DOCX files, inheriting from the FileLoader abstract base class.
    Handles the specifics of validating and loading DOCX files.

    Attributes:
        file_extension (str): The file extension this loader handles, set to '.docx'.
    """

    file_extension = '.docx'

    def load_file(self, filepath: str):
        """
        Validates and loads a DOCX file. If the file is valid, it opens and returns a Document object
        for further manipulation. Errors during the opening of the file are caught and logged, and the
        process is terminated.

        Args:
            filepath (str): The path to the DOCX file that needs to be loaded.

        Returns:
            Document: A Document object from the python-docx library that represents the loaded DOCX file.

        Raises:
            SystemExit: If the DOCX file cannot be opened or read, the process will stop after logging the error.
        """
        if self.validate_file(filepath):  # Utilizes the validate_file method from the abstract base class.
            try:
                doc = Document(filepath)  # Attempts to open and read the DOCX file.
                print(f"Loaded DOCX file: {filepath}")
                return doc
            except Exception as e:
                logging.error(f"Unable to open or read the DOCX file: {e}")
                sys.exit(f"Stopping the process due to a critical error with the DOCX file: {filepath}")
