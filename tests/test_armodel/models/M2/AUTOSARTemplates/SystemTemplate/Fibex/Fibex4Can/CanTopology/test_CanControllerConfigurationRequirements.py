import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Float, Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    AbstractCanCommunicationControllerAttributes,
    CanControllerConfigurationRequirements,
)

CLASS_NOTE = "This element allows the specification of ranges for the CAN Bit Timing configuration parameters. These ranges are taken as requirements and have to be respected by the ECU developer."
MAX_NUMBER_OF_TIME_QUANTA_PER_BIT_NOTE = "Maximum number of time quanta in the bit time."
MAX_SAMPLE_POINT_NOTE = "The max. value of the sample point as a percentage of the total bit time."
MAX_SYNC_JUMP_WIDTH_NOTE = "The max. Synchronization Jump Width value as a percentage of the total bit time. The (Re-)Synchronization Jump Width (SJW) defines how far a resynchronization may move the Sample Point inside the limits defined by the Phase Buffer Segments to compensate for edge phase errors."
MIN_NUMBER_OF_TIME_QUANTA_PER_BIT_NOTE = "Minimum number of time quanta in the bit time."
MIN_SAMPLE_POINT_NOTE = "The min. value of the sample point as a percentage of the total bit time."
MIN_SYNC_JUMP_WIDTH_NOTE = "The min. Synchronization Jump Width value as a percentage of the total bit time. The (Re-)Synchronization Jump Width (SJW) defines how far a resynchronization may move the Sample Point inside the limits defined by the Phase Buffer Segments to compensate for edge phase errors."


class TestCanControllerConfigurationRequirements:
    """Tests for CanControllerConfigurationRequirements (Table 3.15, R23-11)."""

    def test_initialization(self):
        """Test that all __init__ fields default to None, incl. inherited base fields"""
        req = CanControllerConfigurationRequirements()

        assert isinstance(req, ARObject)
        assert isinstance(req, AbstractCanCommunicationControllerAttributes)
        assert req.getMaxNumberOfTimeQuantaPerBit() is None
        assert req.getMaxSamplePoint() is None
        assert req.getMaxSyncJumpWidth() is None
        assert req.getMinNumberOfTimeQuantaPerBit() is None
        assert req.getMinSamplePoint() is None
        assert req.getMinSyncJumpWidth() is None
        assert req.getCanControllerFdAttributes() is None
        assert req.getCanControllerFdRequirements() is None
        assert req.getCanControllerXlAttributes() is None
        assert req.getCanControllerXlRequirements() is None

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 3.15)"""
        assert inspect.cleandoc(CanControllerConfigurationRequirements.__doc__).strip() == CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert CanControllerConfigurationRequirements.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order (Table 3.15)"""
        source = inspect.getsource(CanControllerConfigurationRequirements.__init__)
        assert source.index("self.maxNumberOfTimeQuantaPerBit") < source.index("self.maxSamplePoint")
        assert source.index("self.maxSamplePoint") < source.index("self.maxSyncJumpWidth")
        assert source.index("self.maxSyncJumpWidth") < source.index("self.minNumberOfTimeQuantaPerBit")
        assert source.index("self.minNumberOfTimeQuantaPerBit") < source.index("self.minSamplePoint")
        assert source.index("self.minSamplePoint") < source.index("self.minSyncJumpWidth")

    def _assert_docstring(self, method, note, attr_name=None):
        doc = method.__doc__
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert doc is not None
        assert inspect.cleandoc(doc).strip() == expected

    def test_get_set_max_number_of_time_quanta_per_bit(self):
        """Test maxNumberOfTimeQuantaPerBit default, guarded set chaining, None no-op and typing"""
        req = CanControllerConfigurationRequirements()

        assert req.getMaxNumberOfTimeQuantaPerBit() is None

        value = Integer()
        value.setValue("32")
        assert req == req.setMaxNumberOfTimeQuantaPerBit(value)
        assert req.getMaxNumberOfTimeQuantaPerBit() == value

        assert req == req.setMaxNumberOfTimeQuantaPerBit(None)
        assert req.getMaxNumberOfTimeQuantaPerBit() == value

        getter_hints = typing.get_type_hints(CanControllerConfigurationRequirements.getMaxNumberOfTimeQuantaPerBit)
        assert getter_hints.get("return") == typing.Optional[Integer]

        setter_hints = typing.get_type_hints(CanControllerConfigurationRequirements.setMaxNumberOfTimeQuantaPerBit)
        assert setter_hints.get("value") == typing.Optional[Integer]
        assert setter_hints.get("return") is CanControllerConfigurationRequirements

    def test_max_number_of_time_quanta_per_bit_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.15)"""
        self._assert_docstring(CanControllerConfigurationRequirements.getMaxNumberOfTimeQuantaPerBit, MAX_NUMBER_OF_TIME_QUANTA_PER_BIT_NOTE)
        self._assert_docstring(CanControllerConfigurationRequirements.setMaxNumberOfTimeQuantaPerBit, MAX_NUMBER_OF_TIME_QUANTA_PER_BIT_NOTE, "maxNumberOfTimeQuantaPerBit")

    def test_get_set_max_sample_point(self):
        """Test maxSamplePoint default, guarded set chaining, None no-op and typing"""
        req = CanControllerConfigurationRequirements()

        assert req.getMaxSamplePoint() is None

        value = Float()
        value.setValue("0.8")
        assert req == req.setMaxSamplePoint(value)
        assert req.getMaxSamplePoint() == value

        assert req == req.setMaxSamplePoint(None)
        assert req.getMaxSamplePoint() == value

        getter_hints = typing.get_type_hints(CanControllerConfigurationRequirements.getMaxSamplePoint)
        assert getter_hints.get("return") == typing.Optional[Float]

        setter_hints = typing.get_type_hints(CanControllerConfigurationRequirements.setMaxSamplePoint)
        assert setter_hints.get("value") == typing.Optional[Float]
        assert setter_hints.get("return") is CanControllerConfigurationRequirements

    def test_max_sample_point_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.15)"""
        self._assert_docstring(CanControllerConfigurationRequirements.getMaxSamplePoint, MAX_SAMPLE_POINT_NOTE)
        self._assert_docstring(CanControllerConfigurationRequirements.setMaxSamplePoint, MAX_SAMPLE_POINT_NOTE, "maxSamplePoint")

    def test_get_set_max_sync_jump_width(self):
        """Test maxSyncJumpWidth default, guarded set chaining, None no-op and typing"""
        req = CanControllerConfigurationRequirements()

        assert req.getMaxSyncJumpWidth() is None

        value = Float()
        value.setValue("0.2")
        assert req == req.setMaxSyncJumpWidth(value)
        assert req.getMaxSyncJumpWidth() == value

        assert req == req.setMaxSyncJumpWidth(None)
        assert req.getMaxSyncJumpWidth() == value

        getter_hints = typing.get_type_hints(CanControllerConfigurationRequirements.getMaxSyncJumpWidth)
        assert getter_hints.get("return") == typing.Optional[Float]

        setter_hints = typing.get_type_hints(CanControllerConfigurationRequirements.setMaxSyncJumpWidth)
        assert setter_hints.get("value") == typing.Optional[Float]
        assert setter_hints.get("return") is CanControllerConfigurationRequirements

    def test_max_sync_jump_width_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.15)"""
        self._assert_docstring(CanControllerConfigurationRequirements.getMaxSyncJumpWidth, MAX_SYNC_JUMP_WIDTH_NOTE)
        self._assert_docstring(CanControllerConfigurationRequirements.setMaxSyncJumpWidth, MAX_SYNC_JUMP_WIDTH_NOTE, "maxSyncJumpWidth")

    def test_get_set_min_number_of_time_quanta_per_bit(self):
        """Test minNumberOfTimeQuantaPerBit default, guarded set chaining, None no-op and typing"""
        req = CanControllerConfigurationRequirements()

        assert req.getMinNumberOfTimeQuantaPerBit() is None

        value = Integer()
        value.setValue("16")
        assert req == req.setMinNumberOfTimeQuantaPerBit(value)
        assert req.getMinNumberOfTimeQuantaPerBit() == value

        assert req == req.setMinNumberOfTimeQuantaPerBit(None)
        assert req.getMinNumberOfTimeQuantaPerBit() == value

        getter_hints = typing.get_type_hints(CanControllerConfigurationRequirements.getMinNumberOfTimeQuantaPerBit)
        assert getter_hints.get("return") == typing.Optional[Integer]

        setter_hints = typing.get_type_hints(CanControllerConfigurationRequirements.setMinNumberOfTimeQuantaPerBit)
        assert setter_hints.get("value") == typing.Optional[Integer]
        assert setter_hints.get("return") is CanControllerConfigurationRequirements

    def test_min_number_of_time_quanta_per_bit_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.15)"""
        self._assert_docstring(CanControllerConfigurationRequirements.getMinNumberOfTimeQuantaPerBit, MIN_NUMBER_OF_TIME_QUANTA_PER_BIT_NOTE)
        self._assert_docstring(CanControllerConfigurationRequirements.setMinNumberOfTimeQuantaPerBit, MIN_NUMBER_OF_TIME_QUANTA_PER_BIT_NOTE, "minNumberOfTimeQuantaPerBit")

    def test_get_set_min_sample_point(self):
        """Test minSamplePoint default, guarded set chaining, None no-op and typing"""
        req = CanControllerConfigurationRequirements()

        assert req.getMinSamplePoint() is None

        value = Float()
        value.setValue("0.7")
        assert req == req.setMinSamplePoint(value)
        assert req.getMinSamplePoint() == value

        assert req == req.setMinSamplePoint(None)
        assert req.getMinSamplePoint() == value

        getter_hints = typing.get_type_hints(CanControllerConfigurationRequirements.getMinSamplePoint)
        assert getter_hints.get("return") == typing.Optional[Float]

        setter_hints = typing.get_type_hints(CanControllerConfigurationRequirements.setMinSamplePoint)
        assert setter_hints.get("value") == typing.Optional[Float]
        assert setter_hints.get("return") is CanControllerConfigurationRequirements

    def test_min_sample_point_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.15)"""
        self._assert_docstring(CanControllerConfigurationRequirements.getMinSamplePoint, MIN_SAMPLE_POINT_NOTE)
        self._assert_docstring(CanControllerConfigurationRequirements.setMinSamplePoint, MIN_SAMPLE_POINT_NOTE, "minSamplePoint")

    def test_get_set_min_sync_jump_width(self):
        """Test minSyncJumpWidth default, guarded set chaining, None no-op and typing"""
        req = CanControllerConfigurationRequirements()

        assert req.getMinSyncJumpWidth() is None

        value = Float()
        value.setValue("0.1")
        assert req == req.setMinSyncJumpWidth(value)
        assert req.getMinSyncJumpWidth() == value

        assert req == req.setMinSyncJumpWidth(None)
        assert req.getMinSyncJumpWidth() == value

        getter_hints = typing.get_type_hints(CanControllerConfigurationRequirements.getMinSyncJumpWidth)
        assert getter_hints.get("return") == typing.Optional[Float]

        setter_hints = typing.get_type_hints(CanControllerConfigurationRequirements.setMinSyncJumpWidth)
        assert setter_hints.get("value") == typing.Optional[Float]
        assert setter_hints.get("return") is CanControllerConfigurationRequirements

    def test_min_sync_jump_width_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.15)"""
        self._assert_docstring(CanControllerConfigurationRequirements.getMinSyncJumpWidth, MIN_SYNC_JUMP_WIDTH_NOTE)
        self._assert_docstring(CanControllerConfigurationRequirements.setMinSyncJumpWidth, MIN_SYNC_JUMP_WIDTH_NOTE, "minSyncJumpWidth")
