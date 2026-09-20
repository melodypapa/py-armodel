"""
This module contains comprehensive tests for the EndToEndProtection module in SWComponentTemplate.
Tests cover all classes and methods in the EndToEndProtection.py file to achieve 100% test coverage.
"""

import inspect

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import (
    EndToEndDescription,
    EndToEndProtection,
    EndToEndProtectionSet,
    EndToEndProtectionVariablePrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.EndToEndProtection import EndToEndProtectionISignalIPdu
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef


class TestEndToEndDescription:
    """Test class for EndToEndDescription class."""

    def test_end_to_end_description_initialization(self):
        """Test EndToEndDescription initialization and methods."""
        description = EndToEndDescription()
        assert description.category is None
        assert description.counterOffset is None
        assert description.crcOffset is None
        assert description.dataIds == []
        assert description.dataIdMode is None
        assert description.dataIdNibbleOffset is None
        assert description.dataLength is None
        assert description.maxDeltaCounterInit is None
        assert description.maxNoNewOrRepeatedData is None
        assert description.syncCounterInit is None

        # Test setters and getters
        category = NameToken()
        category.setValue("TestCategory")
        description.setCategory(category)
        assert description.getCategory() == category

        counter_offset = PositiveInteger()
        counter_offset.setValue(5)
        description.setCounterOffset(counter_offset)
        assert description.getCounterOffset() == counter_offset

        crc_offset = PositiveInteger()
        crc_offset.setValue(10)
        description.setCrcOffset(crc_offset)
        assert description.getCrcOffset() == crc_offset

        # Test data IDs methods
        data_id = PositiveInteger()
        data_id.setValue(100)
        description.addDataId(data_id)
        assert data_id in description.getDataIds()

        data_id_mode = PositiveInteger()
        data_id_mode.setValue(2)
        description.setDataIdMode(data_id_mode)
        assert description.getDataIdMode() == data_id_mode

        data_id_nibble = PositiveInteger()
        data_id_nibble.setValue(3)
        description.setDataIdNibbleOffset(data_id_nibble)
        assert description.getDataIdNibbleOffset() == data_id_nibble

        data_length = PositiveInteger()
        data_length.setValue(255)
        description.setDataLength(data_length)
        assert description.getDataLength() == data_length

        max_delta = PositiveInteger()
        max_delta.setValue(50)
        description.setMaxDeltaCounterInit(max_delta)
        assert description.getMaxDeltaCounterInit() == max_delta

        max_no_new = 100  # int value
        description.setMaxNoNewOrRepeatedData(max_no_new)
        assert description.getMaxNoNewOrRepeatedData() == max_no_new

        sync_counter = PositiveInteger()
        sync_counter.setValue(25)
        description.setSyncCounterInit(sync_counter)
        assert description.getSyncCounterInit() == sync_counter


class TestEndToEndProtectionVariablePrototype:
    """Test class for EndToEndProtectionVariablePrototype class."""

    def test_spec_base_and_instantiation(self):
        """Test the spec Base chain and concrete instantiation."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable

        prototype = EndToEndProtectionVariablePrototype()
        assert isinstance(prototype, ARObject)
        assert isinstance(prototype, VariationPointCapable)

    def test_initialization(self):
        """Test all __init__ field defaults per Table 4.98."""
        prototype = EndToEndProtectionVariablePrototype()
        assert prototype.receiverIRefs == []
        assert prototype.senderIRef is None
        assert prototype.shortLabel is None

    def test_class_docstring_note_verbatim(self):
        """Test the class docstring is the spec Note verbatim (Table 4.98)."""
        expected = (
            "It is possible to protect the data exchanged between software components. "
            "For this purpose, for each communication to be protected, the user defines a separate "
            "EndToEndProtection (specifying a set of protection settings) and refers to a "
            "variableDataPrototype in the role of sender and to one or many variableDataPrototypes "
            "in the role of receiver. For details, see EndToEnd Library. Caveat: The E2E wrapper "
            "approach involves technologies that are not subjected to the AUTOSAR standard and is "
            "superseded by the superior E2E transformer approach (which is fully standardized by "
            "AUTOSAR). Hence, new projects (without legacy constraints due to carry-over parts) "
            "shall use the fully standardized E2E transformer approach."
        )
        assert inspect.cleandoc(EndToEndProtectionVariablePrototype.__doc__) == expected

    def test_init_docless(self):
        """Test __init__ has no docstring (Rule 0012.2.4)."""
        assert EndToEndProtectionVariablePrototype.__init__.__doc__ is None

    def test_add_receiver_iref(self):
        """Test addReceiverIref appends, returns self, and is a None no-op."""
        prototype = EndToEndProtectionVariablePrototype()
        iref = VariableDataPrototypeInSystemInstanceRef()
        assert prototype.addReceiverIref(iref) is prototype
        assert prototype.getReceiverIrefs() == [iref]
        prototype.addReceiverIref(None)
        assert prototype.getReceiverIrefs() == [iref]

    def test_get_set_sender_iref(self):
        """Test getSenderIref/setSenderIref round-trip, chaining, and None no-op."""
        prototype = EndToEndProtectionVariablePrototype()
        assert prototype.getSenderIref() is None
        iref = VariableDataPrototypeInSystemInstanceRef()
        assert prototype.setSenderIref(iref) is prototype
        assert prototype.getSenderIref() is iref
        prototype.setSenderIref(None)
        assert prototype.getSenderIref() is iref

    def test_get_set_short_label(self):
        """Test getShortLabel/setShortLabel round-trip, chaining, and None no-op."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier

        prototype = EndToEndProtectionVariablePrototype()
        assert prototype.getShortLabel() is None
        label = Identifier()
        label.setValue("SegmentA")
        assert prototype.setShortLabel(label) is prototype
        assert prototype.getShortLabel() is label
        prototype.setShortLabel(None)
        assert prototype.getShortLabel() is label


class TestEndToEndProtection:
    """Test class for EndToEndProtection class."""

    def test_end_to_end_protection_initialization(self):
        """Test EndToEndProtection initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        protection = EndToEndProtection(ar_root, "TestProtection")

        assert protection.parent == ar_root
        assert protection.short_name == "TestProtection"
        assert protection.endToEndProfile is None
        assert protection.endToEndProtectionISignalIPdus == []
        assert protection.endToEndProtectionVariablePrototypes == []

        # Test setters and getters
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import EndToEndDescription

        profile = EndToEndDescription()
        protection.setEndToEndProfile(profile)
        assert protection.getEndToEndProfile() == profile

        # Test EndToEndProtectionISignalIPdu methods
        pdu = EndToEndProtectionISignalIPdu()
        protection.addEndToEndProtectionISignalIPdu(pdu)
        assert pdu in protection.getEndToEndProtectionISignalIPdus()

        # Test EndToEndProtectionVariablePrototype methods
        var_prototype = EndToEndProtectionVariablePrototype()
        protection.addEndToEndProtectionVariablePrototype(var_prototype)
        assert var_prototype in protection.getEndToEndProtectionVariablePrototypes()


class TestEndToEndProtectionSet:
    """Test class for EndToEndProtectionSet class."""

    def test_end_to_end_protection_set_initialization(self):
        """Test EndToEndProtectionSet initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        protection_set = EndToEndProtectionSet(ar_root, "TestProtectionSet")

        assert protection_set.parent == ar_root
        assert protection_set.short_name == "TestProtectionSet"

        # Test create and get methods
        protection = protection_set.createEndToEndProtection("TestProtection")
        assert protection is not None
        assert protection.short_name == "TestProtection"
        assert protection.parent == protection_set

        protections = protection_set.getEndToEndProtections()
        assert len(protections) == 1
        assert protections[0] == protection
