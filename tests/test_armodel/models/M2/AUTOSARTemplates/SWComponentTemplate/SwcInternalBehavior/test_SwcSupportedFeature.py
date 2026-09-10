import pytest

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions import SwcSupportedFeature


class TestSwcSupportedFeature:
    def test_abstract_class_and_spec_note(self):
        with pytest.raises(TypeError):
            SwcSupportedFeature()

        assert SwcSupportedFeature.__doc__.strip() == ("This meta-class represents a abstract base class for features that can be supported by a RunnableEntity.")

    def test_concrete_child_can_initialize_through_abstract_base(self):
        class ConcreteSupportedFeature(SwcSupportedFeature):
            pass

        feature = ConcreteSupportedFeature()
        assert isinstance(feature, SwcSupportedFeature)
