"""
This module contains comprehensive tests for the EndToEndProtection module in SWComponentTemplate.
Tests cover all classes and methods in the EndToEndProtection.py file to achieve 100% test coverage.
"""

import inspect
import typing
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import (
    EndToEndDescription,
    EndToEndProtection,
    EndToEndProtectionSet,
    EndToEndProtectionVariablePrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.EndToEndProtection import EndToEndProtectionISignalIPdu
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef


def _field_name(getter_name: str) -> str:
    name = getter_name[len("get") :]
    return name[0].lower() + name[1:]


class TestEndToEndDescription:
    """Heritage / API tests for the synced EndToEndDescription (Table 4.95)."""

    def test_spec_notes_are_verbatim(self):
        expected_notes = {
            "getCategory": "The category represents the identification of the concrete E2E profile. The applicable values are specified in a semantic constraint and determine the applicable attributes of EndToEndDescription.",
            "getCounterOffset": "Bit offset of Counter from the beginning of the Array representation of the Signal Group/VariableDataPrototype (MSB order, bit numbering: bit 0 is the least important). The offset shall be a multiplicity of 4 and it should be 8 whenever possible. For example, offset 8 means that the counter will take the low nibble of the byte 1, i.e. bits 8 .. 11. If counterOffset is not present the value is defined by the selected profile.",
            "getCrcOffset": "Bit offset of CRC from the beginning of the Array representation of the Signal Group/VariableDataPrototype (MSB order, bit numbering: bit 0 is the least important). The offset shall be a multiplicity of 8 and it should be 0 whenever possible. For example, offset 8 means that the CRC will take the byte 1, i.e. bits 8..15. If crcOffset is not present the value is defined by the selected profile.",
            "getDataIds": "This represents a unique numerical identifier. Note: ID is used for protection against masquerading. The details concerning the maximum number of values (this information is specific for each E2E profile) applicable for this attribute are controlled by a semantic constraint that depends on the category of the EndToEndProtection.",
            "getDataIdMode": "There are three inclusion modes how the implicit two-byte Data ID is included in the one-byte CRC: • dataIDMode = 0: Two bytes are included in the CRC (double ID configuration) This is used in variant 1A. • dataIDMode = 1: One of the two bytes byte is included, alternating high and low byte, depending on parity of the counter (alternating ID configuration). For even counter low byte is included; For odd counters the high byte is included. This is used in variant 1B. • dataIDMode = 2: Only low byte is included, high byte is never used. This is applicable if the IDs in a particular system are 8 bits. • dataIdMode = 3: The low byte is included in the implicit CRC calculation, the low nibble of the high byte is transmitted along with the data (i.e. it is explicitly included), the high nibble of the high byte is not used. This is applicable for the IDs up to 12 bits.",
            "getDataIdNibbleOffset": "Bit offset of the low nibble of the high byte of Data ID. The applicability of this attribute is controlled by [constr_1261].",
            "getDataLength": "This attribute represents the length of the Array representation of the Signal Group/VariableDataPrototype including CRC and Counter in bits.",
            "getMaxDeltaCounterInit": "Initial maximum allowed gap between two counter values of two consecutively received valid Data, i.e. how many subsequent lost data is accepted. For example, if the receiver gets Data with counter 1 and MaxDeltaCounterInit is 1, then at the next reception the receiver can accept Counters with values 2 and 3, but not 4. Note that if the receiver does not receive new Data at a consecutive read, then the receiver increments the tolerance by 1.",
            "getMaxNoNewOrRepeatedData": "The maximum amount of missing or repeated Data which the receiver does not expect to exceed under normal communication conditions.",
            "getSyncCounterInit": "Number of Data required for validating the consistency of the counter that shall be received with a valid counter (i.e. counter within the allowed lock-in range) after the detection of an unexpected behavior of a received counter.",
        }
        assert EndToEndDescription.__doc__.strip() == (
            "This meta-class contains information about end-to-end protection. The set of applicable attributes depends on the actual value of the category attribute of EndToEndProtection."
        )
        for getter, note in expected_notes.items():
            assert getattr(EndToEndDescription, getter).__doc__.strip() == note
            if getter == "getDataIds":
                continue
            setter = getter.replace("get", "set", 1)
            assert getattr(EndToEndDescription, setter).__doc__.strip() == (note + " A None value is a no-op and does not overwrite an existing %s." % _field_name(getter))
        assert EndToEndDescription.addDataId.__doc__.strip() == (expected_notes["getDataIds"] + " A None value is a no-op and does not append to the dataIds.")

    def test_base_shape(self):
        assert EndToEndDescription.__bases__[0] is ARObject
        signature = inspect.signature(EndToEndDescription.__init__)
        assert list(signature.parameters.keys()) == ["self"]
        hints = typing.get_type_hints(EndToEndDescription.setCategory)
        assert hints.get("value") == Optional[NameToken]
        assert hints.get("return") is EndToEndDescription
        hints = typing.get_type_hints(EndToEndDescription.getCategory)
        assert hints.get("return") == Optional[NameToken]
        for setter, getter in [
            ("setCounterOffset", "getCounterOffset"),
            ("setCrcOffset", "getCrcOffset"),
            ("setDataIdMode", "getDataIdMode"),
            ("setDataIdNibbleOffset", "getDataIdNibbleOffset"),
            ("setDataLength", "getDataLength"),
            ("setMaxDeltaCounterInit", "getMaxDeltaCounterInit"),
            ("setMaxNoNewOrRepeatedData", "getMaxNoNewOrRepeatedData"),
            ("setSyncCounterInit", "getSyncCounterInit"),
        ]:
            hints = typing.get_type_hints(getattr(EndToEndDescription, setter))
            assert hints.get("value") == Optional[PositiveInteger]
            assert hints.get("return") is EndToEndDescription
            hints = typing.get_type_hints(getattr(EndToEndDescription, getter))
            assert hints.get("return") == Optional[PositiveInteger]
        hints = typing.get_type_hints(EndToEndDescription.addDataId)
        assert hints.get("value") == Optional[PositiveInteger]
        assert hints.get("return") is EndToEndDescription
        hints = typing.get_type_hints(EndToEndDescription.getDataIds)
        assert hints.get("return") == List[PositiveInteger]

    def test_initialization(self):
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

    def test_get_set_scalar_attributes(self):
        description = EndToEndDescription()

        category = NameToken()
        category.setValue("PROFILE1")
        assert description.setCategory(category) is description
        assert description.getCategory() is category
        description.setCategory(None)
        assert description.getCategory() is category

        for setter, getter, value in [
            ("setCounterOffset", "getCounterOffset", "5"),
            ("setCrcOffset", "getCrcOffset", "8"),
            ("setDataIdMode", "getDataIdMode", "1"),
            ("setDataIdNibbleOffset", "getDataIdNibbleOffset", "4"),
            ("setDataLength", "getDataLength", "120"),
            ("setMaxDeltaCounterInit", "getMaxDeltaCounterInit", "2"),
            ("setMaxNoNewOrRepeatedData", "getMaxNoNewOrRepeatedData", "3"),
            ("setSyncCounterInit", "getSyncCounterInit", "3"),
        ]:
            numerical = PositiveInteger()
            numerical.setValue(value)
            assert getattr(description, setter)(numerical) is description
            assert getattr(description, getter)() is numerical
            assert getattr(description, getter)().getValue() == int(value)
            getattr(description, setter)(None)
            assert getattr(description, getter)() is numerical

    def test_add_data_id(self):
        description = EndToEndDescription()

        first = PositiveInteger()
        first.setValue("1")
        second = PositiveInteger()
        second.setValue("2")
        assert description.addDataId(first) is description
        assert description.addDataId(second) is description
        assert description.getDataIds() == [first, second]

        description.addDataId(None)
        assert description.getDataIds() == [first, second]


class TestEndToEndProtectionVariablePrototype:
    """Test class for EndToEndProtectionVariablePrototype class."""

    def test_spec_base_and_instantiation(self):
        """Test the spec Base chain and concrete instantiation."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

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
    """Test class for EndToEndProtection class (Swc TPS Table 4.97)."""

    def test_spec_base(self):
        """Test the most-derived spec base and VP capability (Table 4.97 Base = Identifiable; XSD anchors VARIATION-POINT)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        assert issubclass(EndToEndProtection, Identifiable)
        assert issubclass(EndToEndProtection, VariationPointCapable)
        protection = EndToEndProtection(ar_root, "BaseProtection")
        assert protection.parent == ar_root
        assert protection.short_name == "BaseProtection"

    def test_initialization(self):
        """Test all __init__ field defaults per Table 4.97."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        protection = EndToEndProtection(ar_root, "DefaultsProtection")
        assert protection.endToEndProfile is None
        assert protection.endToEndProtectionISignalIPdus == []
        assert protection.endToEndProtectionVariablePrototypes == []
        assert protection.getVariationPoint() is None

    def test_class_docstring_note_verbatim(self):
        """Test the class docstring is the spec Note verbatim (Table 4.97)."""
        expected = "This meta-class represents the ability to describe a particular end to end protection."
        assert inspect.cleandoc(EndToEndProtection.__doc__) == expected

    def test_init_docless(self):
        """Test __init__ has no docstring (Rule 0012.2.4)."""
        assert EndToEndProtection.__init__.__doc__ is None

    def test_spec_notes_are_verbatim(self):
        """Test per-attribute Note texts are verbatim in comments, getter and setter docstrings (Table 4.97)."""
        expected_notes = {
            "getEndToEndProfile": "This represents the particular EndToEndDescription.",
            "getEndToEndProtectionISignalIPdus": "Defines to which ISignalIPdu - ISignalGroup pair this EndToEndProtection shall apply. In case several ISignalGroups are used to transport the data (e.g. fan-out in the RTE) there may exist several EndToEndProtectionISignalIPdu definitions.",
            "getEndToEndProtectionVariablePrototypes": "Defines to which VariableDataPrototypes in the roles of one sender and one or more receivers this EndToEndprotection applies. It shall be possible to aggregate several EndToEndProtectionVariablePrototype in case additional hierarchical decompositions are introduced subsequently. In this case one particular PortPrototype is split into multiple PortPrototypes and connectors, all representing the same data entity. Caveat: The E2E wrapper approach involves technologies that are not subjected to the AUTOSAR standard and is superseded by the superior E2E transformer approach (which is fully standardized by AUTOSAR). Hence, new projects (without legacy constraints due to carry-over parts) shall use the fully standardized E2E transformer approach.",
        }
        for getter, note in expected_notes.items():
            assert getattr(EndToEndProtection, getter).__doc__.strip() == note
        assert EndToEndProtection.setEndToEndProfile.__doc__.strip() == (expected_notes["getEndToEndProfile"] + " A None value is a no-op and does not overwrite an existing endToEndProfile.")
        assert EndToEndProtection.addEndToEndProtectionISignalIPdu.__doc__.strip() == (
            expected_notes["getEndToEndProtectionISignalIPdus"] + " A None value is a no-op and does not append to the endToEndProtectionISignalIPdus."
        )
        assert EndToEndProtection.addEndToEndProtectionVariablePrototype.__doc__.strip() == (
            expected_notes["getEndToEndProtectionVariablePrototypes"] + " A None value is a no-op and does not append to the endToEndProtectionVariablePrototypes."
        )
        assert EndToEndProtection.getEndToEndProtectionISignalIPdus.__doc__.strip() == expected_notes["getEndToEndProtectionISignalIPdus"]
        assert EndToEndProtection.getEndToEndProtectionVariablePrototypes.__doc__.strip() == expected_notes["getEndToEndProtectionVariablePrototypes"]

    def test_type_hints_and_accessor_order(self):
        """Test annotations match the spec multiplicity and accessors follow the spec row order (Rule 0001.11)."""
        hints = typing.get_type_hints(EndToEndProtection.getEndToEndProfile)
        assert hints.get("return") == Optional[EndToEndDescription]
        hints = typing.get_type_hints(EndToEndProtection.setEndToEndProfile)
        assert hints.get("value") == Optional[EndToEndDescription]
        assert hints.get("return") is EndToEndProtection
        hints = typing.get_type_hints(EndToEndProtection.addEndToEndProtectionISignalIPdu)
        assert hints.get("value") == Optional[EndToEndProtectionISignalIPdu]
        assert hints.get("return") is EndToEndProtection
        hints = typing.get_type_hints(EndToEndProtection.getEndToEndProtectionISignalIPdus)
        assert hints.get("return") == List[EndToEndProtectionISignalIPdu]
        hints = typing.get_type_hints(EndToEndProtection.addEndToEndProtectionVariablePrototype)
        assert hints.get("value") == Optional[EndToEndProtectionVariablePrototype]
        assert hints.get("return") is EndToEndProtection
        hints = typing.get_type_hints(EndToEndProtection.getEndToEndProtectionVariablePrototypes)
        assert hints.get("return") == List[EndToEndProtectionVariablePrototype]
        methods = [name for name in EndToEndProtection.__dict__ if not name.startswith("_")]
        assert methods == [
            "getEndToEndProfile",
            "setEndToEndProfile",
            "addEndToEndProtectionISignalIPdu",
            "getEndToEndProtectionISignalIPdus",
            "addEndToEndProtectionVariablePrototype",
            "getEndToEndProtectionVariablePrototypes",
        ]

    def test_get_set_end_to_end_profile(self):
        """Test get/setEndToEndProfile round-trip, chaining, and None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        protection = EndToEndProtection(ar_root, "ProfileProtection")
        assert protection.getEndToEndProfile() is None
        profile = EndToEndDescription()
        assert protection.setEndToEndProfile(profile) is protection
        assert protection.getEndToEndProfile() is profile
        protection.setEndToEndProfile(None)
        assert protection.getEndToEndProfile() is profile

    def test_add_end_to_end_protection_i_signal_ipdu(self):
        """Test addEndToEndProtectionISignalIPdu appends, returns self, and is a None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        protection = EndToEndProtection(ar_root, "IpduProtection")
        first = EndToEndProtectionISignalIPdu()
        second = EndToEndProtectionISignalIPdu()
        assert protection.addEndToEndProtectionISignalIPdu(first) is protection
        assert protection.addEndToEndProtectionISignalIPdu(second) is protection
        assert protection.getEndToEndProtectionISignalIPdus() == [first, second]
        protection.addEndToEndProtectionISignalIPdu(None)
        assert protection.getEndToEndProtectionISignalIPdus() == [first, second]

    def test_add_end_to_end_protection_variable_prototype(self):
        """Test addEndToEndProtectionVariablePrototype appends, returns self, and is a None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        protection = EndToEndProtection(ar_root, "VarProtection")
        first = EndToEndProtectionVariablePrototype()
        second = EndToEndProtectionVariablePrototype()
        assert protection.addEndToEndProtectionVariablePrototype(first) is protection
        assert protection.addEndToEndProtectionVariablePrototype(second) is protection
        assert protection.getEndToEndProtectionVariablePrototypes() == [first, second]
        protection.addEndToEndProtectionVariablePrototype(None)
        assert protection.getEndToEndProtectionVariablePrototypes() == [first, second]


class TestEndToEndProtectionSet:
    """Test class for EndToEndProtectionSet class (Swc TPS Table 4.96)."""

    def test_spec_base(self):
        """Test the most-derived spec base and instantiation (Table 4.96 Base = ARElement)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        assert issubclass(EndToEndProtectionSet, ARElement)
        protection_set = EndToEndProtectionSet(ar_root, "SpecProtectionSet")
        assert protection_set.parent == ar_root
        assert protection_set.short_name == "SpecProtectionSet"

    def test_initialization(self):
        """Test all __init__ field defaults per Table 4.96."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        protection_set = EndToEndProtectionSet(ar_root, "DefaultsProtectionSet")
        assert protection_set.endToEndProtections == []

    def test_class_docstring_note_verbatim(self):
        """Test the class docstring is the spec Note verbatim (Table 4.96)."""
        expected = "This represents a container for collection EndToEndProtectionInformation."
        assert inspect.cleandoc(EndToEndProtectionSet.__doc__) == expected

    def test_init_docless(self):
        """Test __init__ has no docstring (Rule 0012.2.4)."""
        assert EndToEndProtectionSet.__init__.__doc__ is None

    def test_create_end_to_end_protection(self):
        """Test createEndToEndProtection appends, wires the parent, and returns the existing element on duplicate."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        protection_set = EndToEndProtectionSet(ar_root, "CreateProtectionSet")

        protection = protection_set.createEndToEndProtection("TestProtection")
        assert protection is not None
        assert protection.short_name == "TestProtection"
        assert protection.parent == protection_set
        assert protection_set.getEndToEndProtections() == [protection]

        duplicate = protection_set.createEndToEndProtection("TestProtection")
        assert duplicate is protection
        assert protection_set.getEndToEndProtections() == [protection]

    def test_get_end_to_end_protections_insertion_order(self):
        """Test getEndToEndProtections returns the field in insertion order (no registry re-sorting)."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        protection_set = EndToEndProtectionSet(ar_root, "OrderProtectionSet")

        zeta = protection_set.createEndToEndProtection("Zeta")
        alpha = protection_set.createEndToEndProtection("Alpha")
        assert protection_set.getEndToEndProtections() == [zeta, alpha]
