from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    EndToEndTransformationISignalProps,
    TransformationISignalProps,
)


class Test_EndToEndTransformationISignalProps:
    # Table 7.27, p.809 — attribute Notes verbatim from the markdown
    NOTE_DATA_ID = (
        "This represents a unique numerical identifier. Note: ID is used for protection against masquerading. "
        "The details concerning the maximum number of values (this information is specific for each E2E profile) "
        "applicable for this attribute are controlled by a semantic constraint that depends on the category of the EndToEnd Protection."
    )
    NOTE_DATA_LENGTH = "Length of payload and E2E header in bits."
    NOTE_MAX_DATA_LENGTH = "Maximum length of payload and E2E header in bits."
    NOTE_MIN_DATA_LENGTH = "Minimum length of payload and E2E header in bits."
    NOTE_SOURCE_ID = (
        "This attribute represents a unique numerical identifier identifying the source of a certain transmission. "
        "In case of C/S communication, this ID uniquely identifies the client. "
        "Note: ID is used for protection against masquerading. "
        "The details concerning the maximum number of values (this information is specific for each E2E profile) "
        "applicable for this attribute are controlled by a semantic constraint that depends on the category of the EndToEnd Protection."
    )

    def _make_positive(self, value):
        return PositiveInteger().setValue(value)

    def test_docstring_is_spec_note_verbatim(self):
        # Table 7.27, p.809 — class Note verbatim from the markdown
        note = "Holds all the ISignal specific attributes for the EndToEndTransformer."
        assert EndToEndTransformationISignalProps.__doc__.strip() == note

    def test_init_has_no_docstring(self):
        assert EndToEndTransformationISignalProps.__init__.__doc__ is None

    def test_heritage(self):
        props = EndToEndTransformationISignalProps()
        assert isinstance(props, TransformationISignalProps)
        assert isinstance(props, Describable)

    def test_initialization(self):
        # spec displayed order: dataId `*`, dataLength, maxDataLength, minDataLength, sourceId (all 0..1)
        props = EndToEndTransformationISignalProps()
        assert props.getDataIds() == []
        assert props.getDataLength() is None
        assert props.getMaxDataLength() is None
        assert props.getMinDataLength() is None
        assert props.getSourceId() is None

    def test_get_set_data_length(self):
        props = EndToEndTransformationISignalProps()
        value = self._make_positive("8")
        assert props.setDataLength(value) is props
        assert props.getDataLength() is value
        props.setDataLength(None)
        assert props.getDataLength() is value

    def test_get_set_max_data_length(self):
        props = EndToEndTransformationISignalProps()
        value = self._make_positive("2032")
        assert props.setMaxDataLength(value) is props
        assert props.getMaxDataLength() is value
        props.setMaxDataLength(None)
        assert props.getMaxDataLength() is value

    def test_get_set_min_data_length(self):
        props = EndToEndTransformationISignalProps()
        value = self._make_positive("8")
        assert props.setMinDataLength(value) is props
        assert props.getMinDataLength() is value
        props.setMinDataLength(None)
        assert props.getMinDataLength() is value

    def test_get_set_source_id(self):
        props = EndToEndTransformationISignalProps()
        value = self._make_positive("1")
        assert props.setSourceId(value) is props
        assert props.getSourceId() is value
        props.setSourceId(None)
        assert props.getSourceId() is value

    def test_add_data_id(self):
        props = EndToEndTransformationISignalProps()
        first = self._make_positive("1")
        second = self._make_positive("2")
        assert props.addDataId(first) is props
        props.addDataId(second)
        assert props.getDataIds() == [first, second]
        props.addDataId(None)
        assert len(props.getDataIds()) == 2
