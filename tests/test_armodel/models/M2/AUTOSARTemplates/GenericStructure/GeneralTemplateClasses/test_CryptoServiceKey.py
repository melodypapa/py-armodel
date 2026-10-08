import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import TextValueSpecification, ValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement, CryptoServiceKey
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    CryptoServiceKeyGenerationEnum,
    PositiveInteger,
    String,
    VerbatimString,
)

CLASS_NOTE = "This meta-class has the ability to represent a crypto key. Tags: atp.recommendedPackage=CryptoDevelopmentKeys"
CLASS_CONSTRAINTS = (
    "[constr_5334] Supported values for CryptoServiceKey.length: The values defined for CryptoServiceKey.length shall be multiple of 8.",
    "[constr_9206] Existence of CryptoServiceKey.length: For each CryptoServiceKey, the attribute length shall exist at the time when the System Description is complete.",
)
NOTES = {
    "algorithmFamily": "This attribute represent the description of the family of the applicable crypto algorithm.",
    "developmentValue": "This aggregation represents the ability to assign a specific value to the crypto key as part of the system description. This value can then be taken for the development of the respective ECU.",
    "keyGeneration": "This attribute describes how a the specific cryptographic key is created.",
    "keyStorageType": "This attribute describes where the enclosing cryptographic key shall be stored. AUTOSAR reserves specific values for this attributes but it is possible to insert custom values as well.",
    "length": "This attribute describes the length of the cryptographic key in bits.",
}


class TestCryptoServiceKey:
    """Test cases for CryptoServiceKey (Table 6.51, p.377)."""

    def test_inheritance(self):
        assert issubclass(CryptoServiceKey, ARElement)

    def test_concrete_instantiation(self):
        key = CryptoServiceKey(None, "CryptoServiceKey1")
        assert key.getShortName() == "CryptoServiceKey1"

    def test_initialization_defaults(self):
        key = CryptoServiceKey(None, "CryptoServiceKey1")
        assert key.getAlgorithmFamily() is None
        assert key.getDevelopmentValue() is None
        assert key.getKeyGeneration() is None
        assert key.getKeyStorageType() is None
        assert key.getLength() is None

    def test_get_set_algorithm_family(self):
        key = CryptoServiceKey(None, "CryptoServiceKey1")

        value = String().setValue("AES")
        assert key.setAlgorithmFamily(value) is key
        assert key.getAlgorithmFamily() is value
        assert key.getAlgorithmFamily().getValue() == "AES"
        key.setAlgorithmFamily(None)
        assert key.getAlgorithmFamily() is value

    def test_get_set_development_value(self):
        key = CryptoServiceKey(None, "CryptoServiceKey1")

        value = TextValueSpecification().setValue(VerbatimString().setValue("0xAFFE"))
        assert key.setDevelopmentValue(value) is key
        assert key.getDevelopmentValue() is value
        assert isinstance(key.getDevelopmentValue(), ValueSpecification)
        assert key.getDevelopmentValue().getValue().getValue() == "0xAFFE"
        key.setDevelopmentValue(None)
        assert key.getDevelopmentValue() is value

    def test_get_set_key_generation(self):
        key = CryptoServiceKey(None, "CryptoServiceKey1")

        value = ARLiteral().setValue("KEY-DERIVATION")
        assert key.setKeyGeneration(value) is key
        assert key.getKeyGeneration() is value
        assert key.getKeyGeneration().getValue() == "KEY-DERIVATION"
        key.setKeyGeneration(None)
        assert key.getKeyGeneration() is value

    def test_get_set_key_storage_type(self):
        key = CryptoServiceKey(None, "CryptoServiceKey1")

        value = String().setValue("LOCAL")
        assert key.setKeyStorageType(value) is key
        assert key.getKeyStorageType() is value
        assert key.getKeyStorageType().getValue() == "LOCAL"
        key.setKeyStorageType(None)
        assert key.getKeyStorageType() is value

    def test_get_set_length(self):
        key = CryptoServiceKey(None, "CryptoServiceKey1")

        value = PositiveInteger().setValue("256")
        assert key.setLength(value) is key
        assert key.getLength() is value
        assert key.getLength().getValue() == 256
        key.setLength(None)
        assert key.getLength() is value

    def test_annotation_pins(self):
        get_set = [
            ("getAlgorithmFamily", "setAlgorithmFamily", String),
            ("getDevelopmentValue", "setDevelopmentValue", ValueSpecification),
            ("getKeyGeneration", "setKeyGeneration", CryptoServiceKeyGenerationEnum),
            ("getKeyStorageType", "setKeyStorageType", String),
            ("getLength", "setLength", PositiveInteger),
        ]
        for getter_name, setter_name, member_type in get_set:
            getter_hints = typing.get_type_hints(getattr(CryptoServiceKey, getter_name))
            assert getter_hints.get("return") == typing.Optional[member_type]
            setter_hints = typing.get_type_hints(getattr(CryptoServiceKey, setter_name))
            assert setter_hints.get("value") == typing.Optional[member_type]
            assert setter_hints.get("return") is CryptoServiceKey

    def test_class_docstring_note(self):
        assert inspect.cleandoc(CryptoServiceKey.__doc__) == CLASS_NOTE + "\n\n" + "\n".join(CLASS_CONSTRAINTS)

    def test_accessor_docstrings_verbatim(self):
        key = CryptoServiceKey(None, "CryptoServiceKey1")
        for attr, note in NOTES.items():
            getter = getattr(key, "get" + attr[0].upper() + attr[1:])
            setter = getattr(key, "set" + attr[0].upper() + attr[1:])
            assert inspect.cleandoc(getter.__doc__) == note
            assert inspect.cleandoc(setter.__doc__).split("\n")[0] == note

    def test_init_has_no_docstring(self):
        assert CryptoServiceKey.__init__.__doc__ is None
