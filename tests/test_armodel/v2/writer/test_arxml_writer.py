"""
Unit tests for V2 ARXMLWriter.
"""
from armodel.v2.models.models import AUTOSAR, ARPackage
from armodel.v2.writer.base_writer import ARXMLWriter


class TestARXMLWriter:
    """Test ARXMLWriter class methods."""

    def test_save_arxml_with_single_package(self, tmp_path):
        """Test saving ARXML file with one AR-PACKAGE."""
        # Create test data
        document = AUTOSAR()
        pkg = ARPackage()
        pkg.short_name = "TestPackage"
        document.ar_packages.append(pkg)

        # Write to file
        output_file = tmp_path / "output.arxml"
        writer = ARXMLWriter()
        writer.save(str(output_file), document)

        # Verify file was created
        assert output_file.exists()

        # Verify content
        content = output_file.read_text()
        assert "<?xml version=" in content
        assert "<AUTOSAR" in content
        assert "<SHORT-NAME>TestPackage</SHORT-NAME>" in content

    def test_save_arxml_with_multiple_packages(self, tmp_path):
        """Test saving ARXML file with multiple AR-PACKAGEs."""
        # Create test data
        document = AUTOSAR()
        pkg1 = ARPackage()
        pkg1.short_name = "Package1"
        pkg2 = ARPackage()
        pkg2.short_name = "Package2"
        document.ar_packages.extend([pkg1, pkg2])

        # Write to file
        output_file = tmp_path / "output.arxml"
        writer = ARXMLWriter()
        writer.save(str(output_file), document)

        # Verify content
        content = output_file.read_text()
        assert "<SHORT-NAME>Package1</SHORT-NAME>" in content
        assert "<SHORT-NAME>Package2</SHORT-NAME>" in content

    def test_save_arxml_with_nested_packages(self, tmp_path):
        """Test saving ARXML file with nested AR-PACKAGEs."""
        # Create test data
        document = AUTOSAR()
        parent_pkg = ARPackage()
        parent_pkg.short_name = "ParentPackage"
        child_pkg = ARPackage()
        child_pkg.short_name = "ChildPackage"
        parent_pkg.ar_packages.append(child_pkg)
        document.ar_packages.append(parent_pkg)

        # Write to file
        output_file = tmp_path / "output.arxml"
        writer = ARXMLWriter()
        writer.save(str(output_file), document)

        # Verify content
        content = output_file.read_text()
        assert "<SHORT-NAME>ParentPackage</SHORT-NAME>" in content
        assert "<SHORT-NAME>ChildPackage</SHORT-NAME>" in content
