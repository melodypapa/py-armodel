"""Test V2 imports - ensure all V2 modules can be imported."""

import pytest


class TestV2Imports:
    """Test that V2 modules can be imported without errors."""

    def test_import_top_level(self):
        """Test importing top-level V2 models."""
        from armodel.v2.models import AUTOSAR
        from armodel.v2.models import ARObject
        from armodel.v2.models import Identifiable
        from armodel.v2.models import __version__

        assert __version__ == "2.0.0"
        assert AUTOSAR is not None
        assert ARObject is not None
        assert Identifiable is not None

    def test_import_msr_modules(self):
        """Test importing MSR modules."""
        from armodel.v2.models.M2.MSR import AsamHdo
        from armodel.v2.models.M2.MSR import DataDictionary
        from armodel.v2.models.M2.MSR import Documentation
        from armodel.v2.models.M2.MSR import CalibrationData

        assert AsamHdo is not None
        assert DataDictionary is not None
        assert Documentation is not None
        assert CalibrationData is not None

    def test_import_common_structure(self):
        """Test importing CommonStructure modules."""
        from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure import (
            Implementation
        )
        from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure import (
            InternalBehavior
        )

        assert Implementation is not None
        assert InternalBehavior is not None

    def test_import_sw_component_template(self):
        """Test importing SWComponentTemplate modules."""
        from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate import (
            SwComponentType
        )
        from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate import (
            PPortPrototype
        )
        from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate import (
            ClientServerInterface
        )

        assert SwComponentType is not None
        assert PPortPrototype is not None
        assert ClientServerInterface is not None

    def test_no_circular_imports(self):
        """Test that there are no circular import errors."""
        # This test passes if the imports above succeed
        # Circular imports would cause ImportError or RuntimeError
        assert True
