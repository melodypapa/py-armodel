import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import ImplementationProps
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import ExecutableEntityActivationReason
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger


class TestExecutableEntityActivationReason:
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        obj = ExecutableEntityActivationReason(ar_root, "act_reason")
        assert isinstance(obj, ARObject)
        assert isinstance(obj, Referrable)
        assert isinstance(obj, ImplementationProps)
        assert obj.short_name == "act_reason"
        assert obj.bitPosition is None
        assert obj.getBitPosition() is None
        assert obj.getSymbol() is None

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.getdoc(ExecutableEntityActivationReason) == (
            "This meta-class represents the ability to define the reason for the activation of the enclosing Executable Entity."
            "\n\n"
            "[constr_1226] Applicable range for ExecutableEntityActivationReason.bitPosition: The value of attribute ExecutableEntityActivationReason.bitPosition shall be in the range of 0 .. 31 at the time when the contract phase generation is executed."
            "\n\n"
            "[constr_1227] Value of attribute ExecutableEntityActivationReason.bitPosition shall be unique: The value of attributes ExecutableEntityActivationReason.bitPosition and ExecutableEntityActivationReason.symbol shall be unique in the context of the enclosing RunnableEntity at the time when the contract phase generation is executed."
            "\n\n"
            "[constr_1939] Existence of attribute ExecutableEntityActivationReason.bitPosition: For each ExecutableEntityActivationReason, attribute bitPosition shall exist at the time when the contract phase generation is executed."
        )

    def test_get_set_bitPosition(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        obj = ExecutableEntityActivationReason(ar_root, "act_reason")
        value = PositiveInteger().setValue("4")
        assert obj.setBitPosition(value) is obj
        assert obj.getBitPosition() is value
        assert obj.getBitPosition().getValue() == 4

    def test_set_bitPosition_none_noop(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        obj = ExecutableEntityActivationReason(ar_root, "act_reason")
        value = PositiveInteger().setValue("31")
        obj.setBitPosition(value)
        obj.setBitPosition(None)
        assert obj.getBitPosition() is value

    def test_get_set_bit_position_type_hints(self):
        obj = ExecutableEntityActivationReason.__new__(ExecutableEntityActivationReason)
        assert typing.get_type_hints(obj.getBitPosition).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(obj.setBitPosition).get("value") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(obj.setBitPosition).get("return") is ExecutableEntityActivationReason
