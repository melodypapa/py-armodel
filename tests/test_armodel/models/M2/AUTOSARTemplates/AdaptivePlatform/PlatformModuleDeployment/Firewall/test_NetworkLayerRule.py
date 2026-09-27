from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import NetworkLayerRule
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class TestNetworkLayerRule:
    def test_instantiation_and_base(self):
        obj = NetworkLayerRule()
        assert isinstance(obj, ARObject)

    def test_init_has_no_docstring(self):
        assert NetworkLayerRule.__init__.__doc__ is None

    def test_class_docstring_is_spec_note_verbatim(self):
        assert NetworkLayerRule.__doc__.strip() == "Configuration of filter rules on the Network layer Tags: atp.Status=candidate"
