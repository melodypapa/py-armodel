from armodel import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.CryptoDeployment import (
    CryptoKeySlot,
    CryptoKeySlotAllowedModification,
    CryptoKeySlotContentAllowedUsage,
    CryptoKeySlotTypeEnum,
    CryptoObjectTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, String


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(value)
    return p


def _string(value):
    s = String()
    s.setValue(value)
    return s


def _new_key_slot(root):
    slot = CryptoKeySlot(root, "KeySlot1")

    slot.setAllocateShadowCopy(_bool("true"))
    slot.setCryptoAlgId(_string("AES-128"))
    object_type = CryptoObjectTypeEnum()
    object_type.setValue("SYMMETRIC-KEY")
    slot.setCryptoObjectType(object_type)

    modification = CryptoKeySlotAllowedModification()
    modification.setAllowContentTypeChange(_bool("false"))
    modification.setExportability(_bool("true"))
    modification.setMaxNumberOfAllowedUpdates(_pos_int("10"))
    modification.setRestrictUpdate(_bool("true"))
    slot.setKeySlotAllowedModification(modification)

    usage1 = CryptoKeySlotContentAllowedUsage()
    usage1.setAllowedKeyslotUsage(_string("ENCRYPT"))
    usage2 = CryptoKeySlotContentAllowedUsage()
    usage2.setAllowedKeyslotUsage(_string("DECRYPT"))
    slot.addKeySlotContentAllowedUsage(usage1)
    assert slot.addKeySlotContentAllowedUsage(usage2) is slot

    slot.setSlotCapacity(_pos_int("256"))
    slot_type = CryptoKeySlotTypeEnum()
    slot_type.setValue("APPLICATION")
    slot.setSlotType(slot_type)
    return slot


class TestCryptoObjectTypeEnum:
    def test_literal_wire_values_and_indices(self):
        # XSD wire values, ordered by atp.EnumerationLiteralIndex (XSD-only member type)
        assert CryptoObjectTypeEnum.UNDEFINED == "UNDEFINED"
        assert CryptoObjectTypeEnum.SYMMETRIC_KEY == "SYMMETRIC-KEY"
        assert CryptoObjectTypeEnum.PRIVATE_KEY == "PRIVATE-KEY"
        assert CryptoObjectTypeEnum.PUBLIC_KEY == "PUBLIC-KEY"
        assert CryptoObjectTypeEnum.SIGNATURE == "SIGNATURE"
        assert CryptoObjectTypeEnum.SECRET_SEED == "SECRET-SEED"

    def test_instantiability(self):
        e = CryptoObjectTypeEnum()
        e.setValue("PRIVATE-KEY")
        assert e.getValue() == "PRIVATE-KEY"


class TestCryptoKeySlotTypeEnum:
    def test_literal_wire_values_and_indices(self):
        # XSD wire values, ordered by atp.EnumerationLiteralIndex (XSD-only member type)
        assert CryptoKeySlotTypeEnum.MACHINE == "MACHINE"
        assert CryptoKeySlotTypeEnum.APPLICATION == "APPLICATION"

    def test_instantiability(self):
        e = CryptoKeySlotTypeEnum()
        e.setValue("MACHINE")
        assert e.getValue() == "MACHINE"


class TestCryptoKeySlotAllowedModification:
    def test_defaults(self):
        modification = CryptoKeySlotAllowedModification()
        assert isinstance(modification, ARObject)
        assert modification.getAllowContentTypeChange() is None
        assert modification.getExportability() is None
        assert modification.getMaxNumberOfAllowedUpdates() is None
        assert modification.getRestrictUpdate() is None

    def test_get_set_round_trip_and_none_noop(self):
        modification = CryptoKeySlotAllowedModification()
        allow = _bool("false")
        export = _bool("true")
        updates = _pos_int("10")
        restrict = _bool("true")
        assert modification.setAllowContentTypeChange(allow) is modification
        assert modification.setExportability(export) is modification
        assert modification.setMaxNumberOfAllowedUpdates(updates) is modification
        assert modification.setRestrictUpdate(restrict) is modification
        assert modification.getAllowContentTypeChange() is allow
        assert modification.getExportability() is export
        assert modification.getMaxNumberOfAllowedUpdates() is updates
        assert modification.getRestrictUpdate() is restrict
        modification.setAllowContentTypeChange(None)
        modification.setExportability(None)
        modification.setMaxNumberOfAllowedUpdates(None)
        modification.setRestrictUpdate(None)
        assert modification.getAllowContentTypeChange() is allow
        assert modification.getExportability() is export
        assert modification.getMaxNumberOfAllowedUpdates() is updates
        assert modification.getRestrictUpdate() is restrict


class TestCryptoKeySlotContentAllowedUsage:
    def test_defaults(self):
        usage = CryptoKeySlotContentAllowedUsage()
        assert isinstance(usage, ARObject)
        assert usage.getAllowedKeyslotUsage() is None

    def test_get_set_round_trip_and_none_noop(self):
        usage = CryptoKeySlotContentAllowedUsage()
        value = _string("ENCRYPT")
        assert usage.setAllowedKeyslotUsage(value) is usage
        assert usage.getAllowedKeyslotUsage() is value
        usage.setAllowedKeyslotUsage(None)
        assert usage.getAllowedKeyslotUsage() is value


class TestCryptoKeySlot:
    def _parent(self):
        document = AUTOSAR.getInstance()
        return document.createARPackage("Crypto")

    def test_docstring_is_spec_note_verbatim(self):
        note = "This meta-class represents the ability to define a concrete key to be used for a crypto operation. Tags: atp.ManifestKind=MachineManifest"
        assert CryptoKeySlot.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert CryptoKeySlot.__init__.__doc__ is None

    def test_heritage(self):
        parent = self._parent()
        slot = CryptoKeySlot(parent, "HeritageSlot")
        assert isinstance(slot, Identifiable)
        assert isinstance(slot, ARObject)

    def test_defaults_in_spec_displayed_order(self):
        slot = CryptoKeySlot(self._parent(), "DefaultsSlot")
        assert slot.getAllocateShadowCopy() is None
        assert slot.getCryptoAlgId() is None
        assert slot.getCryptoObjectType() is None
        assert slot.getKeySlotAllowedModification() is None
        assert slot.getKeySlotContentAllowedUsages() == []
        assert slot.getSlotCapacity() is None
        assert slot.getSlotType() is None

    def test_get_set_round_trip_and_none_noop(self):
        parent = self._parent()
        slot = _new_key_slot(parent)

        assert slot.getAllocateShadowCopy().getValue() is True
        assert slot.getCryptoAlgId().getValue() == "AES-128"
        assert slot.getCryptoObjectType().getValue() == "SYMMETRIC-KEY"
        modification = slot.getKeySlotAllowedModification()
        assert isinstance(modification, CryptoKeySlotAllowedModification)
        assert modification.getRestrictUpdate().getValue() is True
        assert [u.getAllowedKeyslotUsage().getValue() for u in slot.getKeySlotContentAllowedUsages()] == ["ENCRYPT", "DECRYPT"]
        assert slot.getSlotCapacity().getValue() == 256
        assert slot.getSlotType().getValue() == "APPLICATION"

        slot.setAllocateShadowCopy(None)
        slot.setCryptoAlgId(None)
        slot.setCryptoObjectType(None)
        slot.setKeySlotAllowedModification(None)
        slot.addKeySlotContentAllowedUsage(None)
        slot.setSlotCapacity(None)
        slot.setSlotType(None)
        assert slot.getAllocateShadowCopy().getValue() is True
        assert slot.getCryptoAlgId().getValue() == "AES-128"
        assert slot.getCryptoObjectType().getValue() == "SYMMETRIC-KEY"
        assert slot.getKeySlotAllowedModification() is modification
        assert len(slot.getKeySlotContentAllowedUsages()) == 2
        assert slot.getSlotCapacity().getValue() == 256
        assert slot.getSlotType().getValue() == "APPLICATION"

    def test_chaining_setters(self):
        slot = CryptoKeySlot(self._parent(), "ChainSlot")
        assert slot.setAllocateShadowCopy(_bool("true")) is slot
        assert slot.setCryptoAlgId(_string("RSA")) is slot
        assert slot.setCryptoObjectType(CryptoObjectTypeEnum()) is slot
        assert slot.setKeySlotAllowedModification(CryptoKeySlotAllowedModification()) is slot
        assert slot.setSlotCapacity(_pos_int("1")) is slot
        assert slot.setSlotType(CryptoKeySlotTypeEnum()) is slot
