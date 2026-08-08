import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import McFunction
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import McFunctionDataRefSet
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def make_ref(value: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    return ref


class TestMcFunctionInitialization:
    def test_initialization(self):
        """Test McFunction __init__ defaults"""
        func = McFunction(AUTOSAR.getInstance(), "Fn1")
        assert func is not None
        assert func.getShortName() == "Fn1"
        assert func.defCalprmSet is None
        assert func.inMeasurementSet is None
        assert func.locMeasurementSet is None
        assert func.outMeasurementSet is None
        assert func.refCalprmSet is None
        assert func.subFunctionRefs == []


class TestMcFunctionDefCalprmSet:
    def test_get_set_def_calprm_set(self):
        """Test setDefCalprmSet returns self and getDefCalprmSet round-trips"""
        func = McFunction(AUTOSAR.getInstance(), "Fn1")
        data_ref_set = McFunctionDataRefSet()
        result = func.setDefCalprmSet(data_ref_set)
        assert result is func
        assert func.getDefCalprmSet() is data_ref_set

    def test_set_def_calprm_set_none_is_noop(self):
        """Test setting a None defCalprmSet is a no-op"""
        func = McFunction(AUTOSAR.getInstance(), "Fn1")
        data_ref_set = McFunctionDataRefSet()
        func.setDefCalprmSet(data_ref_set)
        func.setDefCalprmSet(None)
        assert func.getDefCalprmSet() is data_ref_set


class TestMcFunctionInMeasurementSet:
    def test_get_set_in_measurement_set(self):
        """Test setInMeasurementSet returns self and getInMeasurementSet round-trips"""
        func = McFunction(AUTOSAR.getInstance(), "Fn1")
        data_ref_set = McFunctionDataRefSet()
        result = func.setInMeasurementSet(data_ref_set)
        assert result is func
        assert func.getInMeasurementSet() is data_ref_set

    def test_set_in_measurement_set_none_is_noop(self):
        """Test setting a None inMeasurementSet is a no-op"""
        func = McFunction(AUTOSAR.getInstance(), "Fn1")
        data_ref_set = McFunctionDataRefSet()
        func.setInMeasurementSet(data_ref_set)
        func.setInMeasurementSet(None)
        assert func.getInMeasurementSet() is data_ref_set


class TestMcFunctionLocMeasurementSet:
    def test_get_set_loc_measurement_set(self):
        """Test setLocMeasurementSet returns self and getLocMeasurementSet round-trips"""
        func = McFunction(AUTOSAR.getInstance(), "Fn1")
        data_ref_set = McFunctionDataRefSet()
        result = func.setLocMeasurementSet(data_ref_set)
        assert result is func
        assert func.getLocMeasurementSet() is data_ref_set

    def test_set_loc_measurement_set_none_is_noop(self):
        """Test setting a None locMeasurementSet is a no-op"""
        func = McFunction(AUTOSAR.getInstance(), "Fn1")
        data_ref_set = McFunctionDataRefSet()
        func.setLocMeasurementSet(data_ref_set)
        func.setLocMeasurementSet(None)
        assert func.getLocMeasurementSet() is data_ref_set


class TestMcFunctionOutMeasurementSet:
    def test_get_set_out_measurement_set(self):
        """Test setOutMeasurementSet returns self and getOutMeasurementSet round-trips"""
        func = McFunction(AUTOSAR.getInstance(), "Fn1")
        data_ref_set = McFunctionDataRefSet()
        result = func.setOutMeasurementSet(data_ref_set)
        assert result is func
        assert func.getOutMeasurementSet() is data_ref_set

    def test_set_out_measurement_set_none_is_noop(self):
        """Test setting a None outMeasurementSet is a no-op"""
        func = McFunction(AUTOSAR.getInstance(), "Fn1")
        data_ref_set = McFunctionDataRefSet()
        func.setOutMeasurementSet(data_ref_set)
        func.setOutMeasurementSet(None)
        assert func.getOutMeasurementSet() is data_ref_set


class TestMcFunctionRefCalprmSet:
    def test_get_set_ref_calprm_set(self):
        """Test setRefCalprmSet returns self and getRefCalprmSet round-trips"""
        func = McFunction(AUTOSAR.getInstance(), "Fn1")
        data_ref_set = McFunctionDataRefSet()
        result = func.setRefCalprmSet(data_ref_set)
        assert result is func
        assert func.getRefCalprmSet() is data_ref_set

    def test_set_ref_calprm_set_none_is_noop(self):
        """Test setting a None refCalprmSet is a no-op"""
        func = McFunction(AUTOSAR.getInstance(), "Fn1")
        data_ref_set = McFunctionDataRefSet()
        func.setRefCalprmSet(data_ref_set)
        func.setRefCalprmSet(None)
        assert func.getRefCalprmSet() is data_ref_set


class TestMcFunctionSubFunction:
    def test_add_get_sub_function_ref(self):
        """Test addSubFunctionRef appends and returns self for chaining"""
        func = McFunction(AUTOSAR.getInstance(), "Fn1")
        ref = make_ref("/Fn2")
        result = func.addSubFunctionRef(ref)
        assert result is func
        assert func.getSubFunctionRefs() == [ref]

    def test_add_sub_function_ref_none_is_noop(self):
        """Test adding a None sub-function ref is a no-op"""
        func = McFunction(AUTOSAR.getInstance(), "Fn1")
        func.addSubFunctionRef(None)
        assert func.getSubFunctionRefs() == []


class TestMcFunctionRoundTrip:
    def test_round_trip_via_ar_package(self):
        """Test parse -> write -> re-parse round trip of McFunction as an ARPackage element."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        func = ar_root.createMcFunction("Fn1")

        def_calprm_set = McFunctionDataRefSet()
        def_calprm_set.addFlatMapEntryRef(make_ref("/Flat/Cal1"))
        def_calprm_set.addMcDataInstanceRef(make_ref("/MC/Cal1"))
        func.setDefCalprmSet(def_calprm_set)
        func.setRefCalprmSet(McFunctionDataRefSet())
        func.addSubFunctionRef(make_ref("/Fn2"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            func_2 = document_2.getARPackages()[0].getMcFunctions()[0]
            assert func_2.getShortName() == "Fn1"
            assert func_2.getDefCalprmSet().getFlatMapEntryRefs()[0].getValue() == "/Flat/Cal1"
            assert func_2.getDefCalprmSet().getMcDataInstanceRefs()[0].getValue() == "/MC/Cal1"
            assert func_2.getRefCalprmSet() is not None
            assert func_2.getInMeasurementSet() is None
            assert func_2.getLocMeasurementSet() is None
            assert func_2.getOutMeasurementSet() is None
            assert func_2.getSubFunctionRefs()[0].getValue() == "/Fn2"
        finally:
            import os

            if os.path.exists(file_path):
                os.remove(file_path)
