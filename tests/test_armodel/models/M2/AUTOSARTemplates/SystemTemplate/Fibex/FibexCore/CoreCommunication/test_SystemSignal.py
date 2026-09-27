import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    SystemSignal,
)

CLASS_NOTE = (
    "The system signal represents the communication system's view of data exchanged between SW components which "
    "reside on different ECUs. The system signals allow to represent this communication in a flattened structure, "
    "with exactly one system signal defined for each data element prototype sent and received by connected SW "
    "component instances. Tags: atp.recommendedPackage=SystemSignals"
)
DYNAMIC_LENGTH_NOTE = "The length of dynamic length signals is variable in run-time. Only a maximum length of such a signal is " "specified in the configuration (attribute length in ISignal element)."
PHYSICAL_PROPS_NOTE = "Specification of the physical representation. Stereotypes: atpSplitable Tags: atp.Splitkey=physicalProps"


class TestSystemSignal:
    """Test cases for SystemSignal (Table 5.23, p.218)."""

    def test_initialization_defaults(self):
        signal = SystemSignal(None, "Signal")
        assert signal.getDynamicLength() is None
        assert signal.getPhysicalProps() is None

    def test_get_set_round_trip_and_none_noop(self):
        signal = SystemSignal(None, "Signal")

        dynamic_length = Boolean()
        dynamic_length.setValue(True)
        assert signal.setDynamicLength(dynamic_length) is signal
        assert signal.getDynamicLength() is dynamic_length
        signal.setDynamicLength(None)
        assert signal.getDynamicLength() is dynamic_length

        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps

        props = SwDataDefProps()
        assert signal.setPhysicalProps(props) is signal
        assert signal.getPhysicalProps() is props

    def test_class_docstring_note(self):
        assert inspect.cleandoc(SystemSignal.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        signal = SystemSignal(None, "Signal")
        assert inspect.cleandoc(signal.getDynamicLength.__doc__) == DYNAMIC_LENGTH_NOTE
        assert inspect.cleandoc(signal.setDynamicLength.__doc__).split("\n")[0] == DYNAMIC_LENGTH_NOTE
        assert inspect.cleandoc(signal.getPhysicalProps.__doc__) == PHYSICAL_PROPS_NOTE
        assert inspect.cleandoc(signal.setPhysicalProps.__doc__).split("\n")[0] == PHYSICAL_PROPS_NOTE
