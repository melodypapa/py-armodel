from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import McFunctionDataRefSet
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


def make_ref(value: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    return ref


class TestMcFunctionDataRefSetInitialization:
    def test_initialization(self):
        """Test McFunctionDataRefSet __init__ defaults"""
        data_ref_set = McFunctionDataRefSet()
        assert data_ref_set is not None
        assert data_ref_set.flatMapEntryRefs == []
        assert data_ref_set.mcDataInstanceRefs == []


class TestMcFunctionDataRefSetFlatMapEntry:
    def test_add_get_flat_map_entry_ref(self):
        """Test addFlatMapEntryRef appends and returns self for chaining"""
        data_ref_set = McFunctionDataRefSet()
        ref = make_ref("/Flat/Entry1")
        result = data_ref_set.addFlatMapEntryRef(ref)
        assert result is data_ref_set
        assert data_ref_set.getFlatMapEntryRefs() == [ref]

    def test_add_flat_map_entry_ref_none_is_noop(self):
        """Test adding a None flat map entry ref is a no-op"""
        data_ref_set = McFunctionDataRefSet()
        data_ref_set.addFlatMapEntryRef(None)
        assert data_ref_set.getFlatMapEntryRefs() == []


class TestMcFunctionDataRefSetMcDataInstance:
    def test_add_get_mc_data_instance_ref(self):
        """Test addMcDataInstanceRef appends and returns self for chaining"""
        data_ref_set = McFunctionDataRefSet()
        ref = make_ref("/MC/Instance1")
        result = data_ref_set.addMcDataInstanceRef(ref)
        assert result is data_ref_set
        assert data_ref_set.getMcDataInstanceRefs() == [ref]

    def test_add_mc_data_instance_ref_none_is_noop(self):
        """Test adding a None mc data instance ref is a no-op"""
        data_ref_set = McFunctionDataRefSet()
        data_ref_set.addMcDataInstanceRef(None)
        assert data_ref_set.getMcDataInstanceRefs() == []
