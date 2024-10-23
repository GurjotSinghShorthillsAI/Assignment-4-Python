from abc import ABC, abstractmethod
import sys
import logging

class FileLoader(ABC):
    """
    Abstract base class for file loaders. This class provides common file validation logic
    and requires subclasses to implement specific file loading behaviors.

    Attributes:
        file_extension (str): Expected file extension, which is set by subclasses to match
                              the file type they are designed to handle.
    """

    file_extension = ""  # This will be set by subclasses to specify the required file extension.

    def validate_file(self, filepath: str) -> bool:
        """
        Validates that the provided file has the correct extension. This method is used to
        ensure that only files with the correct format are processed.

        Args:
            filepath (str): The full path of the file to be validated.

        Returns:
            bool: True if the file has the correct extension.

        Raises:
            SystemExit: If the file does not have the expected extension, logs an error and exits the program.
        """
        if not filepath.lower().endswith(self.file_extension):
            # Log error if the file extension is not as expected and terminate the program.
            logging.error(f"Invalid file format: {filepath}")
            sys.exit(f"Invalid format stopped process: {filepath}")
        # Log success if the file is valid and return True.
        print(f"File validated: {filepath}")
        return True

    def load_file(self, filepath: str):
        """
        Loads the file and processes its content by calling the `process_file` method, which is
        defined by subclasses. This method first validates the file extension.

        Args:
            filepath (str): The full path of the file to load.

        Returns:
            The processed content of the file (as defined by the subclass).

        Raises:
            SystemExit: If the file validation fails or an error occurs during file processing, 
                        logs the error and exits the program.
        """
        # Validate the file before proceeding with loading.
        if not self.validate_file(filepath):
            logging.error(f"File validation failed for: {filepath}")
            sys.exit("File validation failed")

        try:
            # Process the file using the subclass implementation.
            return self.process_file(filepath)
        except Exception as e:
            # Log any errors that occur during file processing and terminate the program.
            logging.error(f"Error loading file: {e}")
            sys.exit(f"Error during file loading stopped process: {filepath}")

    @abstractmethod
    def process_file(self, filepath):
        """
        Abstract method to process the file. This must be implemented by subclasses to
        handle specific file types, such as PDF, DOCX, or PPT.

        Args:
            filepath (str): The full path of the file to process.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError("The process_file method must be implemented by subclasses.")
