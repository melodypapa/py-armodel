"""Tests for parsing SignalServiceTranslation classes (SystemTemplate 6.339-6.343)."""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

ARXML = """<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="{ns}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="{ns} AUTOSAR_4-3-0.xsd">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>Translation</SHORT-NAME>
      <ELEMENTS>
        <SIGNAL-SERVICE-TRANSLATION-PROPS-SET>
          <SHORT-NAME>propsSet</SHORT-NAME>
          <SIGNAL-SERVICE-TRANSLATION-PROPS>
            <SHORT-NAME>props</SHORT-NAME>
            <CONTROL-CONSUMED-EVENT-GROUP-REFS>
              <CONTROL-CONSUMED-EVENT-GROUP-REF DEST="CONSUMED-EVENT-GROUP">/pkg/ConsumedEventGroup</CONTROL-CONSUMED-EVENT-GROUP-REF>
            </CONTROL-CONSUMED-EVENT-GROUP-REFS>
            <CONTROL-PNC-REFS>
              <CONTROL-PNC-REF DEST="PNC-MAPPING-IDENT">/pkg/PncMapping</CONTROL-PNC-REF>
            </CONTROL-PNC-REFS>
            <CONTROL-PROVIDED-EVENT-GROUP-REFS>
              <CONTROL-PROVIDED-EVENT-GROUP-REF DEST="EVENT-HANDLER">/pkg/EventHandler</CONTROL-PROVIDED-EVENT-GROUP-REF>
            </CONTROL-PROVIDED-EVENT-GROUP-REFS>
            <SERVICE-CONTROL>translationStart</SERVICE-CONTROL>
            <SIGNAL-SERVICE-TRANSLATION-EVENT-PROPS>
              <SHORT-NAME>eventProps</SHORT-NAME>
              <SIGNAL-SERVICE-TRANSLATION-ELEMENT-PROPS>
                <SHORT-NAME>elementProps</SHORT-NAME>
                <FILTER>
                  <DATA-FILTER-TYPE>always</DATA-FILTER-TYPE>
                </FILTER>
                <TRANSMISSION-TRIGGER>true</TRANSMISSION-TRIGGER>
              </SIGNAL-SERVICE-TRANSLATION-ELEMENT-PROPS>
              <SAFE-TRANSLATION>true</SAFE-TRANSLATION>
              <SECURE-TRANSLATION>false</SECURE-TRANSLATION>
              <TRANSLATION-TARGET>
                <TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/pkg/TargetDataPrototype</TARGET-DATA-PROTOTYPE-REF>
              </TRANSLATION-TARGET>
            </SIGNAL-SERVICE-TRANSLATION-EVENT-PROPS>
          </SIGNAL-SERVICE-TRANSLATION-PROPS>
        </SIGNAL-SERVICE-TRANSLATION-PROPS-SET>
      </ELEMENTS>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
""".format(
    ns=NS
)


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def loaded_document(tmp_path):
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    test_file = tmp_path / "signal_service_translation.arxml"
    test_file.write_text(ARXML, encoding="utf-8")
    parser = ARXMLParser()
    parser.load(str(test_file), document)
    return document


class TestSignalServiceTranslationParsing:
    def test_props_set_parsed(self, loaded_document):
        pkg = loaded_document.getARPackages()[0]
        props_set = pkg.getElement("propsSet", None)
        assert props_set is not None
        assert props_set.getShortName() == "propsSet"

    def test_props_refs_and_service_control(self, loaded_document):
        pkg = loaded_document.getARPackages()[0]
        props_set = pkg.getElement("propsSet", None)
        props = props_set.getSignalServiceTranslationProps()[0]
        assert props.getShortName() == "props"
        assert len(props.getControlConsumedEventGroupRefs()) == 1
        assert props.getControlConsumedEventGroupRefs()[0].getValue() == "/pkg/ConsumedEventGroup"
        assert len(props.getControlPncRefs()) == 1
        assert props.getControlPncRefs()[0].getValue() == "/pkg/PncMapping"
        assert len(props.getControlProvidedEventGroupRefs()) == 1
        assert props.getControlProvidedEventGroupRefs()[0].getValue() == "/pkg/EventHandler"
        assert props.getServiceControl().getValue() == "translationStart"

    def test_event_props(self, loaded_document):
        pkg = loaded_document.getARPackages()[0]
        props_set = pkg.getElement("propsSet", None)
        props = props_set.getSignalServiceTranslationProps()[0]
        event_props = props.getSignalServiceTranslationEventProps()[0]
        assert event_props.getShortName() == "eventProps"
        assert event_props.getSafeTranslation().getValue() is True
        assert event_props.getSecureTranslation().getValue() is False
        target = event_props.getTranslationTarget()
        assert target is not None
        assert target.getTargetDataPrototypeRef().getValue() == "/pkg/TargetDataPrototype"

    def test_element_props(self, loaded_document):
        pkg = loaded_document.getARPackages()[0]
        props_set = pkg.getElement("propsSet", None)
        props = props_set.getSignalServiceTranslationProps()[0]
        event_props = props.getSignalServiceTranslationEventProps()[0]
        element_props = event_props.getSignalServiceTranslationElementProps()[0]
        assert element_props.getShortName() == "elementProps"
        assert element_props.getFilter() is not None
        assert element_props.getFilter().getDataFilterType().getValue() == "always"
        assert element_props.getTransmissionTrigger().getValue() is True

    def test_empty_list_round_trip_not_loaded(self, tmp_path):
        empty_arxml = """<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="{ns}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="{ns} AUTOSAR_4-3-0.xsd">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>Translation</SHORT-NAME>
      <ELEMENTS>
        <SIGNAL-SERVICE-TRANSLATION-PROPS-SET>
          <SHORT-NAME>emptySet</SHORT-NAME>
        </SIGNAL-SERVICE-TRANSLATION-PROPS-SET>
      </ELEMENTS>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
""".format(
            ns=NS
        )
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        test_file = tmp_path / "empty_signal_service_translation.arxml"
        test_file.write_text(empty_arxml, encoding="utf-8")
        parser = ARXMLParser()
        parser.load(str(test_file), document)
        pkg = document.getARPackages()[0]
        props_set = pkg.getElement("emptySet", None)
        assert props_set is not None
        assert props_set.getSignalServiceTranslationProps() == []
