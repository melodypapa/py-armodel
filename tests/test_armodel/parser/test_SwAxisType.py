"""
Reader tests for SwAxisType (Table 5.52, p.356).

The XML snippets use the XSD-valid element spellings from
``autosar/R23-11/xsd/AUTOSAR_00052.xsd`` (group SW-AXIS-TYPE,
complexType SW-AXIS-TYPE). The dispatch entry is
readARPackageElementsRest -> readSwAxisType via the ARPackage
create factory (the class is aggregated by ARPackage.element).
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.MSR.DataDictionary.Axis import SwAxisType
from tests.test_armodel.parser._helpers import _snip


class TestSwAxisTypeReader:
    """Tests for readSwAxisType — own element field values (Table 5.52)."""

    def test_read_sw_generic_axis_desc(self, parser):
        """Test that SW-GENERIC-AXIS-DESC is read into the model field."""
        package = AUTOSAR.getInstance().createARPackage("SwAxisTypes")
        element = _snip(
            "<SHORT-NAME>Axis</SHORT-NAME>" '<SW-GENERIC-AXIS-DESC><P><L-1 L="FOR-ALL">desc text</L-1></P></SW-GENERIC-AXIS-DESC>',
            root_tag="SW-AXIS-TYPE",
        )
        parser.readARPackageElementsRest("SW-AXIS-TYPE", element, package)

        axis_type = package.getReferrableElement("Axis", SwAxisType)
        assert axis_type is not None
        assert axis_type.getShortName() == "Axis"
        desc = axis_type.getSwGenericAxisDesc()
        assert desc is not None
        assert len(desc.getPs()) == 1

    def test_read_sw_generic_axis_param_types(self, parser):
        """Test that the SW-GENERIC-AXIS-PARAM-TYPES wrapper children are read as Referrable children."""
        package = AUTOSAR.getInstance().createARPackage("SwAxisTypes")
        element = _snip(
            "<SHORT-NAME>Axis</SHORT-NAME>"
            "<SW-GENERIC-AXIS-PARAM-TYPES>"
            "<SW-GENERIC-AXIS-PARAM-TYPE><SHORT-NAME>ParamA</SHORT-NAME></SW-GENERIC-AXIS-PARAM-TYPE>"
            "<SW-GENERIC-AXIS-PARAM-TYPE><SHORT-NAME>ParamB</SHORT-NAME></SW-GENERIC-AXIS-PARAM-TYPE>"
            "</SW-GENERIC-AXIS-PARAM-TYPES>",
            root_tag="SW-AXIS-TYPE",
        )
        parser.readARPackageElementsRest("SW-AXIS-TYPE", element, package)

        axis_type = package.getReferrableElement("Axis", SwAxisType)
        assert axis_type is not None
        param_types = axis_type.getSwGenericAxisParamTypes()
        assert [pt.getShortName() for pt in param_types] == ["ParamA", "ParamB"]

    def test_read_empty_wrapper(self, parser):
        """Test that an empty element (no children) parses leaving the fields empty."""
        package = AUTOSAR.getInstance().createARPackage("SwAxisTypes")
        element = _snip("<SHORT-NAME>Axis</SHORT-NAME>", root_tag="SW-AXIS-TYPE")
        parser.readARPackageElementsRest("SW-AXIS-TYPE", element, package)

        axis_type = package.getReferrableElement("Axis", SwAxisType)
        assert axis_type is not None
        assert axis_type.getSwGenericAxisDesc() is None
        assert axis_type.getSwGenericAxisParamTypes() == []
