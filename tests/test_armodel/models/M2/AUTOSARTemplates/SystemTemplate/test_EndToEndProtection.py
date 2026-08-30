"""
This module contains comprehensive tests for the EndToEndProtection module in SystemTemplate.
Tests cover all classes and methods in the EndToEndProtection.py file to achieve 100% test coverage.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.EndToEndProtection import EndToEndProtectionISignalIPdu


class TestEndToEndProtectionISignalIPdu:
    """Test class for EndToEndProtectionISignalIPdu class."""

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
