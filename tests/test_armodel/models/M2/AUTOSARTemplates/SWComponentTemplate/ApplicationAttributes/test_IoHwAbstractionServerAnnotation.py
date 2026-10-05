import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Float, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    FilterDebouncingEnum,
    IoHwAbstractionServerAnnotation,
    PulseTestEnum,
)

CLASS_NOTE = 'The IoHwAbstractionServerAnnotation will only be used from a sensor- or an actuator component while interacting with the IoHwAbstraction layer. Note that the "server" in the name of this meta-class is not meant to restrict the usage to ClientServer Interfaces.'
AGE_NOTE = "In case of a SET operation, the age will be interpreted as Delay while in a GET operation (input) it specifies the Lifetime of the signal within the IoHwAbstraction Layer"
ARGUMENT_NOTE = "Reference to the corresponding ArgumentDataPrototype."
BSW_RESOLUTION_NOTE = "This value is determined by an appropriate combination of the range, the unit as well as the data-elements type, i.e. (ecuSignalRange.upperLimit-ecuSignalRange.lower Limit) / (2ˆdatatypelength - 1)"
DATA_ELEMENT_NOTE = "Reference to the corresponding VariableDataPrototype."
FAILURE_MONITORING_NOTE = "This is only applicable in SET operations. If it is enabled, the IoHwAbstraction layer will monitor the result of the operation and issue an diagnostic signal. This means especially, that an additional client-server port has to be created. Tools can use this information to cross-check whether for each data-element in a SET operation with FailureMonitoring enabled an additional port is created The referenced port monitors a failure in the to be monitored VariableDataPrototype of the IoHwAbstraction layer. The referenced port has to be another port of the same Actuator or Sensor Component."
FILTERING_NOTE = "This attribute is used to indicate what kind of filtering/ debouncing has been put to the signal in the IoHw Abstraction layer. rawData means that no modification of the signal has been applied. This is the default value debounceData means that the signal is a mean value waitTimeData means that the signal is delivered by a GET operation after a certain amount of time"
PULSE_TEST_NOTE = (
    "This attribute indicates to the connected SensorActuator SwComponentType whether the VariableDataPrototype can be used to generate pulse test sequences using the IoHwAbstraction layer"
)
TRIGGER_NOTE = "Reference to the corresponding Trigger."


class TestIoHwAbstractionServerAnnotation:
    def test_initialization(self):
        annotation = IoHwAbstractionServerAnnotation()

        assert annotation.getAge() is None
        assert annotation.getArgumentRef() is None
        assert annotation.getBswResolution() is None
        assert annotation.getDataElementRef() is None
        assert annotation.getFailureMonitoringRef() is None
        assert annotation.getFilteringDebouncing() is None
        assert annotation.getPulseTest() is None
        assert annotation.getTriggerRef() is None

    def test_get_set_age(self):
        annotation = IoHwAbstractionServerAnnotation()
        value = MultidimensionalTime()

        assert annotation == annotation.setAge(None)
        assert annotation.getAge() is None

        assert annotation == annotation.setAge(value)
        assert annotation.getAge() is value

        annotation.setAge(None)
        assert annotation.getAge() is value

    def test_get_set_argument_ref(self):
        annotation = IoHwAbstractionServerAnnotation()
        ref = RefType().setValue("/AUTOSAR/Arg")

        assert annotation == annotation.setArgumentRef(ref)
        assert annotation.getArgumentRef() is ref

        annotation.setArgumentRef(None)
        assert annotation.getArgumentRef() is ref

    def test_get_set_bsw_resolution(self):
        annotation = IoHwAbstractionServerAnnotation()
        value = Float().setValue("1.5")

        assert annotation == annotation.setBswResolution(value)
        assert annotation.getBswResolution() is value
        assert annotation.getBswResolution().getValue() == 1.5

        annotation.setBswResolution(None)
        assert annotation.getBswResolution() is value

    def test_get_set_data_element_ref(self):
        annotation = IoHwAbstractionServerAnnotation()
        ref = RefType().setValue("/AUTOSAR/Data")

        assert annotation == annotation.setDataElementRef(ref)
        assert annotation.getDataElementRef() is ref

        annotation.setDataElementRef(None)
        assert annotation.getDataElementRef() is ref

    def test_get_set_failure_monitoring_ref(self):
        annotation = IoHwAbstractionServerAnnotation()
        ref = RefType().setValue("/AUTOSAR/Port2")
        ref.setDest("PORT-PROTOTYPE")

        assert annotation == annotation.setFailureMonitoringRef(ref)
        assert annotation.getFailureMonitoringRef() is ref

        annotation.setFailureMonitoringRef(None)
        assert annotation.getFailureMonitoringRef() is ref

    def test_get_set_filtering_debouncing(self):
        annotation = IoHwAbstractionServerAnnotation()
        value = FilterDebouncingEnum().setValue(FilterDebouncingEnum.DEBOUNCE_DATA)

        assert annotation == annotation.setFilteringDebouncing(value)
        assert annotation.getFilteringDebouncing() is value
        assert annotation.getFilteringDebouncing().getValue() == "debounceData"

        annotation.setFilteringDebouncing(None)
        assert annotation.getFilteringDebouncing() is value

    def test_get_set_pulse_test(self):
        annotation = IoHwAbstractionServerAnnotation()
        value = PulseTestEnum().setValue(PulseTestEnum.ENABLE)

        assert annotation == annotation.setPulseTest(value)
        assert annotation.getPulseTest() is value
        assert annotation.getPulseTest().getValue() == "enable"

        annotation.setPulseTest(None)
        assert annotation.getPulseTest() is value

    def test_get_set_trigger_ref(self):
        annotation = IoHwAbstractionServerAnnotation()
        ref = RefType().setValue("/AUTOSAR/Trig")
        ref.setDest("TRIGGER")

        assert annotation == annotation.setTriggerRef(ref)
        assert annotation.getTriggerRef() is ref

        annotation.setTriggerRef(None)
        assert annotation.getTriggerRef() is ref

    def test_class_docstring_verbatim(self):
        assert IoHwAbstractionServerAnnotation.__doc__.strip() == CLASS_NOTE

    def test_docstrings_verbatim(self):
        assert IoHwAbstractionServerAnnotation.getAge.__doc__.strip() == AGE_NOTE
        assert IoHwAbstractionServerAnnotation.setAge.__doc__.strip().splitlines()[0] == AGE_NOTE
        assert IoHwAbstractionServerAnnotation.getArgumentRef.__doc__.strip() == ARGUMENT_NOTE
        assert IoHwAbstractionServerAnnotation.setArgumentRef.__doc__.strip().splitlines()[0] == ARGUMENT_NOTE
        assert IoHwAbstractionServerAnnotation.getBswResolution.__doc__.strip() == BSW_RESOLUTION_NOTE
        assert IoHwAbstractionServerAnnotation.setBswResolution.__doc__.strip().splitlines()[0] == BSW_RESOLUTION_NOTE
        assert IoHwAbstractionServerAnnotation.getDataElementRef.__doc__.strip() == DATA_ELEMENT_NOTE
        assert IoHwAbstractionServerAnnotation.setDataElementRef.__doc__.strip().splitlines()[0] == DATA_ELEMENT_NOTE
        assert IoHwAbstractionServerAnnotation.getFailureMonitoringRef.__doc__.strip() == FAILURE_MONITORING_NOTE
        assert IoHwAbstractionServerAnnotation.setFailureMonitoringRef.__doc__.strip().splitlines()[0] == FAILURE_MONITORING_NOTE
        assert IoHwAbstractionServerAnnotation.getFilteringDebouncing.__doc__.strip() == FILTERING_NOTE
        assert IoHwAbstractionServerAnnotation.setFilteringDebouncing.__doc__.strip().splitlines()[0] == FILTERING_NOTE
        assert IoHwAbstractionServerAnnotation.getPulseTest.__doc__.strip() == PULSE_TEST_NOTE
        assert IoHwAbstractionServerAnnotation.setPulseTest.__doc__.strip().splitlines()[0] == PULSE_TEST_NOTE
        assert IoHwAbstractionServerAnnotation.getTriggerRef.__doc__.strip() == TRIGGER_NOTE
        assert IoHwAbstractionServerAnnotation.setTriggerRef.__doc__.strip().splitlines()[0] == TRIGGER_NOTE

    def test_get_type_hints_pins(self):
        hints = typing.get_type_hints(IoHwAbstractionServerAnnotation.getAge)
        assert hints.get("return") == typing.Optional[MultidimensionalTime]

        hints = typing.get_type_hints(IoHwAbstractionServerAnnotation.setAge)
        assert hints.get("value") == typing.Optional[MultidimensionalTime]
        assert hints.get("return") is IoHwAbstractionServerAnnotation

        hints = typing.get_type_hints(IoHwAbstractionServerAnnotation.getArgumentRef)
        assert hints.get("return") == typing.Optional[RefType]

        hints = typing.get_type_hints(IoHwAbstractionServerAnnotation.getBswResolution)
        assert hints.get("return") == typing.Optional[Float]

        hints = typing.get_type_hints(IoHwAbstractionServerAnnotation.getFilteringDebouncing)
        assert hints.get("return") == typing.Optional[FilterDebouncingEnum]

        hints = typing.get_type_hints(IoHwAbstractionServerAnnotation.getPulseTest)
        assert hints.get("return") == typing.Optional[PulseTestEnum]
