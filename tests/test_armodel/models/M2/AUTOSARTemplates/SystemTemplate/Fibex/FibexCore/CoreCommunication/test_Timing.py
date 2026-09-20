import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing import (
    CyclicTiming,
    EventControlledTiming,
    ModeDrivenTransmissionModeCondition,
    TimeRangeType,
    TransmissionModeCondition,
    TransmissionModeDeclaration,
    TransmissionModeTiming,
)


class Test_FibexCoreTiming:
    """Test cases for FibexCore Timing classes with method chaining."""

    def test_TransmissionModeCondition(self):
        """Test TransmissionModeCondition class functionality with method chaining."""
        condition = TransmissionModeCondition()

        assert isinstance(condition, ARObject)

        # Test default values
        assert condition.getDataFilter() is None
        assert condition.getISignalInIPduRef() is None

        # Test setter/getter methods with method chaining
        filter_obj = DataFilter()
        result = condition.setDataFilter(filter_obj)
        assert condition.getDataFilter() == filter_obj
        assert result == condition  # Test method chaining

        result = condition.setISignalInIPduRef("signal_ref")
        assert condition.getISignalInIPduRef() == "signal_ref"
        assert result == condition  # Test method chaining

        # Test setting None values
        result = condition.setDataFilter(None)
        assert condition.getDataFilter() is None
        assert result == condition  # Test method chaining

        result = condition.setISignalInIPduRef(None)
        assert condition.getISignalInIPduRef() is None
        assert result == condition  # Test method chaining

    def test_TimeRangeType(self):
        """Test TimeRangeType class functionality with method chaining."""
        time_range = TimeRangeType()

        assert isinstance(time_range, ARObject)

        # Test default values
        assert time_range.getTolerance() is None
        assert time_range.getValue() is None

        # Test setter/getter methods with method chaining
        result = time_range.setTolerance("tolerance_val")
        assert time_range.getTolerance() == "tolerance_val"
        assert result == time_range  # Test method chaining

        result = time_range.setValue("time_val")
        assert time_range.getValue() == "time_val"
        assert result == time_range  # Test method chaining

        # Test setting None values
        result = time_range.setTolerance(None)
        assert time_range.getTolerance() is None
        assert result == time_range  # Test method chaining

        result = time_range.setValue(None)
        assert time_range.getValue() is None
        assert result == time_range  # Test method chaining

    def test_CyclicTiming(self):
        """Test CyclicTiming class functionality with method chaining."""
        timing = CyclicTiming()

        assert isinstance(timing, Describable)

        # Test default values
        assert timing.getTimeOffset() is None
        assert timing.getTimePeriod() is None

        # Test setter/getter methods with method chaining
        time_range = TimeRangeType()
        result = timing.setTimeOffset(time_range)
        assert timing.getTimeOffset() == time_range
        assert result == timing  # Test method chaining

        result = timing.setTimePeriod(time_range)
        assert timing.getTimePeriod() == time_range
        assert result == timing  # Test method chaining

        # Test setting None values
        result = timing.setTimeOffset(None)
        assert timing.getTimeOffset() is None
        assert result == timing  # Test method chaining

        result = timing.setTimePeriod(None)
        assert timing.getTimePeriod() is None
        assert result == timing  # Test method chaining

    def test_EventControlledTiming(self):
        """Test EventControlledTiming class functionality with method chaining."""
        timing = EventControlledTiming()

        assert isinstance(timing, Describable)

        # Test default values
        assert timing.getNumberOfRepetitions() is None
        assert timing.getRepetitionPeriod() is None

        # Test setter/getter methods with method chaining
        result = timing.setNumberOfRepetitions(5)
        assert timing.getNumberOfRepetitions() == 5
        assert result == timing  # Test method chaining

        time_range = TimeRangeType()
        result = timing.setRepetitionPeriod(time_range)
        assert timing.getRepetitionPeriod() == time_range
        assert result == timing  # Test method chaining

        # Test setting None values
        result = timing.setNumberOfRepetitions(None)
        assert timing.getNumberOfRepetitions() is None
        assert result == timing  # Test method chaining

        result = timing.setRepetitionPeriod(None)
        assert timing.getRepetitionPeriod() is None
        assert result == timing  # Test method chaining

    def test_TransmissionModeTiming(self):
        """Test TransmissionModeTiming class functionality with method chaining."""
        timing = TransmissionModeTiming()

        assert isinstance(timing, ARObject)

        # Test default values
        assert timing.getCyclicTiming() is None
        assert timing.getEventControlledTiming() is None

        # Test setter/getter methods with method chaining
        cyclic_timing = CyclicTiming()
        result = timing.setCyclicTiming(cyclic_timing)
        assert timing.getCyclicTiming() == cyclic_timing
        assert result == timing  # Test method chaining

        event_timing = EventControlledTiming()
        result = timing.setEventControlledTiming(event_timing)
        assert timing.getEventControlledTiming() == event_timing
        assert result == timing  # Test method chaining

        # Test setting None values
        result = timing.setCyclicTiming(None)
        assert timing.getCyclicTiming() is None
        assert result == timing  # Test method chaining

        result = timing.setEventControlledTiming(None)
        assert timing.getEventControlledTiming() is None
        assert result == timing  # Test method chaining

    def test_TransmissionModeDeclaration(self):
        """Test TransmissionModeDeclaration class functionality with method chaining."""
        declaration = TransmissionModeDeclaration()

        assert isinstance(declaration, ARObject)

        # Test default values
        assert declaration.getModeDrivenFalseConditions() == []
        assert declaration.getModeDrivenTrueConditions() == []
        assert declaration.getTransmissionModeConditions() == []
        assert declaration.getTransmissionModeFalseTiming() is None
        assert declaration.getTransmissionModeTrueTiming() is None

        # Test setter/getter methods with method chaining
        timing = TransmissionModeTiming()
        result = declaration.setTransmissionModeFalseTiming(timing)
        assert declaration.getTransmissionModeFalseTiming() == timing
        assert result == declaration  # Test method chaining

        result = declaration.setTransmissionModeTrueTiming(timing)
        assert declaration.getTransmissionModeTrueTiming() == timing
        assert result == declaration  # Test method chaining

        # Test setting None values
        result = declaration.setTransmissionModeFalseTiming(None)
        assert declaration.getTransmissionModeFalseTiming() is None
        assert result == declaration  # Test method chaining

        result = declaration.setTransmissionModeTrueTiming(None)
        assert declaration.getTransmissionModeTrueTiming() is None
        assert result == declaration  # Test method chaining

        # Test add methods with method chaining
        false_condition = ModeDrivenTransmissionModeCondition()
        result = declaration.addModeDrivenFalseCondition(false_condition)
        assert false_condition in declaration.getModeDrivenFalseConditions()
        assert result == declaration  # Test method chaining

        true_condition = ModeDrivenTransmissionModeCondition()
        result = declaration.addModeDrivenTrueCondition(true_condition)
        assert true_condition in declaration.getModeDrivenTrueConditions()
        assert result == declaration  # Test method chaining

        transmission_condition = TransmissionModeCondition()
        result = declaration.addTransmissionModeCondition(transmission_condition)
        assert transmission_condition in declaration.getTransmissionModeConditions()
        assert result == declaration  # Test method chaining

        # Test adding None values to add methods (these do add None to the list)
        original_false_count = len(declaration.getModeDrivenFalseConditions())
        result = declaration.addModeDrivenFalseCondition(None)
        assert len(declaration.getModeDrivenFalseConditions()) == original_false_count + 1  # Count should increase by 1
        assert result == declaration  # Test method chaining

        original_true_count = len(declaration.getModeDrivenTrueConditions())
        result = declaration.addModeDrivenTrueCondition(None)
        assert len(declaration.getModeDrivenTrueConditions()) == original_true_count + 1  # Count should increase by 1
        assert result == declaration  # Test method chaining

        original_transmission_count = len(declaration.getTransmissionModeConditions())
        result = declaration.addTransmissionModeCondition(None)
        assert len(declaration.getTransmissionModeConditions()) == original_transmission_count + 1  # Count should increase by 1
        assert result == declaration  # Test method chaining


CLASS_NOTE = (
    "The condition defined by this class evaluates to true if one of the referenced modeDeclarations (OR associated) is active. "
    "All referenced modeDeclarations shall be from the same ModeDeclarationGroup. "
    "The condition is used to define which TransmissionMode shall be activated using Com_SwitchIpduTxMode.\n"
    "\n"
    "[constr_9187] Existence of ModeDrivenTransmissionModeCondition.modeDeclaration: For each ModeDrivenTransmissionModeCondition, "
    "the reference to ModeDeclaration in the role modeDeclaration shall exist at the time when the System Description is complete."
)

MODE_DECLARATION_NOTE = "Reference to one modeDeclaration which is OR associated in the context of the ModeDrivenTransmissionModeCondition."


class TestModeDrivenTransmissionModeCondition:
    """Test cases for ModeDrivenTransmissionModeCondition (Table 6.61, p.393)."""

    MEMBERS = [
        "modeDeclarationRefs",
    ]

    def test_inheritance(self):
        assert issubclass(ModeDrivenTransmissionModeCondition, ARObject)

    def test_class_docstring_note(self):
        assert inspect.cleandoc(ModeDrivenTransmissionModeCondition.__doc__) == CLASS_NOTE

    def test_init_docless(self):
        assert ModeDrivenTransmissionModeCondition.__init__.__doc__ is None

    def test_initialization_defaults(self):
        condition = ModeDrivenTransmissionModeCondition()
        assert condition.getModeDeclarationRefs() == []

    def test_member_order(self):
        condition = ModeDrivenTransmissionModeCondition()
        members = [k for k in vars(condition) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_add_get_mode_declaration_refs(self):
        condition = ModeDrivenTransmissionModeCondition()
        ref1 = RefType()
        ref1.setDest("MODE-DECLARATION")
        ref1.setValue("/ModeDcl/FirstMode")
        ref2 = RefType()
        ref2.setDest("MODE-DECLARATION")
        ref2.setValue("/ModeDcl/SecondMode")

        assert condition == condition.addModeDeclarationRef(ref1)
        assert condition == condition.addModeDeclarationRef(ref2)
        refs = condition.getModeDeclarationRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/ModeDcl/FirstMode"
        assert refs[0].getDest() == "MODE-DECLARATION"
        assert refs[1].getValue() == "/ModeDcl/SecondMode"

        assert condition == condition.addModeDeclarationRef(None)
        assert len(condition.getModeDeclarationRefs()) == 2

        getter_hints = typing.get_type_hints(ModeDrivenTransmissionModeCondition.getModeDeclarationRefs)
        assert getter_hints.get("return") == typing.List[RefType]

        add_hints = typing.get_type_hints(ModeDrivenTransmissionModeCondition.addModeDeclarationRef)
        assert add_hints.get("value") == typing.Optional[RefType]
        assert add_hints.get("return") is ModeDrivenTransmissionModeCondition

    def test_docstrings_are_spec_notes(self):
        """Test that the accessor docstrings carry the attribute Note verbatim (Table 6.61)."""
        assert ModeDrivenTransmissionModeCondition.getModeDeclarationRefs.__doc__.strip() == MODE_DECLARATION_NOTE
        assert inspect.cleandoc(ModeDrivenTransmissionModeCondition.addModeDeclarationRef.__doc__).strip() == MODE_DECLARATION_NOTE + "\nA None value is a no-op and does not append anything."
