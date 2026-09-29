"""
This module contains comprehensive tests for the EndToEndProtection module in SystemTemplate.
Tests cover all classes and methods in the EndToEndProtection.py file to achieve 100% test coverage.
"""

import typing
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.EndToEndProtection import EndToEndProtectionISignalIPdu


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestEndToEndProtectionISignalIPdu:
    """Test class for EndToEndProtectionISignalIPdu class."""

    # Table 6.56, p.385 — attribute Notes verbatim from the markdown
    NOTE_DATA_OFFSET = (
        "This attribute defines the beginning offset (in bits) of the Array representation of the Signal Group "
        "(including CRC, counter and application signal group) in the IPdu. "
        "This attribute is mandatory and the dataOffset shall always be defined."
    )
    NOTE_I_SIGNAL_GROUP = "Reference to the ISignalGroup that is to be protected."
    NOTE_I_SIGNAL_IPDU = "Reference to the ISignalIPdu that transmits the protected ISignalGroup."

    def test_end_to_end_protection_i_signal_i_pdu_initialization(self):
        """Test EndToEndProtectionISignalIPdu initialization and methods."""
        pdu = EndToEndProtectionISignalIPdu()
        assert pdu.dataOffset is None
        assert pdu.iSignalGroupRef is None
        assert pdu.iSignalIPduRef is None

        # Test setters and getters
        offset = Integer()
        offset.setValue(10)
        pdu.setDataOffset(offset)
        assert pdu.getDataOffset() == offset

        group_ref = RefType()
        group_ref.setValue("/Test/ISignalGroup")
        pdu.setISignalGroupRef(group_ref)
        assert pdu.getISignalGroupRef() == group_ref

        pdu_ref = RefType()
        pdu_ref.setValue("/Test/ISignalIPdu")
        pdu.setISignalIPduRef(pdu_ref)
        assert pdu.getISignalIPduRef() == pdu_ref

    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.56, p.385 — class Note verbatim from the markdown + table constraints appended
        note = (
            "It is possible to protect the inter-ECU data exchange of safety-related ISignalGroups at the level of COM IPdus "
            "using protection mechanisms provided by E2E Library. "
            "For each ISignalGroup to be protected, a separate EndToEndProtectionISignalIPdu element shall be created "
            "within the EndToEndProtectionSet. "
            "The EndToEndProtectionISignalIPdu element refers to the ISignalGroup that is to be protected and to the ISignalIPdu "
            "that transmits the protected ISignalGroup. "
            "The information how the referenced ISignalGroup shall be protected (through which E2E Profile and with which E2E settings) "
            "is defined in the EndToEnd Description element."
        )
        constrs = [
            "[constr_9207] Existence of EndToEndProtectionISignalIPdu.iSignalIPdu: For each EndToEndProtectionISignalIPdu, the reference to ISignalIPdu in the role iSignalIPdu shall exist at the time when the System Description is complete.",
            "[constr_9208] Existence of EndToEndProtectionISignalIPdu.iSignalGroup: For each EndToEndProtectionISignalIPdu, the reference to ISignalGroup in the role iSignalGroup shall exist at the time when the System Description is complete.",
            "[constr_9209] Existence of EndToEndProtectionISignalIPdu.dataOffset: For each EndToEndProtectionISignalIPdu, the attribute dataOffset shall exist at the time when the System Description is complete.",
        ]
        expected = note + "\n\n" + "\n\n".join(constrs)
        assert EndToEndProtectionISignalIPdu.__doc__.strip() == expected

    def test_init_has_no_docstring(self):
        assert EndToEndProtectionISignalIPdu.__init__.__doc__ is None

    def test_heritage(self):
        pdu = EndToEndProtectionISignalIPdu()
        assert isinstance(pdu, ARObject)
        assert hasattr(pdu, "getVariationPoint")

    def test_get_set_data_offset_none_no_op(self):
        pdu = EndToEndProtectionISignalIPdu()
        value = Integer().setValue("8")
        assert pdu.setDataOffset(value) is pdu
        assert pdu.getDataOffset() is value
        pdu.setDataOffset(None)
        assert pdu.getDataOffset() is value

    def test_get_set_i_signal_group_ref_none_no_op(self):
        pdu = EndToEndProtectionISignalIPdu()
        value = _ref("/ISignalGroups/Grp", "I-SIGNAL-GROUP")
        assert pdu.setISignalGroupRef(value) is pdu
        assert pdu.getISignalGroupRef() is value
        assert pdu.getISignalGroupRef().getDest() == "I-SIGNAL-GROUP"
        pdu.setISignalGroupRef(None)
        assert pdu.getISignalGroupRef() is value

    def test_get_set_i_signal_i_pdu_ref_none_no_op(self):
        pdu = EndToEndProtectionISignalIPdu()
        value = _ref("/IPdus/Pdu", "I-SIGNAL-I-PDU")
        assert pdu.setISignalIPduRef(value) is pdu
        assert pdu.getISignalIPduRef() is value
        assert pdu.getISignalIPduRef().getDest() == "I-SIGNAL-I-PDU"
        pdu.setISignalIPduRef(None)
        assert pdu.getISignalIPduRef() is value

    def test_type_hints_pins(self):
        assert typing.get_type_hints(EndToEndProtectionISignalIPdu.getDataOffset).get("return") == Optional[Integer]
        assert typing.get_type_hints(EndToEndProtectionISignalIPdu.setDataOffset).get("value") == Optional[Integer]
        assert typing.get_type_hints(EndToEndProtectionISignalIPdu.setDataOffset).get("return") is EndToEndProtectionISignalIPdu
        assert typing.get_type_hints(EndToEndProtectionISignalIPdu.getISignalGroupRef).get("return") == Optional[RefType]
        assert typing.get_type_hints(EndToEndProtectionISignalIPdu.setISignalGroupRef).get("value") == Optional[RefType]
        assert typing.get_type_hints(EndToEndProtectionISignalIPdu.getISignalIPduRef).get("return") == Optional[RefType]
        assert typing.get_type_hints(EndToEndProtectionISignalIPdu.setISignalIPduRef).get("value") == Optional[RefType]
