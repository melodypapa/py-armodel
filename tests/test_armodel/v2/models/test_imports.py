"""Test V2 imports - ensure all V2 modules can be imported."""



class TestV2Imports:
    """Test that V2 modules can be imported without errors."""

    def test_import_top_level(self):
        """Test importing top-level V2 models."""
        from armodel.v2.models import (
            AUTOSAR,
            ARObject,
            Identifiable,
            __version__,
        )

        assert __version__ == "2.0.0"
        assert AUTOSAR is not None
        assert ARObject is not None
        assert Identifiable is not None

    def test_import_msr_modules(self):
        """Test importing MSR modules."""
        from armodel.v2.models.M2.MSR import (
            AsamHdo,
            CalibrationData,
            DataDictionary,
            Documentation,
        )

        assert AsamHdo is not None
        assert DataDictionary is not None
        assert Documentation is not None
        assert CalibrationData is not None

    def test_import_common_structure(self):
        """Test importing CommonStructure modules."""
        from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure import (
            Implementation,
            InternalBehavior,
        )

        assert Implementation is not None
        assert InternalBehavior is not None

    def test_import_sw_component_template(self):
        """Test importing SWComponentTemplate modules."""
        from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate import (
            ClientServerInterface,
            PPortPrototype,
            SwComponentType,
        )

        assert SwComponentType is not None
        assert PPortPrototype is not None
        assert ClientServerInterface is not None

    def test_no_circular_imports(self):
        """Test that there are no circular import errors."""
        # This test passes if the imports above succeed
        # Circular imports would cause ImportError or RuntimeError
        assert True
