"""
Reader tests for SwCalprmRefProxy (Table 5.56, p.370).

The XML snippets use the XSD-valid element spellings from
``autosar/R23-11/xsd/AUTOSAR_00052.xsd`` (group SW-CALPRM-REF-PROXY: AR-PARAMETER
typed AUTOSAR-PARAMETER-REF, then MC-DATA-INSTANCE-REF). The group is inlined into
its aggregators — SW-AXIS-GROUPED (complexType, L114488) and SW-DATA-DEPENDENCY-ARGS
(L115767) — it has NO wrapper element of its own; the assertions go through
``getSwAxisGrouped``.
"""

from tests.test_armodel.parser._helpers import _snip


def _grouped_snip(inner: str):
    return _snip(inner, root_tag="SW-AXIS-GROUPED")


class TestSwCalprmRefProxyReader:
    """Tests for the inlined SW-CALPRM-REF-PROXY group members via getSwAxisGrouped (Table 5.56)."""

    def test_read_ar_parameter_and_mc_data_instance_ref(self, parser):
        """AR-PARAMETER and MC-DATA-INSTANCE-REF are read into one SwCalprmRefProxy's field values."""
        element = _grouped_snip(
            "<SHARED-AXIS-TYPE-REF DEST='SW-AXIS-TYPE'>/axis/types/shared</SHARED-AXIS-TYPE-REF>"
            "<AR-PARAMETER>"
            "<LOCAL-PARAMETER-REF DEST='PARAMETER-DATA-PROTOTYPE'>/params/shift</LOCAL-PARAMETER-REF>"
            "</AR-PARAMETER>"
            "<MC-DATA-INSTANCE-REF DEST='MC-DATA-INSTANCE'>/mc/instances/axis1</MC-DATA-INSTANCE-REF>"
        )
        props = parser.getSwAxisGrouped(element)

        proxy = props.getSwCalprmRef()
        assert proxy is not None
        ar_parameter = proxy.getArParameter()
        assert ar_parameter is not None
        local_ref = ar_parameter.getLocalParameterRef()
        assert local_ref is not None
        assert local_ref.getValue() == "/params/shift"
        assert local_ref.getDest() == "PARAMETER-DATA-PROTOTYPE"
        mc_ref = proxy.getMcDataInstanceRef()
        assert mc_ref is not None
        assert mc_ref.getValue() == "/mc/instances/axis1"
        assert mc_ref.getDest() == "MC-DATA-INSTANCE"

    def test_read_mc_data_instance_ref_only(self, parser):
        """A proxy with only MC-DATA-INSTANCE-REF leaves arParameter unset."""
        element = _grouped_snip("<MC-DATA-INSTANCE-REF DEST='MC-DATA-INSTANCE'>/mc/instances/axis1</MC-DATA-INSTANCE-REF>")
        props = parser.getSwAxisGrouped(element)

        proxy = props.getSwCalprmRef()
        assert proxy is not None
        assert proxy.getArParameter() is None
        assert proxy.getMcDataInstanceRef().getValue() == "/mc/instances/axis1"

    def test_read_ar_parameter_only(self, parser):
        """A proxy with only AR-PARAMETER leaves mcDataInstanceRef unset."""
        element = _grouped_snip(
            "<AR-PARAMETER>"
            "<AUTOSAR-PARAMETER-IREF>"
            "<PORT-PROTOTYPE-REF DEST='PROVIDED-PORT-PROTOTYPE'>/swc/ports/p1</PORT-PROTOTYPE-REF>"
            "<TARGET-DATA-PROTOTYPE-REF DEST='PARAMETER-DATA-PROTOTYPE'>/params/shift</TARGET-DATA-PROTOTYPE-REF>"
            "</AUTOSAR-PARAMETER-IREF>"
            "</AR-PARAMETER>"
        )
        props = parser.getSwAxisGrouped(element)

        proxy = props.getSwCalprmRef()
        assert proxy is not None
        iref = proxy.getArParameter().getAutosarParameterIRef()
        assert iref is not None
        assert iref.getPortPrototypeRef().getValue() == "/swc/ports/p1"
        assert iref.getTargetDataPrototypeRef().getValue() == "/params/shift"
        assert proxy.getMcDataInstanceRef() is None

    def test_read_without_proxy_members_leaves_sw_calprm_ref_none(self, parser):
        """SW-AXIS-GROUPED without either group member leaves swCalprmRef unset (no empty proxy)."""
        element = _grouped_snip("<SHARED-AXIS-TYPE-REF DEST='SW-AXIS-TYPE'>/axis/types/shared</SHARED-AXIS-TYPE-REF>" "<SW-AXIS-INDEX>1</SW-AXIS-INDEX>")
        props = parser.getSwAxisGrouped(element)

        assert props.getSwCalprmRef() is None
