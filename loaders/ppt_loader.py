from pptx import Presentation
from loaders.file_loader import FileLoader
import logging
import sys  # Import sys for using sys.exit()

class PPTLoader(FileLoader):
    """
    Concrete implementation of FileLoader for handling PPTX files.
    """

    def validate_file(self, filepath):
        """
        Validates that the specified file path ends with '.pptx'.

        Args:
        filepath (str): The path to the file to validate.

        Raises:
        ValueError: If the file extension is not .pptx.
        """
        if not filepath.lower().endswith('.pptx'):
            logging.error(f"Invalid file format for PPT loader: {filepath}")
            sys.exit(f"Stopping the process due to invalid file format for PPT loader: {filepath}")

    def load_file(self, filepath):
        """
        Loads a PPTX file and returns a Presentation object.

        Args:
        filepath (str): The path to the file to load.

        Raises:
        IOError: If the file cannot be opened or read.
        """
        try:
            self.validate_file(filepath)
            ppt = Presentation(filepath)
            print(f"Loaded PPTX file: {filepath}")
            return ppt
        except Exception as e:
            logging.error(f"Unable to open or read the PPT file due to corruption or other issues: {e}")
            sys.exit(f"Stopping the process due to a critical error with the file: {filepath}")

