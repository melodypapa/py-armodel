"""Test V2 API compatibility with V1."""

import pytest


class TestV2APICompatibility:
    """Test that V2 maintains V1 API compatibility."""

    def test_v2_has_autosar(self):
        """Test V2 has AUTOSAR class like V1."""
        from armodel.v2.models import AUTOSAR
        from armodel.models import AUTOSAR as V1_AUTOSAR

        # Both should have getInstance method
        assert hasattr(AUTOSAR, "getInstance")
        assert hasattr(V1_AUTOSAR, "getInstance")

        # Both should be singletons
        v2_instance = AUTOSAR.getInstance()
        v1_instance = V1_AUTOSAR.getInstance()

        assert v2_instance is not None
        assert v1_instance is not None

    def test_v2_has_ar_object(self):
        """Test V2 has ARObject base class like V1."""
        from armodel.v2.models import ARObject as V2_ARObject
        from armodel.models import ARObject as V1_ARObject

        # Both should have getTagName method
        assert hasattr(V2_ARObject, "getTagName")
        assert hasattr(V1_ARObject, "getTagName")

        # V2 ARObject should exist and be importable
        assert V2_ARObject is not None

    def test_v2_has_sw_component_type(self):
        """Test V2 has SwComponentType like V1."""
        from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import (
            SwComponentType as V2_SwComponentType,
        )
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwComponentType import (
            SwComponentType as V1_SwComponentType,
        )

        # Both should have short_name property (V2 uses Pythonic properties)
        assert hasattr(V2_SwComponentType, "short_name")
        # V1 uses getShortName method
        assert hasattr(V1_SwComponentType, "getShortName")

        # Both should exist and be importable
        assert V2_SwComponentType is not None
        assert V1_SwComponentType is not None

    def test_v2_version_is_defined(self):
        """Test V2 has __version__ defined."""
        from armodel.v2.models import __version__

        assert __version__ is not None
        assert isinstance(__version__, str)
        assert __version__.startswith("2.")
