"""
Reader tests for E2EProfileCompatibilityProps (Table 4.93, p.202).

The XML snippets use the XSD-valid element spellings from
``autosar/R23-11/xsd/AUTOSAR_00052.xsd`` (group E-2-E-PROFILE-COMPATIBILITY-PROPS,
complexType E-2-E-PROFILE-COMPATIBILITY-PROPS). The dispatch entry is
readARPackageElementsRest -> readE2EProfileCompatibilityProps via the ARPackage
create factory (the class is aggregated by ARPackage.element).
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import E2EProfileCompatibilityProps
from tests.test_armodel.parser._helpers import _snip


class TestE2EProfileCompatibilityPropsReader:
    """Tests for readE2EProfileCompatibilityProps — own element field values (Table 4.93)."""

    def test_read_transit_to_invalid_extended_true(self, parser):
        """Test that TRANSIT-TO-INVALID-EXTENDED true is read into the model field."""
        package = AUTOSAR.getInstance().createARPackage("E2EProfileCompatibilityPropsCollection")
        element = _snip(
            "<SHORT-NAME>Props</SHORT-NAME>" "<TRANSIT-TO-INVALID-EXTENDED>true</TRANSIT-TO-INVALID-EXTENDED>",
            root_tag="E-2-E-PROFILE-COMPATIBILITY-PROPS",
        )
        parser.readARPackageElementsRest("E-2-E-PROFILE-COMPATIBILITY-PROPS", element, package)

        props = package.getReferrableElement("Props", E2EProfileCompatibilityProps)
        assert props is not None
        assert props.getShortName() == "Props"
        assert props.getTransitToInvalidExtended() is not None
        assert props.getTransitToInvalidExtended().getValue() is True

    def test_read_transit_to_invalid_extended_false(self, parser):
        """Test that TRANSIT-TO-INVALID-EXTENDED false is read (not skipped as missing)."""
        package = AUTOSAR.getInstance().createARPackage("E2EProfileCompatibilityPropsCollection")
        element = _snip(
            "<SHORT-NAME>Props</SHORT-NAME>" "<TRANSIT-TO-INVALID-EXTENDED>false</TRANSIT-TO-INVALID-EXTENDED>",
            root_tag="E-2-E-PROFILE-COMPATIBILITY-PROPS",
        )
        parser.readARPackageElementsRest("E-2-E-PROFILE-COMPATIBILITY-PROPS", element, package)

        props = package.getReferrableElement("Props", E2EProfileCompatibilityProps)
        assert props is not None
        assert props.getTransitToInvalidExtended() is not None
        assert props.getTransitToInvalidExtended().getValue() is False

    def test_read_empty_wrapper(self, parser):
        """Test that an empty wrapper (no children) parses leaving the field None."""
        package = AUTOSAR.getInstance().createARPackage("E2EProfileCompatibilityPropsCollection")
        element = _snip("<SHORT-NAME>Props</SHORT-NAME>", root_tag="E-2-E-PROFILE-COMPATIBILITY-PROPS")
        parser.readARPackageElementsRest("E-2-E-PROFILE-COMPATIBILITY-PROPS", element, package)

        props = package.getReferrableElement("Props", E2EProfileCompatibilityProps)
        assert props is not None
        assert props.getTransitToInvalidExtended() is None
