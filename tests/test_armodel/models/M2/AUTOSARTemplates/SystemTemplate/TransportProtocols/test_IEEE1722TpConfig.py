import typing
from inspect import cleandoc
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import TpConfig
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import IEEE1722TpConfig


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestIEEE1722TpConfig:
    def test_docstring_is_spec_note(self):
        # Table 6.274 has no Note row; class Note taken from the XSD IEEE-1722-TP-CONFIG group documentation
        assert cleandoc(IEEE1722TpConfig.__doc__) == "Definition of the IEEE1722Tp protocol."

    def test_heritage(self):
        assert issubclass(IEEE1722TpConfig, TpConfig)

    def test_initialization(self):
        config = IEEE1722TpConfig(None, "IEEE1722TpConfig")
        assert config.getTpConnectionRefs() == []

    def test_get_set_tp_connection_refs(self):
        config = IEEE1722TpConfig(None, "IEEE1722TpConfig")

        result = config.addTpConnectionRef(_ref("/Tp/Conn1", "IEEE-1722-TP-CONNECTION"))
        assert result is config
        refs = config.getTpConnectionRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/Tp/Conn1"
        assert refs[0].getDest() == "IEEE-1722-TP-CONNECTION"

        config.addTpConnectionRef(_ref("/Tp/Conn2", "IEEE-1722-TP-CONNECTION"))
        assert len(config.getTpConnectionRefs()) == 2

        config.addTpConnectionRef(None)
        assert len(config.getTpConnectionRefs()) == 2

    def test_annotations(self):
        hints = typing.get_type_hints(IEEE1722TpConfig.addTpConnectionRef)
        assert hints["value"] == Optional[RefType] or hints["value"] == typing.Optional[RefType]
        hints = typing.get_type_hints(IEEE1722TpConfig.getTpConnectionRefs)
        assert hints["return"] == List[RefType]
