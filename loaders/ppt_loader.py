from .file_loader import FileLoader
from pptx import Presentation
import logging
import sys

class PPTLoader(FileLoader):
    """
    Loader class for PPTX files, inheriting from the FileLoader abstract base class.
    Handles the specifics of validating and loading PowerPoint (PPTX) files.

    Attributes:
        file_extension (str): The file extension this loader handles, specifically set to '.pptx'.
    """

    file_extension = '.pptx'

    def load_file(self, filepath: str):
        """
        Validates and loads a PPTX file. If the file is valid, it opens and returns a Presentation object
        for further manipulation. Errors during the file opening are caught and logged, leading to termination
        of the process.

        Args:
            filepath (str): The path to the PPTX file that needs to be loaded.

        Returns:
            Presentation: A Presentation object from the python-pptx library that represents the loaded PPTX file.

        Raises:
            SystemExit: If the PPTX file cannot be opened or read, the process will stop after logging the error.
        """
        if self.validate_file(filepath):  # Utilizes the inherited validate_file method to check file extension.
            try:
                ppt = Presentation(filepath)  # Attempts to open and read the PPTX file.
                print(f"Loaded PPTX file: {filepath}")
                return ppt
            except Exception as e:
                logging.error(f"Unable to open or read the PPT file: {e}")
                sys.exit(f"Stopping the process due to a critical error with the PPT file: {filepath}")
