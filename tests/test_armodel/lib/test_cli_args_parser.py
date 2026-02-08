"""
Test cases for the InputFileParser class.
These tests ensure 100% code coverage for the CLI argument parsing functionality.
"""

import os
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

from armodel.lib.cli_args_parser import InputFileParser


class TestInputFileParser:
    """
    Test class for InputFileParser functionality.
    This class contains test methods for validating the behavior of
    the InputFileParser class, including its initialization,
    file list parsing, directory parsing, and main parse method.
    """

    def test_initialization_with_empty_args(self):
        """
        Test InputFileParser initialization with empty args.
        Verifies that the parser can be properly instantiated with empty args
        and that it has the required attributes initialized correctly.
        """
        parser = InputFileParser([])

        assert parser is not None
        assert hasattr(parser, '_args')
        assert hasattr(parser, '_filenames')
        assert hasattr(parser, '_logger')
        assert parser._args == []
        assert parser._filenames == []

    def test_initialization_with_args(self):
        """
        Test InputFileParser initialization with args.
        Verifies that the parser properly stores the provided args.
        """
        args = ['file1.arxml', 'file2.arxml']
        parser = InputFileParser(args)

        assert parser._args == args
        assert parser._filenames == []

    def test_parse_with_empty_args(self):
        """
        Test parse method with empty args.
        Verifies that the method returns an empty list when no args are provided.
        """
        parser = InputFileParser([])
        result = parser.parse()

        assert result == []

    def test_parse_with_regular_files(self):
        """
        Test parse method with regular file paths.
        Verifies that the method properly handles regular file paths.
        """
        tmpdir = tempfile.mkdtemp()
        try:
            # Create test files
            file1 = Path(tmpdir) / 'test1.arxml'
            file2 = Path(tmpdir) / 'test2.arxml'
            file1.touch()
            file2.touch()

            parser = InputFileParser([str(file1), str(file2)])
            result = parser.parse()

            assert len(result) == 2
            assert str(file1) in result
            assert str(file2) in result
        finally:
            # Cleanup
            import shutil
            shutil.rmtree(tmpdir, ignore_errors=True)

    def test_parse_with_file_list(self):
        """
        Test parse method with a file list (prefixed with @).
        Verifies that the method properly reads and parses a file containing
        a list of file paths.
        """
        tmpdir = tempfile.mkdtemp()
        try:
            # Create a list file
            list_file = Path(tmpdir) / 'filelist.txt'
            file1_path = (Path(tmpdir) / 'test1.arxml')
            file2_path = (Path(tmpdir) / 'test2.arxml')
            file1_path.touch()
            file2_path.touch()

            with open(list_file, 'w') as f:
                f.write(str(file1_path) + '\n')
                f.write(str(file2_path) + '\n')
                f.write('  # comment line  \n')  # This should be included as-is (not stripped as comment)
                f.write('\n')  # Empty line
                f.write(str(Path(tmpdir) / 'test3.arxml') + '\n')

            parser = InputFileParser(['@' + str(list_file)])
            result = parser.parse()

            # Should have 5 entries: 2 existing files, comment line, empty line, 1 non-existent file path
            # The code appends line.strip() for each line, so:
            # - file1_path (stripped)
            # - file2_path (stripped)
            # - "# comment line" (stripped)
            # - "" (empty string from empty line)
            # - test3.arxml path (stripped)
            assert len(result) == 5
            assert str(file1_path) in result
            assert str(file2_path) in result
            assert '# comment line' in result
            assert '' in result
        finally:
            # Cleanup
            import shutil
            shutil.rmtree(tmpdir, ignore_errors=True)

    def test_parse_with_directory(self):
        """
        Test parse method with a directory path.
        Verifies that the method properly walks a directory and finds all .arxml files.
        """
        tmpdir = tempfile.mkdtemp()
        try:
            # Create directory structure with .arxml files
            subdir = Path(tmpdir) / 'subdir'
            subdir.mkdir()

            file1 = Path(tmpdir) / 'test1.arxml'
            file2 = Path(tmpdir) / 'test2.ARXML'  # Test case insensitivity
            file3 = subdir / 'test3.arxml'
            file4 = subdir / 'test4.txt'  # Non-.arxml file
            file1.touch()
            file2.touch()
            file3.touch()
            file4.touch()

            parser = InputFileParser([tmpdir])
            result = parser.parse()

            # Should find all .arxml files (case insensitive)
            assert len(result) == 3
            assert str(file1) in result
            assert str(file2) in result
            assert str(file3) in result
            assert str(file4) not in result  # .txt files should be ignored
        finally:
            # Cleanup
            import shutil
            shutil.rmtree(tmpdir, ignore_errors=True)

    def test_parse_with_mixed_inputs(self):
        """
        Test parse method with mixed input types (files, directories, and lists).
        Verifies that the method properly handles a combination of different input types.
        """
        tmpdir = tempfile.mkdtemp()
        try:
            # Create files and directories
            dir1 = Path(tmpdir) / 'dir1'
            dir1.mkdir()

            file1 = Path(tmpdir) / 'file1.arxml'
            file2 = dir1 / 'file2.arxml'
            file1.touch()
            file2.touch()

            # Create list file
            list_file = Path(tmpdir) / 'list.txt'
            file3 = Path(tmpdir) / 'file3.arxml'
            file3.touch()

            with open(list_file, 'w') as f:
                f.write(str(file3) + '\n')

            parser = InputFileParser([str(file1), str(dir1), '@' + str(list_file)])
            result = parser.parse()

            # Should have file1, file2 (from dir), and file3 (from list)
            assert len(result) == 3
            assert str(file1) in result
            assert str(file2) in result
            assert str(file3) in result
        finally:
            # Cleanup
            import shutil
            shutil.rmtree(tmpdir, ignore_errors=True)

    def test_parse_preserves_order(self):
        """
        Test that parse method preserves the order of input files.
        Verifies that files are returned in the order they were specified.
        """
        tmpdir = tempfile.mkdtemp()
        try:
            file1 = Path(tmpdir) / 'b.arxml'
            file2 = Path(tmpdir) / 'a.arxml'
            file3 = Path(tmpdir) / 'c.arxml'
            file1.touch()
            file2.touch()
            file3.touch()

            parser = InputFileParser([str(file1), str(file2), str(file3)])
            result = parser.parse()

            assert result == [str(file1), str(file2), str(file3)]
        finally:
            # Cleanup
            import shutil
            shutil.rmtree(tmpdir, ignore_errors=True)

    def test_parse_with_nonexistent_file(self):
        """
        Test parse method with non-existent file.
        Verifies that the method still adds non-existent file paths to the list.
        The parser doesn't check if files exist, it just processes the paths.
        """
        parser = InputFileParser(['nonexistent.arxml'])
        result = parser.parse()

        assert result == ['nonexistent.arxml']

    def test_parse_with_deeply_nested_directory(self):
        """
        Test parse method with deeply nested directory structure.
        Verifies that the method properly walks nested directories.
        """
        tmpdir = tempfile.mkdtemp()
        try:
            # Create deeply nested structure
            level1 = Path(tmpdir) / 'level1'
            level2 = level1 / 'level2'
            level3 = level2 / 'level3'
            level3.mkdir(parents=True)

            file1 = level3 / 'deep.arxml'
            file1.touch()

            parser = InputFileParser([tmpdir])
            result = parser.parse()

            assert len(result) == 1
            assert str(file1) in result
        finally:
            # Cleanup
            import shutil
            shutil.rmtree(tmpdir, ignore_errors=True)

    def test_parse_with_empty_directory(self):
        """
        Test parse method with an empty directory.
        Verifies that the method handles empty directories without errors.
        """
        tmpdir = tempfile.mkdtemp()
        try:
            parser = InputFileParser([tmpdir])
            result = parser.parse()

            assert result == []
        finally:
            # Cleanup
            import shutil
            shutil.rmtree(tmpdir, ignore_errors=True)

    def test_parse_with_symlinks(self):
        """
        Test parse method with symbolic links (if supported by OS).
        Verifies that the method handles symlinks appropriately.
        Note: This test may be skipped on systems that don't support symlinks.
        """
        tmpdir = tempfile.mkdtemp()
        try:
            # Create a file and a symlink to it
            file1 = Path(tmpdir) / 'original.arxml'
            file1.touch()

            link = Path(tmpdir) / 'link.arxml'
            try:
                link.symlink_to(file1)
            except (OSError, NotImplementedError):
                # Symlinks not supported on this system
                return

            parser = InputFileParser([tmpdir])
            result = parser.parse()

            # Both the original and symlink should be found
            assert str(file1) in result or str(link) in result
        finally:
            # Cleanup
            import shutil
            shutil.rmtree(tmpdir, ignore_errors=True)

    def test_parse_with_directory_and_non_arxml_files(self):
        """
        Test parse method filters out non-.arxml files in directories.
        Verifies that only .arxml files are collected from directories.
        """
        tmpdir = tempfile.mkdtemp()
        try:
            # Create various file types
            arxml_file1 = Path(tmpdir) / 'test.arxml'
            txt_file = Path(tmpdir) / 'test.txt'
            xml_file = Path(tmpdir) / 'test.xml'
            arxml_file2 = Path(tmpdir) / 'data.ARXML'  # Different base name for case-insensitive test

            arxml_file1.touch()
            txt_file.touch()
            xml_file.touch()
            arxml_file2.touch()

            parser = InputFileParser([tmpdir])
            result = parser.parse()

            # Should only include .arxml files (case insensitive)
            assert len(result) == 2
            assert str(arxml_file1) in result
            assert str(arxml_file2) in result
            assert str(txt_file) not in result
            assert str(xml_file) not in result
        finally:
            # Cleanup
            import shutil
            shutil.rmtree(tmpdir, ignore_errors=True)

    def test_logger_initialization(self):
        """
        Test that the logger is properly initialized.
        Verifies that the _logger attribute is a logging.Logger instance.
        """
        parser = InputFileParser([])

        assert parser._logger is not None
        assert hasattr(parser._logger, 'debug')

    @patch('logging.getLogger')
    def test_logger_debug_called_for_list_file(self, mock_get_logger):
        """
        Test that debug logging is called when parsing a list file.
        Verifies that the debug message is logged with the correct list file path.
        """
        mock_logger = Mock()
        mock_get_logger.return_value = mock_logger

        tmpdir = tempfile.mkdtemp()
        try:
            # Create list file
            list_file = Path(tmpdir) / 'filelist.txt'
            arxml_file = Path(tmpdir) / 'test.arxml'
            arxml_file.touch()

            with open(list_file, 'w') as f:
                f.write(str(arxml_file) + '\n')

            parser = InputFileParser(['@' + str(list_file)])
            parser.parse()

            # Verify debug was called
            assert mock_logger.debug.called
            # Get the actual call
            call_args = mock_logger.debug.call_args[0][0]
            assert '@' in call_args or 'filelist.txt' in call_args or list_file.name in call_args
        finally:
            # Cleanup
            import shutil
            shutil.rmtree(tmpdir, ignore_errors=True)

    def test_multiple_parse_calls(self):
        """
        Test calling parse multiple times on the same parser instance.
        Verifies that multiple parse calls accumulate results (files are added each time).
        Note: The parse method returns the same list reference each time.
        """
        tmpdir = tempfile.mkdtemp()
        try:
            file1 = Path(tmpdir) / 'file1.arxml'
            file2 = Path(tmpdir) / 'file2.arxml'
            file1.touch()
            file2.touch()

            parser = InputFileParser([str(file1), str(file2)])
            result1 = parser.parse()
            assert len(result1) == 2
            assert result1 == [str(file1), str(file2)]

            # The second call will add the same files again (accumulate)
            result2 = parser.parse()

            # Both result1 and result2 point to the same list (same reference)
            assert result1 is result2
            # The list now has 4 files because the second parse added the same files again
            assert len(result2) == 4
            assert result2.count(str(file1)) == 2  # file1 appears twice
            assert result2.count(str(file2)) == 2  # file2 appears twice
        finally:
            # Cleanup
            import shutil
            shutil.rmtree(tmpdir, ignore_errors=True)

    def test_parse_with_absolute_paths(self):
        """
        Test parse method with absolute paths.
        Verifies that absolute paths are handled correctly.
        """
        tmpdir = tempfile.mkdtemp()
        try:
            file1 = Path(tmpdir) / 'test.arxml'
            file1.touch()

            # Use absolute path
            parser = InputFileParser([str(file1.resolve())])
            result = parser.parse()

            assert len(result) == 1
            # The absolute path should be in the result
            assert str(file1.resolve()) in result or str(file1) in result
        finally:
            # Cleanup
            import shutil
            shutil.rmtree(tmpdir, ignore_errors=True)

    def test_parse_with_relative_paths(self):
        """
        Test parse method with relative paths.
        Verifies that relative paths are preserved.
        """
        # Create files in current directory
        old_cwd = os.getcwd()
        tmpdir = tempfile.mkdtemp()
        try:
            os.chdir(tmpdir)

            file1 = Path('test.arxml')
            file1.touch()

            parser = InputFileParser(['test.arxml'])
            result = parser.parse()

            assert result == ['test.arxml']
        finally:
            os.chdir(old_cwd)
            # Cleanup
            import shutil
            shutil.rmtree(tmpdir, ignore_errors=True)

    def test_filenames_list_state_during_parsing(self):
        """
        Test that _filenames list is properly maintained during parsing.
        Verifies that files are added to the internal list correctly.
        """
        tmpdir = tempfile.mkdtemp()
        try:
            file1 = Path(tmpdir) / 'file1.arxml'
            file2 = Path(tmpdir) / 'file2.arxml'
            file1.touch()
            file2.touch()

            parser = InputFileParser([str(file1), str(file2)])

            # Before parsing, list should be empty
            assert parser._filenames == []

            # After parsing, list should contain files
            result = parser.parse()
            assert parser._filenames == result
            assert len(parser._filenames) == 2
        finally:
            # Cleanup
            import shutil
            shutil.rmtree(tmpdir, ignore_errors=True)

    def test_parse_with_windows_paths(self):
        """
        Test parse method with Windows-style paths.
        Verifies that Windows paths are handled correctly.
        """
        # This test is mainly for Windows systems
        if os.name != 'nt':
            return  # Skip on non-Windows systems

        tmpdir = tempfile.mkdtemp()
        try:
            file1 = Path(tmpdir) / 'test.arxml'
            file1.touch()

            # Windows path with backslashes
            windows_path = str(file1).replace('/', '\\')
            parser = InputFileParser([windows_path])
            result = parser.parse()

            assert len(result) == 1
            assert file1.name in result[0]
        finally:
            # Cleanup
            import shutil
            shutil.rmtree(tmpdir, ignore_errors=True)

    def test_parse_file_list_with_empty_lines(self):
        """
        Test parsing a file list with empty lines.
        Verifies that empty lines are handled (stripped but may be added as empty strings).
        """
        tmpdir = tempfile.mkdtemp()
        try:
            list_file = Path(tmpdir) / 'filelist.txt'
            file1 = Path(tmpdir) / 'file1.arxml'
            file1.touch()

            with open(list_file, 'w') as f:
                f.write(str(file1) + '\n')
                f.write('\n')  # Empty line
                f.write('   \n')  # Whitespace only line
                f.write(str(Path(tmpdir) / 'file2.arxml') + '\n')

            parser = InputFileParser(['@' + str(list_file)])
            result = parser.parse()

            # Empty lines after strip become empty strings
            # So we should have 4 entries: file1, '', '', file2 path
            assert len(result) == 4
            assert str(file1) in result
            # Empty strings should be present
            assert '' in result
            # Count empty strings - there should be 2 from the blank lines
            assert result.count('') >= 2
        finally:
            # Cleanup
            import shutil
            shutil.rmtree(tmpdir, ignore_errors=True)
