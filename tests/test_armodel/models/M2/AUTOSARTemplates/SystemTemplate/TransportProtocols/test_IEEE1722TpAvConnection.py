import typing
from inspect import cleandoc
from typing import List, Optional

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import (
    IEEE1722TpAvConnection,
    IEEE1722TpConnection,
)


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _time(value):
    t = TimeValue()
    t.setValue(value)
    return t


class TestIEEE1722TpAvConnection:
    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.276, p.639 — class Note verbatim from the markdown
        assert cleandoc(IEEE1722TpAvConnection.__doc__) == "AV IEEE1722Tp connection. Tags: atp.Status=candidate"

    def test_abstract(self):
        with pytest.raises(TypeError):
            IEEE1722TpAvConnection(None, "AvConn")

    def test_heritage(self):
        assert issubclass(IEEE1722TpAvConnection, IEEE1722TpConnection)

    def test_initialization(self):
        class _AvConn(IEEE1722TpAvConnection):
            pass

        connection = _AvConn(None, "AvConn")
        assert connection.getMaxTransitTime() is None
        assert connection.getSduRefs() == []

    def test_base_accessors(self):
        class _AvConn(IEEE1722TpAvConnection):
            pass

        connection = _AvConn(None, "AvConn")

        max_transit_time = _time(0.001)
        assert connection.setMaxTransitTime(max_transit_time) is connection
        assert connection.getMaxTransitTime() is max_transit_time
        assert connection.setMaxTransitTime(None) is connection
        assert connection.getMaxTransitTime() is max_transit_time

        assert connection.addSduRef(_ref("/Pdu/Pt1", "PDU-TRIGGERING")) is connection
        assert connection.addSduRef(_ref("/Pdu/Pt2", "PDU-TRIGGERING")) is connection
        sdu_refs = connection.getSduRefs()
        assert len(sdu_refs) == 2
        assert sdu_refs[0].getValue() == "/Pdu/Pt1"
        assert sdu_refs[1].getValue() == "/Pdu/Pt2"
        assert connection.addSduRef(None) is connection
        assert len(connection.getSduRefs()) == 2

    def test_annotations(self):
        hints = typing.get_type_hints(IEEE1722TpAvConnection.getMaxTransitTime)
        assert hints["return"] == Optional[TimeValue]
        hints = typing.get_type_hints(IEEE1722TpAvConnection.addSduRef)
        assert hints["value"] == Optional[RefType]
        hints = typing.get_type_hints(IEEE1722TpAvConnection.getSduRefs)
        assert hints["return"] == List[RefType]
