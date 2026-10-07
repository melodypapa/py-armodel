import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import SwcToSwcSignal


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestSwcToSwcSignal:
    """Test cases for SwcToSwcSignal (Table 5.37, p.253)."""

    MEMBERS = [
        "dataElementIRefs",
    ]

    def test_inheritance(self):
        assert issubclass(SwcToSwcSignal, ARObject)

    def test_class_docstring_note(self):
        expected = (
            "The SwcToSwcSignal describes the information (data element) that is exchanged between two SW Components. "
            "On the SWC Level it is possible that a SW Component sends one data element from one P-Port to two different SW Components (1:n Communication). "
            "The SwcToSwcSignal describes exactly the information which is exchanged between one P-Port of a SW Component and one R-Port of another SW Component."
        )
        assert inspect.cleandoc(SwcToSwcSignal.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert SwcToSwcSignal.__init__.__doc__ is None

    def test_initialization_defaults(self):
        signal = SwcToSwcSignal()
        assert signal.getDataElementIRefs() == []

    def test_member_order(self):
        signal = SwcToSwcSignal()
        members = [k for k in vars(signal) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_add_data_element_i_ref(self):
        signal = SwcToSwcSignal()
        iref1 = VariableDataPrototypeInSystemInstanceRef()
        iref2 = VariableDataPrototypeInSystemInstanceRef()
        result = signal.addDataElementIRef(iref1)
        assert result is signal
        signal.addDataElementIRef(iref2)
        assert signal.getDataElementIRefs() == [iref1, iref2]
        signal.addDataElementIRef(None)
        assert len(signal.getDataElementIRefs()) == 2

    def test_type_hints(self):
        hints = typing.get_type_hints(SwcToSwcSignal.getDataElementIRefs)
        assert hints["return"] == typing.List[VariableDataPrototypeInSystemInstanceRef]
        hints = typing.get_type_hints(SwcToSwcSignal.addDataElementIRef)
        assert hints["return"] is SwcToSwcSignal
        assert hints["value"] == typing.Optional[VariableDataPrototypeInSystemInstanceRef]
