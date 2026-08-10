"""Round-trip writer tests for SignalServiceTranslation classes (SystemTemplate 6.339-6.343)."""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, Boolean, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _build_document():
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    pkg = document.createARPackage("Translation")

    props_set = pkg.createSignalServiceTranslationPropsSet("propsSet")
    props = props_set.createSignalServiceTranslationProps("props")
    consumed_ref = RefType()
    consumed_ref.setValue("/pkg/ConsumedEventGroup")
    props.addControlConsumedEventGroupRef(consumed_ref)
    pnc_ref = RefType()
    pnc_ref.setValue("/pkg/PncMapping")
    props.addControlPncRef(pnc_ref)
    provided_ref = RefType()
    provided_ref.setValue("/pkg/EventHandler")
    props.addControlProvidedEventGroupRef(provided_ref)
    props.setServiceControl(ARLiteral().setValue("translationStart"))

    event_props = props.createSignalServiceTranslationEventProps("eventProps")
    event_props.setSafeTranslation(Boolean().setValue("true"))
    event_props.setSecureTranslation(Boolean().setValue("false"))

    element_props = event_props.createSignalServiceTranslationElementProps("elementProps")
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter

    flt = DataFilter()
    flt.setDataFilterType(ARLiteral().setValue("always"))
    element_props.setFilter(flt)
    element_props.setTransmissionTrigger(Boolean().setValue("true"))

    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import (
        VariableDataPrototypeInSystemInstanceRef,
    )

    target = VariableDataPrototypeInSystemInstanceRef()
    target_ref = RefType()
    target_ref.setValue("/pkg/TargetDataPrototype")
    target.setTargetDataPrototypeRef(target_ref)
    event_props.setTranslationTarget(target)

    return document


def _reload(tmp_path, document):
    writer = ARXMLWriter()
    out_file = tmp_path / "signal_service_translation_out.arxml"
    writer.save(str(out_file), document)

    reloaded = AUTOSAR.getInstance()
    reloaded.clear()
    reloaded.setARRelease("R23-11")
    parser = ARXMLParser()
    parser.load(str(out_file), reloaded)
    return reloaded


class TestSignalServiceTranslationWriter:
    def test_round_trip_full(self, tmp_path):
        document = _build_document()
        reloaded = _reload(tmp_path, document)

        pkg = reloaded.getARPackages()[0]
        props_set = pkg.getElement("propsSet", None)
        assert props_set is not None
        props = props_set.getSignalServiceTranslationProps()[0]
        assert props.getShortName() == "props"
        assert props.getControlConsumedEventGroupRefs()[0].getValue() == "/pkg/ConsumedEventGroup"
        assert props.getControlPncRefs()[0].getValue() == "/pkg/PncMapping"
        assert props.getControlProvidedEventGroupRefs()[0].getValue() == "/pkg/EventHandler"
        assert props.getServiceControl().getValue() == "translationStart"

        event_props = props.getSignalServiceTranslationEventProps()[0]
        assert event_props.getSafeTranslation().getValue() is True
        assert event_props.getSecureTranslation().getValue() is False
        target = event_props.getTranslationTarget()
        assert target is not None
        assert target.getTargetDataPrototypeRef().getValue() == "/pkg/TargetDataPrototype"

        element_props = event_props.getSignalServiceTranslationElementProps()[0]
        assert element_props.getFilter().getDataFilterType().getValue() == "always"
        assert element_props.getTransmissionTrigger().getValue() is True

    def test_round_trip_empty_lists(self, tmp_path):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Translation")
        pkg.createSignalServiceTranslationPropsSet("emptySet")

        reloaded = _reload(tmp_path, document)
        pkg2 = reloaded.getARPackages()[0]
        props_set = pkg2.getElement("emptySet", None)
        assert props_set is not None
        assert props_set.getSignalServiceTranslationProps() == []

    def test_no_wrapper_when_empty(self, tmp_path):
        document = _build_document()
        out_file = tmp_path / "no_wrapper.arxml"
        ARXMLWriter().save(str(out_file), document)
        content = out_file.read_text(encoding="utf-8")
        assert "CONTROL-CONSUMED-EVENT-GROUP-REFS" in content
        assert "FILTER" in content
        assert "TRANSMISSION-TRIGGER" in content
