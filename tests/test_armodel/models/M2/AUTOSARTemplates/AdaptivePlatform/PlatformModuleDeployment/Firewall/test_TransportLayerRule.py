from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import TransportLayerRule
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class TestTransportLayerRule:
    def test_instantiation_and_base(self):
        obj = TransportLayerRule()
        assert isinstance(obj, ARObject)

    def test_init_has_no_docstring(self):
        assert TransportLayerRule.__init__.__doc__ is None

    def test_class_docstring_is_spec_note_verbatim(self):
        assert TransportLayerRule.__doc__.strip() == "Configuration of filter rules on Transport Layer level. Tags: atp.Status=candidate"
