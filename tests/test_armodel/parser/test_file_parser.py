"""Tests for file_parser module."""



from armodel.parser.file_parser import FileListParser


class TestFileListParserInit:
    """Tests for FileListParser initialization."""

    def test_init_creates_empty_list(self):
        """Test that FileListParser starts with empty file list."""
        parser = FileListParser()
        assert parser.get_file_list() == []

    def test_init_creates_logger(self):
        """Test that FileListParser creates a logger."""
        parser = FileListParser()
        assert parser.logger is not None


class TestParseTextFile:
    """Tests for parse_text_file method."""

    def test_parse_text_file_with_content(self, tmp_path):
        """Test parsing a text file with file paths."""
        # Create a text file with paths
        text_file = tmp_path / "file_list.txt"
        text_file.write_text(
            "file1.arxml\nfile2.arxml\nfile3.arxml",
            encoding="utf-8"
        )

        parser = FileListParser()
        parser.parse_text_file(str(text_file))

        assert parser.get_file_list() == ["file1.arxml", "file2.arxml", "file3.arxml"]

    def test_parse_text_file_ignores_comments(self, tmp_path):
        """Test that lines starting with # are ignored."""
        text_file = tmp_path / "file_list.txt"
        text_file.write_text(
            "# This is a comment\nfile1.arxml\n# Another comment\nfile2.arxml",
            encoding="utf-8"
        )

        parser = FileListParser()
        parser.parse_text_file(str(text_file))

        assert parser.get_file_list() == ["file1.arxml", "file2.arxml"]

    def test_parse_text_file_with_whitespace(self, tmp_path):
        """Test that leading/trailing whitespace is stripped."""
        text_file = tmp_path / "file_list.txt"
        text_file.write_text(
            "  file1.arxml  \n\tfile2.arxml\t\nfile3.arxml",
            encoding="utf-8"
        )

        parser = FileListParser()
        parser.parse_text_file(str(text_file))

        assert parser.get_file_list() == ["file1.arxml", "file2.arxml", "file3.arxml"]

    def test_parse_text_file_nonexistent(self, tmp_path, caplog):
        """Test parsing a non-existent file."""
        parser = FileListParser()
        parser.parse_text_file("nonexistent.txt")

        # Should log an error but not crash
        assert parser.get_file_list() == []


class TestParseDirFiles:
    """Tests for parse_dir_files method."""

    def test_parse_dir_finds_arxml_files(self, tmp_path):
        """Test that parse_dir_files finds .arxml files."""
        # Create test directory with ARXML files
        test_dir = tmp_path / "test_dir"
        test_dir.mkdir()

        (test_dir / "file1.arxml").write_text("<root></root>")
        (test_dir / "file2.arxml").write_text("<root></root>")
        (test_dir / "readme.txt").write_text("not an arxml")
        (test_dir / "script.py").write_text("print('test')")

        parser = FileListParser()
        parser.parse_dir_files(str(test_dir))

        file_list = parser.get_file_list()
        assert len(file_list) == 2
        assert any("file1.arxml" in f for f in file_list)
        assert any("file2.arxml" in f for f in file_list)

    def test_parse_dir_recursive(self, tmp_path):
        """Test that parse_dir_files searches recursively."""
        test_dir = tmp_path / "test_dir"
        test_dir.mkdir()
        (test_dir / "top.arxml").write_text("<root></root>")

        subdir = test_dir / "subdir"
        subdir.mkdir()
        (subdir / "nested.arxml").write_text("<root></root>")

        parser = FileListParser()
        parser.parse_dir_files(str(test_dir))

        file_list = parser.get_file_list()
        assert len(file_list) == 2
        assert any("top.arxml" in f for f in file_list)
        assert any("nested.arxml" in f for f in file_list)

    def test_parse_dir_case_insensitive(self, tmp_path):
        """Test that .ARXML (uppercase) is also matched."""
        test_dir = tmp_path / "test_dir"
        test_dir.mkdir()

        (test_dir / "lower.arxml").write_text("<root></root>")
        (test_dir / "UPPER.ARXML").write_text("<root></root>")
        (test_dir / "Mixed.ArXml").write_text("<root></root>")

        parser = FileListParser()
        parser.parse_dir_files(str(test_dir))

        file_list = parser.get_file_list()
        assert len(file_list) == 3

    def test_parse_dir_empty_directory(self, tmp_path):
        """Test parsing an empty directory."""
        test_dir = tmp_path / "empty_dir"
        test_dir.mkdir()

        parser = FileListParser()
        parser.parse_dir_files(str(test_dir))

        assert parser.get_file_list() == []

    def test_parse_dir_nonexistent(self, tmp_path):
        """Test parsing a non-existent directory."""
        parser = FileListParser()
        # Should handle gracefully (os.walk on non-existent dir yields nothing)
        parser.parse_dir_files(str(tmp_path / "nonexistent"))
        assert parser.get_file_list() == []


class TestParse:
    """Tests for parse method."""

    def test_parse_with_single_file(self, tmp_path):
        """Test parsing a single file path."""
        arxml_file = tmp_path / "test.arxml"
        arxml_file.write_text("<root></root>")

        parser = FileListParser()
        parser.parse([str(arxml_file)])

        assert parser.get_file_list() == [str(arxml_file)]

    def test_parse_with_multiple_files(self, tmp_path):
        """Test parsing multiple file paths."""
        file1 = tmp_path / "file1.arxml"
        file2 = tmp_path / "file2.arxml"
        file1.write_text("<root></root>")
        file2.write_text("<root></root>")

        parser = FileListParser()
        parser.parse([str(file1), str(file2)])

        file_list = parser.get_file_list()
        assert len(file_list) == 2
        assert str(file1) in file_list
        assert str(file2) in file_list

    def test_parse_with_directory(self, tmp_path):
        """Test parsing a directory path."""
        test_dir = tmp_path / "test_dir"
        test_dir.mkdir()
        (test_dir / "test.arxml").write_text("<root></root>")

        parser = FileListParser()
        parser.parse([str(test_dir)])

        file_list = parser.get_file_list()
        assert len(file_list) == 1
        assert any("test.arxml" in f for f in file_list)

    def test_parse_with_list_file(self, tmp_path):
        """Test parsing a list file (@ prefix)."""
        list_file = tmp_path / "list.txt"
        list_file.write_text("file1.arxml\nfile2.arxml")

        arxml1 = tmp_path / "file1.arxml"
        arxml2 = tmp_path / "file2.arxml"
        arxml1.write_text("<root></root>")
        arxml2.write_text("<root></root>")

        parser = FileListParser()
        parser.parse(["@" + str(list_file)])

        file_list = parser.get_file_list()
        assert len(file_list) == 2
        assert "file1.arxml" in file_list
        assert "file2.arxml" in file_list

    def test_parse_mixed_inputs(self, tmp_path):
        """Test parsing a mix of files, directories, and list files."""
        # Create individual file
        single_file = tmp_path / "single.arxml"
        single_file.write_text("<root></root>")

        # Create directory with file
        test_dir = tmp_path / "test_dir"
        test_dir.mkdir()
        (test_dir / "dir_file.arxml").write_text("<root></root>")

        # Create list file
        list_file = tmp_path / "list.txt"
        list_file.write_text("listed.arxml")
        (tmp_path / "listed.arxml").write_text("<root></root>")

        parser = FileListParser()
        parser.parse([str(single_file), str(test_dir), "@" + str(list_file)])

        file_list = parser.get_file_list()
        assert len(file_list) == 3
        assert any("single.arxml" in f for f in file_list)
        assert any("dir_file.arxml" in f for f in file_list)
        assert any("listed.arxml" in f for f in file_list)

    def test_parse_empty_list(self):
        """Test parsing with empty input list."""
        parser = FileListParser()
        parser.parse([])
        assert parser.get_file_list() == []

    def test_parse_accumulates(self, tmp_path):
        """Test that multiple parse calls accumulate results."""
        file1 = tmp_path / "file1.arxml"
        file2 = tmp_path / "file2.arxml"
        file1.write_text("<root></root>")
        file2.write_text("<root></root>")

        parser = FileListParser()
        parser.parse([str(file1)])
        parser.parse([str(file2)])

        file_list = parser.get_file_list()
        assert len(file_list) == 2
