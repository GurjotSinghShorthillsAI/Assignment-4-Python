from .file_loader import FileLoader
from pptx import Presentation

class PPTLoader(FileLoader):
    """
    Loader class for PPTX files, inheriting from the FileLoader abstract base class.
    Handles the specifics of validating and loading PowerPoint (PPTX) files.

    Attributes:
        file_extension (str): The file extension this loader handles, specifically set to '.pptx'.
    """

    file_extension = '.pptx'

    def process_file(self, filepath: str):
        """
        Loads a PPTX file after validation. If the file is valid, it opens and returns
        a Presentation object from the python-pptx library for further manipulation.

        Args:
            filepath (str): The path to the PPTX file that needs to be loaded.

        Returns:
            Presentation: A Presentation object representing the loaded PPTX file.

        Raises:
            SystemExit: If the PPTX file cannot be opened or read, logs the error and stops the process.
        """
        ppt = Presentation(filepath)  # Attempts to open and read the PPTX file.
        print(f"Loaded PPTX file: {filepath}")
        return ppt
