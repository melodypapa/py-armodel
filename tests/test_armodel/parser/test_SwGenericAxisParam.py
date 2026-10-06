"""
Reader tests for SwGenericAxisParam (Table 5.53, p.356).

The XML snippets use the XSD-valid element spellings from
``autosar/R23-11/xsd/AUTOSAR_00052.xsd`` (group SW-GENERIC-AXIS-PARAM,
complexType SW-GENERIC-AXIS-PARAM). SwGenericAxisParam has no standalone
dispatch — it is read through its aggregator SwAxisGeneric
(``getSwAxisGeneric``), which is reached from ``getSwAxisIndividual``.
"""

from armodel.models.M2.MSR.DataDictionary.Axis import SwAxisIndividual
from tests.test_armodel.parser._helpers import _snip


def _individual_snip(inner: str, attrs: str = ""):
    return _snip(inner, root_tag="SW-AXIS-INDIVIDUAL", attrs=attrs)


class TestSwGenericAxisParamReader:
    """Tests for getSwGenericAxisParam — field values via the SwAxisGeneric aggregator (Table 5.53)."""

    def test_read_param_type_ref_and_vfs(self, parser):
        """SW-GENERIC-AXIS-PARAM-TYPE-REF and VF children are read into the model fields."""
        element = _individual_snip(
            "<SW-AXIS-GENERIC>"
            "<SW-GENERIC-AXIS-PARAMS>"
            "<SW-GENERIC-AXIS-PARAM>"
            "<SW-GENERIC-AXIS-PARAM-TYPE-REF DEST='SW-GENERIC-AXIS-PARAM-TYPE'>/axis/types/fixed/shift</SW-GENERIC-AXIS-PARAM-TYPE-REF>"
            "<VF>1.5</VF>"
            "<VF>-2.25e-3</VF>"
            "</SW-GENERIC-AXIS-PARAM>"
            "</SW-GENERIC-AXIS-PARAMS>"
            "</SW-AXIS-GENERIC>"
        )
        props = parser.getSwAxisIndividual(element)

        generic = props.getSwAxisGeneric()
        assert generic is not None
        params = generic.getSwGenericAxisParams()
        assert len(params) == 1
        param = params[0]
        ref = param.getSwGenericAxisParamTypeRef()
        assert ref is not None
        assert ref.getValue() == "/axis/types/fixed/shift"
        assert ref.getDest() == "SW-GENERIC-AXIS-PARAM-TYPE"
        vfs = param.getVfs()
        assert len(vfs) == 2
        assert vfs[0].getValue() == 1.5
        assert vfs[1].getValue() == -0.00225

    def test_read_multiple_params_keep_order(self, parser):
        """Multiple SW-GENERIC-AXIS-PARAM instances are read in document order."""
        element = _individual_snip(
            "<SW-AXIS-GENERIC>"
            "<SW-GENERIC-AXIS-PARAMS>"
            "<SW-GENERIC-AXIS-PARAM>"
            "<SW-GENERIC-AXIS-PARAM-TYPE-REF DEST='SW-GENERIC-AXIS-PARAM-TYPE'>/axis/types/fixed/shift</SW-GENERIC-AXIS-PARAM-TYPE-REF>"
            "</SW-GENERIC-AXIS-PARAM>"
            "<SW-GENERIC-AXIS-PARAM>"
            "<VF>7</VF>"
            "</SW-GENERIC-AXIS-PARAM>"
            "</SW-GENERIC-AXIS-PARAMS>"
            "</SW-AXIS-GENERIC>"
        )
        props = parser.getSwAxisIndividual(element)

        params = props.getSwAxisGeneric().getSwGenericAxisParams()
        assert len(params) == 2
        assert params[0].getSwGenericAxisParamTypeRef().getValue() == "/axis/types/fixed/shift"
        assert params[0].getVfs() == []
        assert params[1].getSwGenericAxisParamTypeRef() is None
        assert params[1].getVfs()[0].getValue() == 7

    def test_read_empty_wrapper_yields_no_params(self, parser):
        """An empty SW-GENERIC-AXIS-PARAMS wrapper parses to an empty list."""
        element = _individual_snip("<SW-AXIS-GENERIC>" "<SW-GENERIC-AXIS-PARAMS></SW-GENERIC-AXIS-PARAMS>" "</SW-AXIS-GENERIC>")
        props = parser.getSwAxisIndividual(element)

        assert props.getSwAxisGeneric().getSwGenericAxisParams() == []

    def test_read_ar_object_attributes(self, parser):
        """The S/T attributes of the SW-GENERIC-AXIS-PARAM element (AR-OBJECT attributeGroup) round-trip into the model."""
        element = _individual_snip(
            "<SW-AXIS-GENERIC>"
            "<SW-GENERIC-AXIS-PARAMS>"
            '<SW-GENERIC-AXIS-PARAM S="1234" T="2024-01-01T00:00:00Z">'
            "<VF>3.5</VF>"
            "</SW-GENERIC-AXIS-PARAM>"
            "</SW-GENERIC-AXIS-PARAMS>"
            "</SW-AXIS-GENERIC>"
        )
        props = parser.getSwAxisIndividual(element)

        param = props.getSwAxisGeneric().getSwGenericAxisParams()[0]
        assert param.getChecksum().getValue() == "1234"
        assert param.getTimestamp().getValue() == "2024-01-01T00:00:00Z"
        assert param.getVfs()[0].getValue() == 3.5

    def test_read_defaults_without_generic_axis(self, parser):
        """An SW-AXIS-INDIVIDUAL without SW-AXIS-GENERIC leaves swAxisGeneric unset."""
        element = _individual_snip("<UNIT-REF DEST='UNIT'>/units/u</UNIT-REF>")
        props = parser.getSwAxisIndividual(element)

        assert isinstance(props, SwAxisIndividual)
        assert props.getSwAxisGeneric() is None
