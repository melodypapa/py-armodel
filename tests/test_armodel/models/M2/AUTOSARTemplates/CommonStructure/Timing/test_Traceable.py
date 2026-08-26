"""
This module contains tests for the Traceable class in the
AUTOSAR CommonStructure.Timing module.
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.RequirementsTracing import (
    Traceable,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestTraceable:
    """
    Test class for Traceable functionality.
    """

    def test_abstract_initialization(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        try:
            _obj = Traceable(ar_root, "TestTraceable")
            assert False, "Traceable should not be instantiable"
        except TypeError:
            pass

    def test_concrete_subclass_initialization(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteTraceable(Traceable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteTraceable(ar_root, "TestName")
        assert obj.getShortName() == "TestName"

    def test_trace_refs(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteTraceable(Traceable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteTraceable(ar_root, "TestName")

        ref = RefType()
        ref.setDest("TRACEABLE")
        ref.setValue("/PKG/TEST")

        returned = obj.addTraceRef(ref)
        assert returned is obj
        assert len(obj.getTraceRefs()) == 1
        assert obj.getTraceRefs()[0] is ref

        obj.addTraceRef(None)
        assert len(obj.getTraceRefs()) == 1

    def _round_trip(self, elem):
        xml_str = ET.tostring(elem).decode()
        idx = xml_str.find(">")
        xml_str = xml_str[:idx] + ' xmlns="http://autosar.org/schema/r4.0"' + xml_str[idx:]
        return ET.fromstring(xml_str)

    def test_trace_reader_writer_round_trip(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteTraceable(Traceable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteTraceable(ar_root, "TC")
        ref = RefType()
        ref.setValue("/PKG/TARGET")
        obj.addTraceRef(ref)

        elem = ET.Element("TEST")
        ARXMLWriter().writeTraceable(elem, obj)

        refs_tag = elem.find("TRACE-REFS")
        assert refs_tag is not None
        assert refs_tag.find("TRACE-REF").text == "/PKG/TARGET"

        parsed = self._round_trip(elem)
        obj2 = ConcreteTraceable(ar_root, "TC2")
        ARXMLParser().readTraceable(parsed, obj2)
        assert len(obj2.getTraceRefs()) == 1
        assert obj2.getTraceRefs()[0].getValue() == "/PKG/TARGET"
        assert obj2.getTraceRefs()[0].getDest() is None

    def test_traceable_text_reuses_base(self):
        from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.RequirementsTracing import (
            TraceableText,
        )

        tt = TraceableText()
        ref = RefType()
        ref.setValue("/PKG/TARGET")
        tt.addTraceRef(ref)

        elem = ET.Element("TRACE")
        ARXMLWriter().writeTraceable(elem, tt)
        assert elem.find("TRACE-REFS/TRACE-REF").text == "/PKG/TARGET"

        parsed = self._round_trip(elem)
        tt2 = TraceableText()
        ARXMLParser().readTraceable(parsed, tt2)
        assert len(tt2.getTraceRefs()) == 1
        assert tt2.getTraceRefs()[0].getValue() == "/PKG/TARGET"
