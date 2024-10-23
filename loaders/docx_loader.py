from .file_loader import FileLoader
from docx import Document

class DOCXLoader(FileLoader):
    """
    Loader class for DOCX files, inheriting from the FileLoader abstract base class.
    Handles the specifics of validating and loading DOCX files.

    Attributes:
        file_extension (str): The file extension this loader handles, set to '.docx'.
    """

    file_extension = '.docx'

    def process_file(self, filepath: str):
        """
        Loads a DOCX file after validation. If the file is valid, it opens and returns
        a Document object from the python-docx library.

        Args:
            filepath (str): The path to the DOCX file that needs to be loaded.

        Returns:
            Document: A Document object representing the loaded DOCX file.

        Raises:
            SystemExit: If the DOCX file cannot be opened or read, logs the error and stops the process.
        """
        doc = Document(filepath)  # Attempts to open and read the DOCX file.
        print(f"Loaded DOCX file: {filepath}")
        return doc
