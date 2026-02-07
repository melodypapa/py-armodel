"""
Error classes for V2 ARXML reader/writer.
"""
from pathlib import Path
from typing import Optional


class ReadError(Exception):
    """Exception raised during ARXML reading (strict mode)."""

    def __init__(self, message: str, element_path: str = "",
                 line_number: Optional[int] = None,
                 file_path: Optional[Path] = None):
        self.message = message
        self.element_path = element_path
        self.line_number = line_number
        self.file_path = file_path

        # Build full error message
        full_message = message
        if element_path:
            full_message = f"{element_path}: {message}"
        if line_number:
            full_message = f"Line {line_number}: {full_message}"
        if file_path:
            full_message = f"{file_path}: {full_message}"

        super().__init__(full_message)
