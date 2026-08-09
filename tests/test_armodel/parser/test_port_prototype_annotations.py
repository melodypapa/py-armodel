"""Reader/writer round-trip tests for PortPrototype annotation classes."""

import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes import (
    ClientServerAnnotation,
    DataLimitKindEnum,
    DelegatedPortAnnotation,
    FilterDebouncingEnum,
    IoHwAbstractionServerAnnotation,
    ModePortAnnotation,
    NvDataPortAnnotation,
    ParameterPortAnnotation,
    ProcessingKindEnum,
    PulseTestEnum,
    SenderReceiverAnnotation,
    SignalFanEnum,
    TriggerPortAnnotation,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _bool(value):
    b = ARBoolean()
    b.setValue("true" if value else "false")
    return b


class TestPortPrototypeAnnotationsRoundTrip:
    def _build(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        swc = pkg.createApplicationSwComponentType("App")
        port = swc.createPRPortPrototype("Port")

        cs = ClientServerAnnotation()
        cs.setOperationRef(_ref("/If/Op", "CLIENT-SERVER-OPERATION"))
        port.addClientServerAnnotation(cs)

        delegated = DelegatedPortAnnotation()
        delegated.setSignalFan(SignalFanEnum().setValue(SignalFanEnum.NFOLD))
        port.setDelegatedPortAnnotation(delegated)

        io = IoHwAbstractionServerAnnotation()
        io.setFilteringDebouncing(FilterDebouncingEnum().setValue(FilterDebouncingEnum.DEBOUNCE_DATA))
        io.setPulseTest(PulseTestEnum().setValue(PulseTestEnum.ENABLE))
        io.setTriggerRef(_ref("/Trig", "TRIGGER"))
        port.addIoHwAbstractionServerAnnotation(io)

        mode = ModePortAnnotation()
        mode.setModeGroupRef(_ref("/Mode", "MODE-DECLARATION-GROUP-PROTOTYPE"))
        port.addModePortAnnotation(mode)

        nv = NvDataPortAnnotation()
        nv.setVariableRef(_ref("/Nv", "VARIABLE-DATA-PROTOTYPE"))
        port.addNvDataPortAnnotation(nv)

        param = ParameterPortAnnotation()
        param.setParameterRef(_ref("/Param", "PARAMETER-DATA-PROTOTYPE"))
        port.addParameterPortAnnotation(param)

        sr = SenderReceiverAnnotation()
        sr.setComputed(_bool(True))
        sr.setDataElementRef(_ref("/Data", "VARIABLE-DATA-PROTOTYPE"))
        sr.setLimitKind(DataLimitKindEnum().setValue(DataLimitKindEnum.MAX))
        sr.setProcessingKind(ProcessingKindEnum().setValue(ProcessingKindEnum.FILTERED))
        port.addSenderReceiverAnnotation(sr)

        trig = TriggerPortAnnotation()
        trig.setTriggerRef(_ref("/Trig2", "TRIGGER"))
        port.addTriggerPortAnnotation(trig)

        return document

    def test_round_trip(self):
        document = self._build()
        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            port_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0].getPRPortPrototypes()[0]

            cs_list = port_2.getClientServerAnnotations()
            assert len(cs_list) == 1
            assert cs_list[0].getOperationRef().getValue() == "/If/Op"
            assert cs_list[0].getOperationRef().getDest() == "CLIENT-SERVER-OPERATION"

            delegated = port_2.getDelegatedPortAnnotation()
            assert delegated is not None
            assert isinstance(delegated.getSignalFan(), SignalFanEnum)
            assert delegated.getSignalFan().getValue() == SignalFanEnum.NFOLD

            io_list = port_2.getIoHwAbstractionServerAnnotations()
            assert len(io_list) == 1
            assert isinstance(io_list[0].getFilteringDebouncing(), FilterDebouncingEnum)
            assert io_list[0].getFilteringDebouncing().getValue() == FilterDebouncingEnum.DEBOUNCE_DATA
            assert isinstance(io_list[0].getPulseTest(), PulseTestEnum)
            assert io_list[0].getPulseTest().getValue() == PulseTestEnum.ENABLE
            assert io_list[0].getTriggerRef().getValue() == "/Trig"

            mode_list = port_2.getModePortAnnotations()
            assert len(mode_list) == 1
            assert mode_list[0].getModeGroupRef().getValue() == "/Mode"

            nv_list = port_2.getNvDataPortAnnotations()
            assert len(nv_list) == 1
            assert nv_list[0].getVariableRef().getValue() == "/Nv"

            param_list = port_2.getParameterPortAnnotations()
            assert len(param_list) == 1
            assert param_list[0].getParameterRef().getValue() == "/Param"

            sr_list = port_2.getSenderReceiverAnnotations()
            assert len(sr_list) == 1
            assert sr_list[0].getComputed().getValue() is True
            assert sr_list[0].getDataElementRef().getValue() == "/Data"
            assert isinstance(sr_list[0].getLimitKind(), DataLimitKindEnum)
            assert sr_list[0].getLimitKind().getValue() == DataLimitKindEnum.MAX
            assert isinstance(sr_list[0].getProcessingKind(), ProcessingKindEnum)
            assert sr_list[0].getProcessingKind().getValue() == ProcessingKindEnum.FILTERED

            trig_list = port_2.getTriggerPortAnnotations()
            assert len(trig_list) == 1
            assert trig_list[0].getTriggerRef().getValue() == "/Trig2"
        finally:
            import os

            if os.path.exists(file_path):
                os.remove(file_path)
