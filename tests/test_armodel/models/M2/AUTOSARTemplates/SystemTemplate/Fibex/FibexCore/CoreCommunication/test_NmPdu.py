import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ISignalToIPduMapping,
    NmPdu,
    Pdu,
)

CLASS_NOTE = "Network Management Pdu Tags: atp.recommendedPackage=Pdus"
CLASS_CONSTRAINTS = (
    "[constr_5385] Reception of UserData inside of a NmPdu by Applications is not supported: A SystemSignal that is referenced by an ISignal that in turn is mapped via an ISignalToIPduMapping into a NmPdu shall not be mapped by a DataMapping that references a RPortPrototype with the contextPort reference in the VariableDataPrototypeInSystemInstanceRef that the DataMapping aggregates.",
    "[constr_3073] nmVoteInformation only valid for FrNm: The nmVoteInformation attribute is only valid for FrNm.",
)
NOTES = {
    "iSignalToIPduMapping": "This optional aggregation is used to describe NmUser Data that is transmitted in the NmPdu. The counting of the startPosition starts at the beginning of the NmPdu regardless whether Cbv or Nid are used.",
    "nmDataInformation": "Defines if the Pdu contains NM Data. If the NmPdu does not aggregate any ISignalToIPduMappings it still may contain UserData that is set via Nm_SetUserData(). If the ISignalToIPduMapping exists then the nmDataInformation attribute shall be ignored.",
    "nmVoteInformation": "Defines if the Pdu contains NM Vote information.",
    "unusedBitPattern": "AUTOSAR COM is filling not used areas of an Pdu with this bit-pattern. This attribute can only be used if the nm DataInformation attribute is set to true.",
}


class TestNmPdu:
    """Test cases for NmPdu (Table 6.20, p.343)."""

    def test_inheritance(self):
        assert issubclass(NmPdu, Pdu)

    def test_initialization_defaults(self):
        pdu = NmPdu(None, "NmPdu1")
        assert pdu.getShortName() == "NmPdu1"
        assert pdu.getISignalToIPduMappings() == []
        assert pdu.getNmDataInformation() is None
        assert pdu.getNmVoteInformation() is None
        assert pdu.getUnusedBitPattern() is None

    def test_create_isignal_to_ipdu_mapping(self):
        pdu = NmPdu(None, "NmPdu1")

        mapping = pdu.createISignalToIPduMapping("mapping1")
        assert isinstance(mapping, ISignalToIPduMapping)
        assert pdu.getISignalToIPduMappings() == [mapping]
        assert pdu.createISignalToIPduMapping("mapping1") is mapping

    def test_get_set_nm_data_information(self):
        pdu = NmPdu(None, "NmPdu1")

        value = Boolean()
        value.setValue(True)
        assert pdu.setNmDataInformation(value) is pdu
        assert pdu.getNmDataInformation() is value
        assert pdu.getNmDataInformation().getValue() is True
        pdu.setNmDataInformation(None)
        assert pdu.getNmDataInformation() is value

    def test_get_set_nm_vote_information(self):
        pdu = NmPdu(None, "NmPdu1")

        value = Boolean()
        value.setValue(False)
        assert pdu.setNmVoteInformation(value) is pdu
        assert pdu.getNmVoteInformation() is value
        assert pdu.getNmVoteInformation().getValue() is False
        pdu.setNmVoteInformation(None)
        assert pdu.getNmVoteInformation() is value

    def test_get_set_unused_bit_pattern(self):
        pdu = NmPdu(None, "NmPdu1")

        pattern = Integer().setValue("255")
        assert pdu.setUnusedBitPattern(pattern) is pdu
        assert pdu.getUnusedBitPattern() is pattern
        assert pdu.getUnusedBitPattern().getValue() == 255
        pdu.setUnusedBitPattern(None)
        assert pdu.getUnusedBitPattern() is pattern

    def test_class_docstring_note(self):
        assert inspect.cleandoc(NmPdu.__doc__) == CLASS_NOTE + "\n\n" + "\n".join(CLASS_CONSTRAINTS)

    def test_accessor_docstrings_verbatim(self):
        pdu = NmPdu(None, "NmPdu1")
        pairs = (
            ("createISignalToIPduMapping", "getISignalToIPduMappings", "iSignalToIPduMapping"),
            ("setNmDataInformation", "getNmDataInformation", "nmDataInformation"),
            ("setNmVoteInformation", "getNmVoteInformation", "nmVoteInformation"),
            ("setUnusedBitPattern", "getUnusedBitPattern", "unusedBitPattern"),
        )
        for mutator_name, getter_name, key in pairs:
            mutator = getattr(pdu, mutator_name)
            getter = getattr(pdu, getter_name)
            assert inspect.cleandoc(getter.__doc__) == NOTES[key], key
            assert inspect.cleandoc(mutator.__doc__).split("\n")[0] == NOTES[key], key

    def test_init_has_no_docstring(self):
        assert NmPdu.__init__.__doc__ is None
