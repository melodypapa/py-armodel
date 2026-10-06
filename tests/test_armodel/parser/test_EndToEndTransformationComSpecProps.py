"""Reader tests for EndToEndTransformationComSpecProps (Table 4.92, p.201).

The XML snippets use the XSD-valid element spellings from
``autosar/R23-11/xsd/AUTOSAR_00052.xsd`` (group END-TO-END-TRANSFORMATION-COM-SPEC-PROPS),
including the ``E-2-E-PROFILE-COMPATIBILITY-PROPS-REF`` reference element.
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import NonqueuedReceiverComSpec, ServerComSpec
from tests.test_armodel.parser._helpers import _snip

_FULL_INNER = (
    "<CLEAR-FROM-VALID-TO-INVALID>true</CLEAR-FROM-VALID-TO-INVALID>"
    "<DISABLE-END-TO-END-CHECK>true</DISABLE-END-TO-END-CHECK>"
    "<DISABLE-END-TO-END-STATE-MACHINE>true</DISABLE-END-TO-END-STATE-MACHINE>"
    "<E-2-E-PROFILE-COMPATIBILITY-PROPS-REF DEST='E-2-E-PROFILE-COMPATIBILITY-PROPS'>/Pkg/Props</E-2-E-PROFILE-COMPATIBILITY-PROPS-REF>"
    "<MAX-DELTA-COUNTER>3</MAX-DELTA-COUNTER>"
    "<MAX-ERROR-STATE-INIT>2</MAX-ERROR-STATE-INIT>"
    "<MAX-ERROR-STATE-INVALID>2</MAX-ERROR-STATE-INVALID>"
    "<MAX-ERROR-STATE-VALID>2</MAX-ERROR-STATE-VALID>"
    "<MAX-NO-NEW-OR-REPEATED-DATA>2</MAX-NO-NEW-OR-REPEATED-DATA>"
    "<MIN-OK-STATE-INIT>1</MIN-OK-STATE-INIT>"
    "<MIN-OK-STATE-INVALID>1</MIN-OK-STATE-INVALID>"
    "<MIN-OK-STATE-VALID>1</MIN-OK-STATE-VALID>"
    "<SYNC-COUNTER-INIT>0</SYNC-COUNTER-INIT>"
    "<WINDOW-SIZE-INIT>5</WINDOW-SIZE-INIT>"
    "<WINDOW-SIZE-INVALID>5</WINDOW-SIZE-INVALID>"
    "<WINDOW-SIZE-VALID>5</WINDOW-SIZE-VALID>"
)


class TestEndToEndTransformationComSpecPropsReader:
    def test_read_e2e_transformation_com_spec_props_full(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import EndToEndTransformationComSpecProps

        com_spec = ServerComSpec()
        element = _snip(
            "<TRANSFORMATION-COM-SPEC-PROPSS>" "<END-TO-END-TRANSFORMATION-COM-SPEC-PROPS>%s</END-TO-END-TRANSFORMATION-COM-SPEC-PROPS>" "</TRANSFORMATION-COM-SPEC-PROPSS>" % _FULL_INNER,
            root_tag="SERVER-COM-SPEC",
        )
        parser.readTransformationComSpecPropss(element, com_spec)

        props = com_spec.getTransformationComSpecProps()
        assert len(props) == 1
        assert isinstance(props[0], EndToEndTransformationComSpecProps)
        assert props[0].getClearFromValidToInvalid().getValue() is True
        assert props[0].getDisableEndToEndCheck().getValue() is True
        assert props[0].getDisableEndToEndStateMachine().getValue() is True
        ref = props[0].getE2eProfileCompatibilityPropsRef()
        assert ref is not None
        assert ref.getValue() == "/Pkg/Props"
        assert ref.getDest() == "E-2-E-PROFILE-COMPATIBILITY-PROPS"
        assert props[0].getMaxDeltaCounter().getValue() == 3
        assert props[0].getMaxErrorStateInit().getValue() == 2
        assert props[0].getMaxErrorStateInvalid().getValue() == 2
        assert props[0].getMaxErrorStateValid().getValue() == 2
        assert props[0].getMaxNoNewOrRepeatedData().getValue() == 2
        assert props[0].getMinOkStateInit().getValue() == 1
        assert props[0].getMinOkStateInvalid().getValue() == 1
        assert props[0].getMinOkStateValid().getValue() == 1
        assert props[0].getSyncCounterInit().getValue() == 0
        assert props[0].getWindowSizeInit().getValue() == 5
        assert props[0].getWindowSizeInvalid().getValue() == 5
        assert props[0].getWindowSizeValid().getValue() == 5

    def test_read_e2e_transformation_com_spec_props_empty(self, parser):
        com_spec = ServerComSpec()
        element = _snip(
            "<TRANSFORMATION-COM-SPEC-PROPSS>" "<END-TO-END-TRANSFORMATION-COM-SPEC-PROPS/>" "</TRANSFORMATION-COM-SPEC-PROPSS>",
            root_tag="SERVER-COM-SPEC",
        )
        parser.readTransformationComSpecPropss(element, com_spec)

        props = com_spec.getTransformationComSpecProps()
        assert len(props) == 1
        assert props[0].getClearFromValidToInvalid() is None
        assert props[0].getDisableEndToEndCheck() is None
        assert props[0].getDisableEndToEndStateMachine() is None
        assert props[0].getE2eProfileCompatibilityPropsRef() is None
        assert props[0].getMaxDeltaCounter() is None
        assert props[0].getMaxErrorStateInit() is None
        assert props[0].getMaxErrorStateInvalid() is None
        assert props[0].getMaxErrorStateValid() is None
        assert props[0].getMaxNoNewOrRepeatedData() is None
        assert props[0].getMinOkStateInit() is None
        assert props[0].getMinOkStateInvalid() is None
        assert props[0].getMinOkStateValid() is None
        assert props[0].getSyncCounterInit() is None
        assert props[0].getWindowSizeInit() is None
        assert props[0].getWindowSizeInvalid() is None
        assert props[0].getWindowSizeValid() is None

    def test_read_receiver_com_spec_e2e_props(self, parser):
        com_spec = NonqueuedReceiverComSpec()
        element = _snip(
            "<TRANSFORMATION-COM-SPEC-PROPSS>"
            "<END-TO-END-TRANSFORMATION-COM-SPEC-PROPS>"
            "<MAX-DELTA-COUNTER>3</MAX-DELTA-COUNTER>"
            "<WINDOW-SIZE-INIT>5</WINDOW-SIZE-INIT>"
            "</END-TO-END-TRANSFORMATION-COM-SPEC-PROPS>"
            "</TRANSFORMATION-COM-SPEC-PROPSS>",
            root_tag="NONQUEUED-RECEIVER-COM-SPEC",
        )
        parser.readReceiverComSpec(element, com_spec)

        props = com_spec.getTransformationComSpecProps()
        assert len(props) == 1
        assert props[0].getMaxDeltaCounter().getValue() == 3
        assert props[0].getWindowSizeInit().getValue() == 5

    def test_read_receiver_com_spec_without_wrapper_yields_empty_list(self, parser):
        com_spec = NonqueuedReceiverComSpec()
        element = _snip("<DATA-ELEMENT-REF DEST='VARIABLE-DATA-PROTOTYPE'>/Pkg/Data</DATA-ELEMENT-REF>", root_tag="NONQUEUED-RECEIVER-COM-SPEC")
        parser.readReceiverComSpec(element, com_spec)

        assert com_spec.getTransformationComSpecProps() == []
