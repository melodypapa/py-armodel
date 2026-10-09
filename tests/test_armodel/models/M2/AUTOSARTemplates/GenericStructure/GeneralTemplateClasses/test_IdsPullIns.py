"""
This module contains tests for the IdsmSignatureSupportAp, IdsmSignatureSupportCp and
SecurityEventContextData pull-in classes.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import IdsmSignatureSupportAp, IdsmSignatureSupportCp, SecurityEventContextData
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String


class TestIdsmSignatureSupportAp:
    def test_initialization(self):
        obj = IdsmSignatureSupportAp()
        assert isinstance(obj, IdsmSignatureSupportAp)
        assert obj.getCryptoPrimitive() is None
        assert obj.getKeySlotRef() is None

    def test_get_set_crypto_primitive(self):
        obj = IdsmSignatureSupportAp()
        value = String()
        value.setValue("TLS-AES-128-GCM")
        assert obj.setCryptoPrimitive(value) is obj
        assert obj.getCryptoPrimitive() is value

    def test_set_crypto_primitive_none_noop(self):
        obj = IdsmSignatureSupportAp()
        value = String()
        value.setValue("TLS-AES-128-GCM")
        obj.setCryptoPrimitive(value)
        assert obj.setCryptoPrimitive(None) is obj
        assert obj.getCryptoPrimitive() is value

    def test_get_set_key_slot_ref(self):
        obj = IdsmSignatureSupportAp()
        ref = RefType().setValue("/Pkg/KeySlot").setDest("CRYPTO-KEY-SLOT")
        assert obj.setKeySlotRef(ref) is obj
        assert obj.getKeySlotRef() is ref


class TestIdsmSignatureSupportCp:
    def test_initialization(self):
        obj = IdsmSignatureSupportCp()
        assert isinstance(obj, IdsmSignatureSupportCp)
        assert obj.getAuthenticationRef() is None
        assert obj.getCryptoServiceKeyRef() is None

    def test_get_set_authentication_ref(self):
        obj = IdsmSignatureSupportCp()
        ref = RefType().setValue("/Pkg/Primitive").setDest("CRYPTO-SERVICE-PRIMITIVE")
        assert obj.setAuthenticationRef(ref) is obj
        assert obj.getAuthenticationRef() is ref

    def test_get_set_crypto_service_key_ref(self):
        obj = IdsmSignatureSupportCp()
        ref = RefType().setValue("/Pkg/Key").setDest("CRYPTO-SERVICE-KEY")
        assert obj.setCryptoServiceKeyRef(ref) is obj
        assert obj.getCryptoServiceKeyRef() is ref


class TestSecurityEventContextData:
    def test_initialization(self):
        obj = SecurityEventContextData()
        assert isinstance(obj, SecurityEventContextData)
        assert obj.getVariationPoint() is None
