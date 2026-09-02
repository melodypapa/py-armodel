"""Writer round-trip tests for DataPrototype.swDataDefProps (SWCT Table 5.28).

Builds a concrete VariableDataPrototype (a DataPrototype subclass) carrying
SwDataDefProps, writes it, re-parses, and asserts the aggregation survives the
round-trip -- confirming writeDataPrototype / readDataPrototype coverage.
"""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestDataPrototypeWriter:
    def test_round_trip_sw_data_def_props(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()

        pkg = document.createARPackage("Pkg")
        sr_if = pkg.createSenderReceiverInterface("SR")
        prototype = sr_if.createDataElement("DE")

        props = SwDataDefProps()
        props.setSwAddrMethodRef(RefType().setDest("AUTOSAR/SwAddrMethods/ram"))
        prototype.setSwDataDefProps(props)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            prototype_2 = document_2.getARPackages()[0].getSenderReceiverInterfaces()[0].getDataElements()[0]
            props_2 = prototype_2.getSwDataDefProps()
            assert props_2 is not None
            assert props_2.getSwAddrMethodRef().getDest() == "AUTOSAR/SwAddrMethods/ram"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
