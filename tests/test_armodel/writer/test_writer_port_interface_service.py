"""Round-trip tests for PortInterface.isService and PortInterface.serviceKind (Table 3.18)."""

import os
import tempfile
import xml.etree.cElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import ServiceProviderEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestPortInterfaceServiceAttributesRoundTrip:
    def test_round_trip_is_service_and_service_kind(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("PortInterfaces")
        cs = pkg.createClientServerInterface("CSInterface")
        cs.createOperation("Op")

        is_service = Boolean()
        is_service.setValue("true")
        cs.setIsService(is_service)

        service_kind = ServiceProviderEnum().setValue(ServiceProviderEnum.COM_MANAGER)
        cs.setServiceKind(service_kind)

        with tempfile.NamedTemporaryFile(suffix=".arxml", delete=False) as tmp:
            tmp_path = tmp.name
        try:
            ARXMLWriter().save(tmp_path, autosar)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(tmp_path, document_2)

            cs_2 = document_2.getARPackages()[0].getClientServerInterfaces()[0]
            assert cs_2.getShortName() == "CSInterface"

            # isService round-trips as a Boolean
            assert cs_2.getIsService() is not None
            assert cs_2.getIsService().getValue() is True

            # serviceKind round-trips as the literal text "comManager"
            assert cs_2.getServiceKind() is not None
            assert cs_2.getServiceKind().getText() == "comManager"
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_round_trip_optional_absent(self):
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("PortInterfaces")
        cs = pkg.createClientServerInterface("CSInterface")
        cs.createOperation("Op")

        with tempfile.NamedTemporaryFile(suffix=".arxml", delete=False) as tmp:
            tmp_path = tmp.name
        try:
            ARXMLWriter().save(tmp_path, autosar)

            tree = ET.parse(tmp_path)
            root = tree.getroot()
            local_tags = [el.tag.split("}")[-1] for el in root.iter()]
            assert "IS-SERVICE" not in local_tags
            assert "SERVICE-KIND" not in local_tags

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(tmp_path, document_2)
            cs_2 = document_2.getARPackages()[0].getClientServerInterfaces()[0]
            assert cs_2.getIsService() is None
            assert cs_2.getServiceKind() is None
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
