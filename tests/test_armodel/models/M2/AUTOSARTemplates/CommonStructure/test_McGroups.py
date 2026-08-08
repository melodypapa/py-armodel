import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.McGroups import McGroup, McGroupDataRefSet
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def make_ref(value: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    return ref


class TestMcGroupInitialization:
    def test_initialization(self):
        """Test McGroup __init__ defaults"""
        group = McGroup(AUTOSAR.getInstance(), "Grp1")
        assert group is not None
        assert group.getShortName() == "Grp1"
        assert group.mcFunctionRefs == []
        assert group.refCalprmSet is None
        assert group.refMeasurementSet is None
        assert group.subGroupRefs == []


class TestMcGroupMcFunctionRef:
    def test_add_get_mc_function_ref(self):
        """Test addMcFunctionRef appends and returns self for chaining"""
        group = McGroup(AUTOSAR.getInstance(), "Grp1")
        ref = make_ref("/Fn1")
        result = group.addMcFunctionRef(ref)
        assert result is group
        assert group.getMcFunctionRefs() == [ref]

    def test_add_mc_function_ref_none_is_noop(self):
        """Test adding a None mcFunction ref is a no-op"""
        group = McGroup(AUTOSAR.getInstance(), "Grp1")
        group.addMcFunctionRef(None)
        assert group.getMcFunctionRefs() == []


class TestMcGroupRefCalprmSet:
    def test_get_set_ref_calprm_set(self):
        """Test setRefCalprmSet returns self and getRefCalprmSet round-trips"""
        group = McGroup(AUTOSAR.getInstance(), "Grp1")
        data_ref_set = McGroupDataRefSet()
        result = group.setRefCalprmSet(data_ref_set)
        assert result is group
        assert group.getRefCalprmSet() is data_ref_set

    def test_set_ref_calprm_set_none_is_noop(self):
        """Test setting a None refCalprmSet is a no-op"""
        group = McGroup(AUTOSAR.getInstance(), "Grp1")
        data_ref_set = McGroupDataRefSet()
        group.setRefCalprmSet(data_ref_set)
        group.setRefCalprmSet(None)
        assert group.getRefCalprmSet() is data_ref_set


class TestMcGroupRefMeasurementSet:
    def test_get_set_ref_measurement_set(self):
        """Test setRefMeasurementSet returns self and getRefMeasurementSet round-trips"""
        group = McGroup(AUTOSAR.getInstance(), "Grp1")
        data_ref_set = McGroupDataRefSet()
        result = group.setRefMeasurementSet(data_ref_set)
        assert result is group
        assert group.getRefMeasurementSet() is data_ref_set

    def test_set_ref_measurement_set_none_is_noop(self):
        """Test setting a None refMeasurementSet is a no-op"""
        group = McGroup(AUTOSAR.getInstance(), "Grp1")
        data_ref_set = McGroupDataRefSet()
        group.setRefMeasurementSet(data_ref_set)
        group.setRefMeasurementSet(None)
        assert group.getRefMeasurementSet() is data_ref_set


class TestMcGroupSubGroupRef:
    def test_add_get_sub_group_ref(self):
        """Test addSubGroupRef appends and returns self for chaining"""
        group = McGroup(AUTOSAR.getInstance(), "Grp1")
        ref = make_ref("/Grp2")
        result = group.addSubGroupRef(ref)
        assert result is group
        assert group.getSubGroupRefs() == [ref]

    def test_add_sub_group_ref_none_is_noop(self):
        """Test adding a None sub-group ref is a no-op"""
        group = McGroup(AUTOSAR.getInstance(), "Grp1")
        group.addSubGroupRef(None)
        assert group.getSubGroupRefs() == []


class TestMcGroupDataRefSetInitialization:
    def test_initialization(self):
        """Test McGroupDataRefSet __init__ defaults"""
        data_ref_set = McGroupDataRefSet()
        assert data_ref_set is not None
        assert data_ref_set.flatMapEntryRefs == []
        assert data_ref_set.mcDataInstanceRefs == []


class TestMcGroupDataRefSetFlatMapEntry:
    def test_add_get_flat_map_entry_ref(self):
        """Test addFlatMapEntryRef appends and returns self for chaining"""
        data_ref_set = McGroupDataRefSet()
        ref = make_ref("/Flat/Cal1")
        result = data_ref_set.addFlatMapEntryRef(ref)
        assert result is data_ref_set
        assert data_ref_set.getFlatMapEntryRefs() == [ref]

    def test_add_flat_map_entry_ref_none_is_noop(self):
        """Test adding a None flatMapEntry ref is a no-op"""
        data_ref_set = McGroupDataRefSet()
        data_ref_set.addFlatMapEntryRef(None)
        assert data_ref_set.getFlatMapEntryRefs() == []


class TestMcGroupDataRefSetMcDataInstance:
    def test_add_get_mc_data_instance_ref(self):
        """Test addMcDataInstanceRef appends and returns self for chaining"""
        data_ref_set = McGroupDataRefSet()
        ref = make_ref("/MC/Cal1")
        result = data_ref_set.addMcDataInstanceRef(ref)
        assert result is data_ref_set
        assert data_ref_set.getMcDataInstanceRefs() == [ref]

    def test_add_mc_data_instance_ref_none_is_noop(self):
        """Test adding a None mcDataInstance ref is a no-op"""
        data_ref_set = McGroupDataRefSet()
        data_ref_set.addMcDataInstanceRef(None)
        assert data_ref_set.getMcDataInstanceRefs() == []


class TestMcGroupRoundTrip:
    def test_round_trip_via_ar_package(self):
        """Test parse -> write -> re-parse round trip of McGroup as an ARPackage element."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        group = ar_root.createMcGroup("Grp1")

        ref_calprm_set = McGroupDataRefSet()
        ref_calprm_set.addFlatMapEntryRef(make_ref("/Flat/Cal1"))
        ref_calprm_set.addMcDataInstanceRef(make_ref("/MC/Cal1"))
        group.setRefCalprmSet(ref_calprm_set)
        group.setRefMeasurementSet(McGroupDataRefSet())
        group.addMcFunctionRef(make_ref("/Fn1"))
        group.addSubGroupRef(make_ref("/Grp2"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            group_2 = document_2.getARPackages()[0].getMcGroups()[0]
            assert group_2.getShortName() == "Grp1"
            assert group_2.getRefCalprmSet().getFlatMapEntryRefs()[0].getValue() == "/Flat/Cal1"
            assert group_2.getRefCalprmSet().getMcDataInstanceRefs()[0].getValue() == "/MC/Cal1"
            assert group_2.getRefMeasurementSet() is not None
            assert group_2.getMcFunctionRefs()[0].getValue() == "/Fn1"
            assert group_2.getSubGroupRefs()[0].getValue() == "/Grp2"
        finally:
            import os

            if os.path.exists(file_path):
                os.remove(file_path)
