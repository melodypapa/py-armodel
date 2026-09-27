import inspect

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import HandleInvalidEnum
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ISignalPort,
)

CLASS_NOTE = (
    "Connectors reception or send port on the referenced channel referenced by an ISignalTriggering. "
    "If different timeouts or DataFilters for ISignals need to be specified several ISignalPorts may be created."
)
NOTES = {
    "dataFilter": (
        "Optional specification of a signal COM filter at the receiver side in case that the System Description "
        "doesn't use a complete Software Component Description (VFB View). This supports the inclusion of legacy "
        "system signals. If a full DataMapping exist for the SystemSignal this information may be available from a "
        "configured ReceiverComSpec. In this case the ReceiverComSpec overrides this optional specification."
    ),
    "ddsQosProfileRef": "Reference to the DDS Qos profile used for this ISignal. Tags: atp.Status=candidate",
    "firstTimeout": (
        "• ISignalPort with communicationDirection = in: Optional first timeout value in seconds for the reception "
        "of the ISignal. • ISignalPort with communicationDirection = out: Optional first timeout value in seconds "
        "for transmission deadline monitoring."
    ),
    "handleInvalid": "This attribute defines how invalidation is applied to the ISignals received in the context of this ISignalPort.",
    "timeout": (
        "• ISignalPort with communicationDirection = in: Optional timeout value in seconds for the reception of the "
        "ISignal. The attribute value is used to configure the Com Timeout in the COM module. The RTE ignores this "
        "attribute. The timeout can also be specified with the NonqueuedReceiverComSpec.aliveTimeout attribute. If a "
        "full DataMapping exists for the SystemSignal and the value is available in the configured ReceiverComSpec, "
        "then the timeout value in the ReceiverComSpec overrides this optional timeout specification during the "
        "creation of the Base Ecu Configuration of the COM module. • ISignalPort with communicationDirection = out: "
        "Optional timeout value in seconds for the transmission of the ISignal. The attribute value is used to "
        "configure the ComTimeout in the COM module. The RTE ignores this attribute. The timeout can also be "
        "specified with the ender ComSpec.transmissionAcknowledge.timeout attribute. If a full DataMapping exists "
        "for the SystemSignal and the value is available in the configured SenderComSpec, then the timeout value in "
        "the SenderComSpec overrides this optional timeout specification during the creation of the Base Ecu "
        "Configuration of the COM module. This attribute can be used in the following cases: • legacy signal where "
        "the System Description doesn't use a complete Software Component Description (VFB View) and where the "
        "DataMapping is missing. • bus monitoring use cases in which the DataMapping is ignored."
    ),
}


class TestISignalPort:
    """Test cases for ISignalPort (Table 6.5, p.306)."""

    def test_initialization_defaults(self):
        port = ISignalPort(None, "Port")
        assert port.getDataFilter() is None
        assert port.getDdsQosProfileRef() is None
        assert port.getFirstTimeout() is None
        assert port.getHandleInvalid() is None
        assert port.getTimeout() is None

    def test_get_set_round_trip_and_none_noop(self):
        port = ISignalPort(None, "Port")

        data_filter = DataFilter()
        assert port.setDataFilter(data_filter) is port
        assert port.getDataFilter() is data_filter
        port.setDataFilter(None)
        assert port.getDataFilter() is data_filter

        ref = RefType()
        ref.value = "profiles/myProfile"
        assert port.setDdsQosProfileRef(ref) is port
        assert port.getDdsQosProfileRef() is ref
        port.setDdsQosProfileRef(None)
        assert port.getDdsQosProfileRef() is ref

        first_timeout = TimeValue()
        assert port.setFirstTimeout(first_timeout) is port
        assert port.getFirstTimeout() is first_timeout

        assert port.setHandleInvalid(HandleInvalidEnum.KEEP) is port
        assert port.getHandleInvalid() == HandleInvalidEnum.KEEP

        timeout = TimeValue()
        assert port.setTimeout(timeout) is port
        assert port.getTimeout() is timeout

    def test_class_docstring_note(self):
        assert inspect.cleandoc(ISignalPort.__doc__).split("\n\n")[0] == CLASS_NOTE

    def test_accessor_docstrings_verbatim(self):
        port = ISignalPort(None, "Port")
        for attr in ("dataFilter", "ddsQosProfileRef", "firstTimeout", "handleInvalid", "timeout"):
            getter = getattr(port, "get" + attr[0].upper() + attr[1:])
            setter = getattr(port, "set" + attr[0].upper() + attr[1:])
            assert inspect.cleandoc(getter.__doc__) == NOTES[attr], attr
            assert inspect.cleandoc(setter.__doc__).split("\n")[0] == NOTES[attr], attr
