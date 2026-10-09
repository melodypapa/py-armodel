import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    IPdu,
    IPduTiming,
    ISignalIPdu,
    ISignalToIPduMapping,
)

CLASS_NOTE = "Represents the IPdus handled by Com. The ISignalIPdu assembled and disassembled in AUTOSAR COM consists of one or more signals. In case no multiplexing is performed this IPdu is routed to/from the Interface Layer. A maximum of one dynamic length signal per IPdu is allowed. Tags: atp.recommendedPackage=Pdus"
NOTES = {
    "iPduTimingSpecification": "Timing specification for Com IPdus (Transmission Modes). This information is mandatory for the sender in a System Extract. This information may be omitted on receivers in a System Extract. atpVariation: The timing of a Pdu can vary. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iPduTimingSpecification, iPduTiming Specification.variationPoint.shortLabel vh.latestBindingTime=postBuild",
    "iSignalToPduMapping": "Definition of SignalToIPduMappings included in the Signal IPdu. atpVariation: The content of a PDU can be variable. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=iSignalToPduMapping.shortName, iSignalTo PduMapping.variationPoint.shortLabel vh.latestBindingTime=postBuild",
    "unusedBitPattern": "AUTOSAR COM and AUTOSAR IPDUM are filling not used areas of an IPDU with this bit-pattern. This attribute is mandatory to avoid undefined behavior. This byte-pattern will be repeated throughout the IPdu.",
}


class TestISignalIPdu:
    """Test cases for ISignalIPdu (Table 6.19, p.342)."""

    def test_inheritance(self):
        assert issubclass(ISignalIPdu, IPdu)

    def test_initialization_defaults(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")
        assert ipdu.getShortName() == "ISignalIPdu1"
        assert ipdu.getIPduTimingSpecification() is None
        assert ipdu.getISignalToPduMappings() == []
        assert ipdu.getUnusedBitPattern() is None

    def test_get_set_ipdu_timing_specification(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")

        timing = IPduTiming()
        assert ipdu.setIPduTimingSpecification(timing) is ipdu
        assert ipdu.getIPduTimingSpecification() is timing
        ipdu.setIPduTimingSpecification(None)
        assert ipdu.getIPduTimingSpecification() is timing

    def test_create_isignal_to_pdu_mapping(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")

        mapping = ipdu.createISignalToPduMapping("mapping1")
        assert isinstance(mapping, ISignalToIPduMapping)
        assert ipdu.getISignalToPduMappings() == [mapping]
        assert ipdu.createISignalToPduMapping("mapping1") is mapping

    def test_get_set_unused_bit_pattern(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")

        pattern = Integer().setValue("255")
        assert ipdu.setUnusedBitPattern(pattern) is ipdu
        assert ipdu.getUnusedBitPattern() is pattern
        assert ipdu.getUnusedBitPattern().getValue() == 255
        ipdu.setUnusedBitPattern(None)
        assert ipdu.getUnusedBitPattern() is pattern

    def test_class_docstring_note(self):
        assert inspect.cleandoc(ISignalIPdu.__doc__) == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")
        pairs = (
            ("getIPduTimingSpecification", "setIPduTimingSpecification", "iPduTimingSpecification"),
            ("getISignalToPduMappings", "createISignalToPduMapping", "iSignalToPduMapping"),
            ("getUnusedBitPattern", "setUnusedBitPattern", "unusedBitPattern"),
        )
        for getter_name, mutator_name, key in pairs:
            getter = getattr(ipdu, getter_name)
            mutator = getattr(ipdu, mutator_name)
            assert inspect.cleandoc(getter.__doc__) == NOTES[key], key
            assert inspect.cleandoc(mutator.__doc__).split("\n")[0] == NOTES[key], key

    def test_init_has_no_docstring(self):
        assert ISignalIPdu.__init__.__doc__ is None
