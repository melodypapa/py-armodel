from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall import TransportLayerRule, UdpRule
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class TestUdpRule:
    def test_instantiation_and_base(self):
        obj = UdpRule()
        assert isinstance(obj, ARObject)
        assert isinstance(obj, TransportLayerRule)

    def test_init_has_no_docstring(self):
        assert UdpRule.__init__.__doc__ is None

    def test_class_docstring_is_spec_note_verbatim(self):
        assert UdpRule.__doc__.strip() == "Configuration of UDP filter rules. Tags: atp.Status=candidate"
