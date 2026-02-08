"""Tests for format_xml_cli module."""

import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

from armodel.cli.format_xml_cli import main, patch_xml, perform_format


class TestPatchXml:
    """Tests for patch_xml function."""

    def test_patch_xml_self_closing_tag(self):
        """Test patching self-closing XML tags."""
        xml = '<root><item/></root>'
        result = patch_xml(xml)
        assert result == '<root><item></item></root>'

    def test_patch_xml_multiple_tags(self):
        """Test patching multiple self-closing tags."""
        xml = '<root><item1/><item2/><item3/></root>'
        result = patch_xml(xml)
        assert '<item1></item1>' in result
        assert '<item2></item2>' in result
        assert '<item3></item3>' in result

    def test_patch_xml_nested_tags(self):
        """Test patching nested self-closing tags."""
        xml = '<root><outer><inner/></outer></root>'
        result = patch_xml(xml)
        assert '<inner></inner>' in result

    def test_patch_xml_no_self_closing_tags(self):
        """Test patch_xml when there are no self-closing tags."""
        xml = '<root><item>content</item></root>'
        result = patch_xml(xml)
        assert result == xml


class TestPerformFormat:
    """Tests for perform_format function."""

    def test_perform_format_basic_xml(self, tmp_path):
        """Test formatting a basic XML file."""
        # Create input XML file
        input_file = tmp_path / "input.xml"
        input_file.write_text(
            '<?xml version="1.0" encoding="UTF-8"?><root><item>test</item></root>',
            encoding="utf-8"
        )

        # Create output file path
        output_file = tmp_path / "output.xml"

        # Create mock args
        args = MagicMock()
        args.INPUT = str(input_file)
        args.OUTPUT = str(output_file)

        # Run perform_format
        perform_format(args)

        # Check output file was created
        assert output_file.exists()
        content = output_file.read_text(encoding="utf-8")
        assert "<root>" in content
        assert "<item>test</item>" in content

    def test_perform_format_empty_lines_removed(self, tmp_path):
        """Test that empty lines are removed from output."""
        # Create input XML
        input_file = tmp_path / "input.xml"
        input_file.write_text(
            '<?xml version="1.0"?><root>\n\n<item>test</item>\n\n</root>',
            encoding="utf-8"
        )

        output_file = tmp_path / "output.xml"
        args = MagicMock()
        args.INPUT = str(input_file)
        args.OUTPUT = str(output_file)

        perform_format(args)

        content = output_file.read_text(encoding="utf-8")
        lines = content.splitlines()
        # Check that no consecutive empty lines exist
        for i in range(len(lines) - 1):
            assert not (lines[i].strip() == "" and lines[i + 1].strip() == "")


class TestMain:
    """Tests for main function."""

    @patch("armodel.cli.format_xml_cli.perform_format")
    @patch("argparse.ArgumentParser.parse_args")
    def test_main_basic_call(self, mock_parse_args, mock_perform_format):
        """Test main function basic call."""
        # Create mock args
        args = MagicMock()
        mock_parse_args.return_value = args

        # Call main (should not raise since perform_format is mocked)
        main()

        # Check that perform_format was called
        mock_perform_format.assert_called_once_with(args)

    @patch("sys.argv", ["format-xml", "input.xml", "output.xml"])
    @patch("armodel.cli.format_xml_cli.perform_format")
    def test_main_with_file_args(self, mock_perform_format):
        """Test main with actual file arguments."""
        # Create temporary files
        with tempfile.NamedTemporaryFile(mode="w", suffix=".xml", delete=False) as f:
            f.write('<?xml version="1.0"?><root></root>')
            input_file = f.name

        with tempfile.NamedTemporaryFile(mode="w", suffix=".xml", delete=False) as f:
            output_file = f.name

        try:
            main()
        except SystemExit:
            pass
        finally:
            # Cleanup
            Path(input_file).unlink(missing_ok=True)
            Path(output_file).unlink(missing_ok=True)
