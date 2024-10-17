from .file_loader import FileLoader
from PyPDF2 import PdfReader
import sys

class PDFLoader(FileLoader):
    """
    Loader class for PDF files, inheriting from the FileLoader abstract base class.
    Handles the specifics of validating and loading PDF files.

    Attributes:
        file_extension (str): The file extension this loader handles, set to '.pdf'.
    """

    file_extension = '.pdf'

    def load_file(self, filepath: str):
        """
        Validates and loads a PDF file. If the file is valid, it opens and returns a PdfReader object
        for further manipulation. If there are issues opening the file, the process is terminated.

        Args:
            filepath (str): The path to the PDF file that needs to be loaded.

        Returns:
            PdfReader: A PdfReader object from the PyPDF2 library that represents the loaded PDF file.

        Raises:
            SystemExit: If the PDF file cannot be opened or read due to corruption or other issues, the process
                        will stop after logging the error.
        """
        if self.validate_file(filepath):  # Utilizes the validate_file method from the abstract base class.
            try:
                reader = PdfReader(filepath)  # Attempts to open and read the PDF file.
                print(f"Loaded PDF file: {filepath}")
                return reader
            except Exception:
                sys.exit(f"Unable to open or read the PDF file due to corruption or other issues")
