from abc import ABC, abstractmethod

class FileLoader(ABC):
    """
    Abstract base class for file loaders. This class serves as a template for 
    file-type specific loaders like PDF, DOCX, and PPT. Each subclass must implement
    the methods to validate and load files according to their specific formats.
    """

    @abstractmethod
    def validate_file(self, filepath: str) -> bool:
        """
        Validates the file to ensure it is of a correct format.

        Args:
        filepath (str): The path to the file that needs validation.

        Returns:
        bool: True if the file is valid, False otherwise.
        """
        pass

    @abstractmethod
    def load_file(self, filepath: str):
        """
        Loads the file and returns its contents for further processing.

        Args:
        filepath (str): The path to the file that needs to be loaded.

        Returns:
        object: The loaded file content, the specific type depends on the file format.
        """
        pass
