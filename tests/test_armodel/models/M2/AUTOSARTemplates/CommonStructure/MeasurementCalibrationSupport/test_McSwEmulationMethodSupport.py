import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import McParameterElementGroup, McSupportData, McSwEmulationMethodSupport
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def make_ref(value: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    return ref


class TestMcSwEmulationMethodSupportInitialization:
    def test_initialization(self):
        """Test McSwEmulationMethodSupport __init__ defaults"""
        support = McSwEmulationMethodSupport()
        assert support is not None
        assert support.baseReferenceRef is None
        assert support.category is None
        assert support.elementGroups == []
        assert support.referenceTableRef is None
        assert support.shortLabel is None


class TestMcSwEmulationMethodSupportBaseReference:
    def test_get_set_base_reference_ref(self):
        """Test setBaseReferenceRef returns self and getBaseReferenceRef round-trips"""
        support = McSwEmulationMethodSupport()
        ref = make_ref("/Base/Pointer")
        result = support.setBaseReferenceRef(ref)
        assert result is support
        assert support.getBaseReferenceRef() is ref

    def test_set_base_reference_ref_none_is_noop(self):
        """Test setting a None base reference is a no-op"""
        support = McSwEmulationMethodSupport()
        ref = make_ref("/Base/Pointer")
        support.setBaseReferenceRef(ref)
        support.setBaseReferenceRef(None)
        assert support.getBaseReferenceRef() is ref


class TestMcSwEmulationMethodSupportCategory:
    def test_get_set_category(self):
        """Test setCategory returns self and getCategory round-trips"""
        support = McSwEmulationMethodSupport()
        category = Identifier().setValue("DOUBLE_POINTERED")
        result = support.setCategory(category)
        assert result is support
        assert support.getCategory().getValue() == "DOUBLE_POINTERED"

    def test_set_category_none_is_noop(self):
        """Test setting a None category is a no-op"""
        support = McSwEmulationMethodSupport()
        support.setCategory(Identifier().setValue("DOUBLE_POINTERED"))
        support.setCategory(None)
        assert support.getCategory().getValue() == "DOUBLE_POINTERED"


class TestMcSwEmulationMethodSupportElementGroup:
    def test_add_get_element_group(self):
        """Test addElementGroup appends and returns self for chaining"""
        support = McSwEmulationMethodSupport()
        group = McParameterElementGroup()
        result = support.addElementGroup(group)
        assert result is support
        assert support.getElementGroups() == [group]

    def test_add_element_group_none_is_noop(self):
        """Test adding a None element group is a no-op"""
        support = McSwEmulationMethodSupport()
        support.addElementGroup(None)
        assert support.getElementGroups() == []


class TestMcSwEmulationMethodSupportReferenceTable:
    def test_get_set_reference_table_ref(self):
        """Test setReferenceTableRef returns self and getReferenceTableRef round-trips"""
        support = McSwEmulationMethodSupport()
        ref = make_ref("/Reference/Table")
        result = support.setReferenceTableRef(ref)
        assert result is support
        assert support.getReferenceTableRef() is ref

    def test_set_reference_table_ref_none_is_noop(self):
        """Test setting a None reference table ref is a no-op"""
        support = McSwEmulationMethodSupport()
        ref = make_ref("/Reference/Table")
        support.setReferenceTableRef(ref)
        support.setReferenceTableRef(None)
        assert support.getReferenceTableRef() is ref


class TestMcSwEmulationMethodSupportShortLabel:
    def test_get_set_short_label(self):
        """Test setShortLabel returns self and getShortLabel round-trips"""
        support = McSwEmulationMethodSupport()
        result = support.setShortLabel(Identifier().setValue("EmuLabel"))
        assert result is support
        assert support.getShortLabel().getValue() == "EmuLabel"

    def test_set_short_label_none_is_noop(self):
        """Test setting a None short label is a no-op"""
        support = McSwEmulationMethodSupport()
        support.setShortLabel(Identifier().setValue("EmuLabel"))
        support.setShortLabel(None)
        assert support.getShortLabel().getValue() == "EmuLabel"


class TestMcParameterElementGroupInitialization:
    def test_initialization(self):
        """Test McParameterElementGroup __init__ defaults"""
        group = McParameterElementGroup()
        assert group is not None
        assert group.ramLocationRef is None
        assert group.romLocationRef is None
        assert group.shortLabel is None


class TestMcParameterElementGroupRamLocation:
    def test_get_set_ram_location_ref(self):
        """Test setRamLocationRef returns self and getRamLocationRef round-trips"""
        group = McParameterElementGroup()
        ref = make_ref("/Ram/Location")
        result = group.setRamLocationRef(ref)
        assert result is group
        assert group.getRamLocationRef() is ref

    def test_set_ram_location_ref_none_is_noop(self):
        """Test setting a None RAM location ref is a no-op"""
        group = McParameterElementGroup()
        ref = make_ref("/Ram/Location")
        group.setRamLocationRef(ref)
        group.setRamLocationRef(None)
        assert group.getRamLocationRef() is ref


class TestMcParameterElementGroupRomLocation:
    def test_get_set_rom_location_ref(self):
        """Test setRomLocationRef returns self and getRomLocationRef round-trips"""
        group = McParameterElementGroup()
        ref = make_ref("/Rom/Location")
        result = group.setRomLocationRef(ref)
        assert result is group
        assert group.getRomLocationRef() is ref

    def test_set_rom_location_ref_none_is_noop(self):
        """Test setting a None ROM location ref is a no-op"""
        group = McParameterElementGroup()
        ref = make_ref("/Rom/Location")
        group.setRomLocationRef(ref)
        group.setRomLocationRef(None)
        assert group.getRomLocationRef() is ref


class TestMcParameterElementGroupShortLabel:
    def test_get_set_short_label(self):
        """Test setShortLabel returns self and getShortLabel round-trips"""
        group = McParameterElementGroup()
        result = group.setShortLabel(Identifier().setValue("GroupLabel"))
        assert result is group
        assert group.getShortLabel().getValue() == "GroupLabel"

    def test_set_short_label_none_is_noop(self):
        """Test setting a None short label is a no-op"""
        group = McParameterElementGroup()
        group.setShortLabel(Identifier().setValue("GroupLabel"))
        group.setShortLabel(None)
        assert group.getShortLabel().getValue() == "GroupLabel"


class TestMcSwEmulationMethodSupportRoundTrip:
    def test_round_trip_via_bsw_implementation(self):
        """Test parse -> write -> re-parse round trip of McSwEmulationMethodSupport including its element groups."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        impl = ar_root.createBswImplementation("test_impl")
        mc_support = McSupportData()
        impl.setMcSupport(mc_support)

        support = McSwEmulationMethodSupport()
        support.setShortLabel(Identifier().setValue("EmuLabel"))
        support.setCategory(Identifier().setValue("initRam"))
        support.setBaseReferenceRef(make_ref("/Base/Pointer"))
        support.setReferenceTableRef(make_ref("/Reference/Table"))
        group = McParameterElementGroup()
        group.setShortLabel(Identifier().setValue("GroupLabel"))
        group.setRamLocationRef(make_ref("/Ram/Location"))
        group.setRomLocationRef(make_ref("/Rom/Location"))
        support.addElementGroup(group)
        mc_support.addEmulationSupport(support)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            mc_support_2 = document_2.getARPackages()[0].getBswImplementations()[0].getMcSupport()

            assert mc_support_2 is not None
            assert len(mc_support_2.getEmulationSupports()) == 1
            support_2 = mc_support_2.getEmulationSupports()[0]
            assert support_2.getShortLabel().getValue() == "EmuLabel"
            assert support_2.getCategory().getValue() == "initRam"
            assert support_2.getBaseReferenceRef().getValue() == "/Base/Pointer"
            assert support_2.getReferenceTableRef().getValue() == "/Reference/Table"
            assert len(support_2.getElementGroups()) == 1
            group_2 = support_2.getElementGroups()[0]
            assert group_2.getShortLabel().getValue() == "GroupLabel"
            assert group_2.getRamLocationRef().getValue() == "/Ram/Location"
            assert group_2.getRomLocationRef().getValue() == "/Rom/Location"
        finally:
            import os

            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty_element_groups_emits_no_wrapper(self):
        """Test an empty elementGroups list round-trips to no ELEMENT-GROUPS wrapper element."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        impl = ar_root.createBswImplementation("test_impl")
        mc_support = McSupportData()
        impl.setMcSupport(mc_support)

        support = McSwEmulationMethodSupport()
        support.setShortLabel(Identifier().setValue("EmuLabel"))
        mc_support.addEmulationSupport(support)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            with open(file_path, "r", encoding="utf-8") as file_handle:
                content = file_handle.read()
            assert "ELEMENT-GROUPS" not in content

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            mc_support_2 = document_2.getARPackages()[0].getBswImplementations()[0].getMcSupport()
            support_2 = mc_support_2.getEmulationSupports()[0]
            assert support_2.getElementGroups() == []
            assert support_2.getBaseReferenceRef() is None
            assert support_2.getReferenceTableRef() is None
        finally:
            import os

            if os.path.exists(file_path):
                os.remove(file_path)
