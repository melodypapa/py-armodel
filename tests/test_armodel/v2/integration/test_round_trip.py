"""
Integration tests for V2 ARXML reader and writer.
"""
from armodel.v2.models import AUTOSAR
from armodel.v2.reader.base_reader import ARXMLReader
from armodel.v2.writer.base_writer import ARXMLWriter


class TestRoundTrip:
    """Test round-trip parsing (read → write → read → compare)."""

    def test_round_trip_single_package(self, autosar_reset, tmp_path):
        """Test round-trip for single AR-PACKAGE."""
        # Create initial ARXML
        arxml_content = """<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/3.2.3">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>TestPackage</SHORT-NAME>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
"""
        input_file = tmp_path / "input.arxml"
        input_file.write_text(arxml_content)

        # Read
        document1 = AUTOSAR.getInstance()
        reader = ARXMLReader()
        reader.load(str(input_file), document1)

        # Write
        output_file = tmp_path / "output.arxml"
        writer = ARXMLWriter()
        writer.save(str(output_file), document1)

        # Reset and read again
        AUTOSAR.resetInstance()
        document2 = AUTOSAR.getInstance()
        reader.load(str(output_file), document2)

        # Compare
        assert len(document1.ar_package) == len(document2.ar_package)
        assert document1.ar_package[0].short_name == document2.ar_package[0].short_name

    def test_round_trip_multiple_packages(self, autosar_reset, tmp_path):
        """Test round-trip for multiple AR-PACKAGEs."""
        # Create initial ARXML
        arxml_content = """<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/3.2.3">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>Package1</SHORT-NAME>
    </AR-PACKAGE>
    <AR-PACKAGE>
      <SHORT-NAME>Package2</SHORT-NAME>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
"""
        input_file = tmp_path / "input.arxml"
        input_file.write_text(arxml_content)

        # Read
        document1 = AUTOSAR.getInstance()
        reader = ARXMLReader()
        reader.load(str(input_file), document1)

        # Write
        output_file = tmp_path / "output.arxml"
        writer = ARXMLWriter()
        writer.save(str(output_file), document1)

        # Reset and read again
        AUTOSAR.resetInstance()
        document2 = AUTOSAR.getInstance()
        reader.load(str(output_file), document2)

        # Compare
        assert len(document1.ar_package) == len(document2.ar_package)
        assert document1.ar_package[0].short_name == document2.ar_package[0].short_name
        assert document1.ar_package[1].short_name == document2.ar_package[1].short_name

    def test_round_trip_nested_packages(self, autosar_reset, tmp_path):
        """Test round-trip for nested AR-PACKAGEs."""
        # Create initial ARXML
        arxml_content = """<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/3.2.3">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>ParentPackage</SHORT-NAME>
      <AR-PACKAGES>
        <AR-PACKAGE>
          <SHORT-NAME>ChildPackage</SHORT-NAME>
        </AR-PACKAGE>
      </AR-PACKAGES>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
"""
        input_file = tmp_path / "input.arxml"
        input_file.write_text(arxml_content)

        # Read
        document1 = AUTOSAR.getInstance()
        reader = ARXMLReader()
        reader.load(str(input_file), document1)

        # Write
        output_file = tmp_path / "output.arxml"
        writer = ARXMLWriter()
        writer.save(str(output_file), document1)

        # Reset and read again
        AUTOSAR.resetInstance()
        document2 = AUTOSAR.getInstance()
        reader.load(str(output_file), document2)

        # Compare
        assert len(document1.ar_package) == len(document2.ar_package)
        parent1 = document1.ar_package[0]
        parent2 = document2.ar_package[0]
        assert parent1.short_name == parent2.short_name
        assert len(parent1.ar_package) == len(parent2.ar_package)
        assert parent1.ar_package[0].short_name == parent2.ar_package[0].short_name
