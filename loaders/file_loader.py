from abc import ABC, abstractmethod
import sys
import logging

class FileLoader(ABC):
    """
    Abstract base class for file loaders. Implements common file validation logic and
    requires subclasses to define specific file loading behaviors.

    Attributes:
        file_extension (str): Expected file extension, set by subclasses.
    """

    file_extension = ""

    def validate_file(self, filepath: str) -> bool:
        """
        Validates that the file has the correct extension, stopping the process if invalid.

        Args:
            filepath (str): The file path to validate.

        Returns:
            bool: True if the file is valid.

        Raises:
            SystemExit: If the file extension is incorrect, logs the error and exits.
        """
        if not filepath.lower().endswith(self.file_extension):
            logging.error(f"Invalid file format: {filepath}")
            sys.exit(f"Invalid format stopped process: {filepath}")
        print(f"File validated: {filepath}")
        return True

    @abstractmethod
    def load_file(self, filepath: str):
        """
        Loads the file and returns its content. Must be implemented by subclasses.

        Args:
            filepath (str): The file path to load.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError("Load method not implemented.")


    @abstractmethod
    def load_file(self, filepath: str):
        pass
