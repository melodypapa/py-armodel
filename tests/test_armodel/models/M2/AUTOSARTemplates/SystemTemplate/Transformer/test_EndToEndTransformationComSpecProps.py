from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import TransformationComSpecProps
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import EndToEndTransformationComSpecProps


class TestEndToEndTransformationComSpecProps:
    """
    Model tests for EndToEndTransformationComSpecProps (Table 4.92).
    """

    def test_initialization(self):
        props = EndToEndTransformationComSpecProps()

        assert isinstance(props, TransformationComSpecProps)
        assert props.getClearFromValidToInvalid() is None
        assert props.getDisableEndToEndCheck() is None
        assert props.getDisableEndToEndStateMachine() is None
        assert props.getE2eProfileCompatibilityPropsRef() is None
        assert props.getMaxDeltaCounter() is None
        assert props.getMaxErrorStateInit() is None
        assert props.getMaxErrorStateInvalid() is None
        assert props.getMaxErrorStateValid() is None
        assert props.getMaxNoNewOrRepeatedData() is None
        assert props.getMinOkStateInit() is None
        assert props.getMinOkStateInvalid() is None
        assert props.getMinOkStateValid() is None
        assert props.getSyncCounterInit() is None
        assert props.getWindowSizeInit() is None
        assert props.getWindowSizeInvalid() is None
        assert props.getWindowSizeValid() is None

    def test_get_set_clear_from_valid_to_invalid(self):
        props = EndToEndTransformationComSpecProps()
        value = Boolean().setValue(True)

        assert props == props.setClearFromValidToInvalid(None)
        assert props.getClearFromValidToInvalid() is None

        assert props == props.setClearFromValidToInvalid(value)
        assert props.getClearFromValidToInvalid() == value
        assert props.getClearFromValidToInvalid().getValue() is True

        assert props == props.setClearFromValidToInvalid(None)  # None no-op
        assert props.getClearFromValidToInvalid() == value
        assert props.getClearFromValidToInvalid().getValue() is True

    def test_get_set_disable_end_to_end_check(self):
        props = EndToEndTransformationComSpecProps()
        value = Boolean().setValue(True)

        assert props == props.setDisableEndToEndCheck(None)
        assert props.getDisableEndToEndCheck() is None

        assert props == props.setDisableEndToEndCheck(value)
        assert props.getDisableEndToEndCheck() == value
        assert props.getDisableEndToEndCheck().getValue() is True

        assert props == props.setDisableEndToEndCheck(None)  # None no-op
        assert props.getDisableEndToEndCheck() == value
        assert props.getDisableEndToEndCheck().getValue() is True

    def test_get_set_disable_end_to_end_state_machine(self):
        props = EndToEndTransformationComSpecProps()
        value = Boolean().setValue(True)

        assert props == props.setDisableEndToEndStateMachine(None)
        assert props.getDisableEndToEndStateMachine() is None

        assert props == props.setDisableEndToEndStateMachine(value)
        assert props.getDisableEndToEndStateMachine() == value
        assert props.getDisableEndToEndStateMachine().getValue() is True

        assert props == props.setDisableEndToEndStateMachine(None)  # None no-op
        assert props.getDisableEndToEndStateMachine() == value
        assert props.getDisableEndToEndStateMachine().getValue() is True

    def test_get_set_e2e_profile_compatibility_props_ref(self):
        props = EndToEndTransformationComSpecProps()
        value = RefType().setValue("/Pkg/Props").setDest("E-2-E-PROFILE-COMPATIBILITY-PROPS")

        assert props == props.setE2eProfileCompatibilityPropsRef(None)
        assert props.getE2eProfileCompatibilityPropsRef() is None

        assert props == props.setE2eProfileCompatibilityPropsRef(value)
        assert props.getE2eProfileCompatibilityPropsRef() == value
        assert props.getE2eProfileCompatibilityPropsRef().getValue() == "/Pkg/Props"
        assert props.getE2eProfileCompatibilityPropsRef().getDest() == "E-2-E-PROFILE-COMPATIBILITY-PROPS"

        assert props == props.setE2eProfileCompatibilityPropsRef(None)  # None no-op
        assert props.getE2eProfileCompatibilityPropsRef() == value
        assert props.getE2eProfileCompatibilityPropsRef().getValue() == "/Pkg/Props"

    def test_get_set_max_delta_counter(self):
        props = EndToEndTransformationComSpecProps()
        value = PositiveInteger().setValue("3")

        assert props == props.setMaxDeltaCounter(None)
        assert props.getMaxDeltaCounter() is None

        assert props == props.setMaxDeltaCounter(value)
        assert props.getMaxDeltaCounter() == value
        assert props.getMaxDeltaCounter().getValue() == 3

        assert props == props.setMaxDeltaCounter(None)  # None no-op
        assert props.getMaxDeltaCounter() == value
        assert props.getMaxDeltaCounter().getValue() == 3

    def test_get_set_max_error_state_init(self):
        props = EndToEndTransformationComSpecProps()
        value = PositiveInteger().setValue("2")

        assert props == props.setMaxErrorStateInit(None)
        assert props.getMaxErrorStateInit() is None

        assert props == props.setMaxErrorStateInit(value)
        assert props.getMaxErrorStateInit() == value
        assert props.getMaxErrorStateInit().getValue() == 2

        assert props == props.setMaxErrorStateInit(None)  # None no-op
        assert props.getMaxErrorStateInit() == value
        assert props.getMaxErrorStateInit().getValue() == 2

    def test_get_set_max_error_state_invalid(self):
        props = EndToEndTransformationComSpecProps()
        value = PositiveInteger().setValue("2")

        assert props == props.setMaxErrorStateInvalid(None)
        assert props.getMaxErrorStateInvalid() is None

        assert props == props.setMaxErrorStateInvalid(value)
        assert props.getMaxErrorStateInvalid() == value
        assert props.getMaxErrorStateInvalid().getValue() == 2

        assert props == props.setMaxErrorStateInvalid(None)  # None no-op
        assert props.getMaxErrorStateInvalid() == value
        assert props.getMaxErrorStateInvalid().getValue() == 2

    def test_get_set_max_error_state_valid(self):
        props = EndToEndTransformationComSpecProps()
        value = PositiveInteger().setValue("2")

        assert props == props.setMaxErrorStateValid(None)
        assert props.getMaxErrorStateValid() is None

        assert props == props.setMaxErrorStateValid(value)
        assert props.getMaxErrorStateValid() == value
        assert props.getMaxErrorStateValid().getValue() == 2

        assert props == props.setMaxErrorStateValid(None)  # None no-op
        assert props.getMaxErrorStateValid() == value
        assert props.getMaxErrorStateValid().getValue() == 2

    def test_get_set_max_no_new_or_repeated_data(self):
        props = EndToEndTransformationComSpecProps()
        value = PositiveInteger().setValue("2")

        assert props == props.setMaxNoNewOrRepeatedData(None)
        assert props.getMaxNoNewOrRepeatedData() is None

        assert props == props.setMaxNoNewOrRepeatedData(value)
        assert props.getMaxNoNewOrRepeatedData() == value
        assert props.getMaxNoNewOrRepeatedData().getValue() == 2

        assert props == props.setMaxNoNewOrRepeatedData(None)  # None no-op
        assert props.getMaxNoNewOrRepeatedData() == value
        assert props.getMaxNoNewOrRepeatedData().getValue() == 2

    def test_get_set_min_ok_state_init(self):
        props = EndToEndTransformationComSpecProps()
        value = PositiveInteger().setValue("1")

        assert props == props.setMinOkStateInit(None)
        assert props.getMinOkStateInit() is None

        assert props == props.setMinOkStateInit(value)
        assert props.getMinOkStateInit() == value
        assert props.getMinOkStateInit().getValue() == 1

        assert props == props.setMinOkStateInit(None)  # None no-op
        assert props.getMinOkStateInit() == value
        assert props.getMinOkStateInit().getValue() == 1

    def test_get_set_min_ok_state_invalid(self):
        props = EndToEndTransformationComSpecProps()
        value = PositiveInteger().setValue("1")

        assert props == props.setMinOkStateInvalid(None)
        assert props.getMinOkStateInvalid() is None

        assert props == props.setMinOkStateInvalid(value)
        assert props.getMinOkStateInvalid() == value
        assert props.getMinOkStateInvalid().getValue() == 1

        assert props == props.setMinOkStateInvalid(None)  # None no-op
        assert props.getMinOkStateInvalid() == value
        assert props.getMinOkStateInvalid().getValue() == 1

    def test_get_set_min_ok_state_valid(self):
        props = EndToEndTransformationComSpecProps()
        value = PositiveInteger().setValue("1")

        assert props == props.setMinOkStateValid(None)
        assert props.getMinOkStateValid() is None

        assert props == props.setMinOkStateValid(value)
        assert props.getMinOkStateValid() == value
        assert props.getMinOkStateValid().getValue() == 1

        assert props == props.setMinOkStateValid(None)  # None no-op
        assert props.getMinOkStateValid() == value
        assert props.getMinOkStateValid().getValue() == 1

    def test_get_set_sync_counter_init(self):
        props = EndToEndTransformationComSpecProps()
        value = PositiveInteger().setValue("0")

        assert props == props.setSyncCounterInit(None)
        assert props.getSyncCounterInit() is None

        assert props == props.setSyncCounterInit(value)
        assert props.getSyncCounterInit() == value
        assert props.getSyncCounterInit().getValue() == 0

        assert props == props.setSyncCounterInit(None)  # None no-op
        assert props.getSyncCounterInit() == value
        assert props.getSyncCounterInit().getValue() == 0

    def test_get_set_window_size_init(self):
        props = EndToEndTransformationComSpecProps()
        value = PositiveInteger().setValue("5")

        assert props == props.setWindowSizeInit(None)
        assert props.getWindowSizeInit() is None

        assert props == props.setWindowSizeInit(value)
        assert props.getWindowSizeInit() == value
        assert props.getWindowSizeInit().getValue() == 5

        assert props == props.setWindowSizeInit(None)  # None no-op
        assert props.getWindowSizeInit() == value
        assert props.getWindowSizeInit().getValue() == 5

    def test_get_set_window_size_invalid(self):
        props = EndToEndTransformationComSpecProps()
        value = PositiveInteger().setValue("5")

        assert props == props.setWindowSizeInvalid(None)
        assert props.getWindowSizeInvalid() is None

        assert props == props.setWindowSizeInvalid(value)
        assert props.getWindowSizeInvalid() == value
        assert props.getWindowSizeInvalid().getValue() == 5

        assert props == props.setWindowSizeInvalid(None)  # None no-op
        assert props.getWindowSizeInvalid() == value
        assert props.getWindowSizeInvalid().getValue() == 5

    def test_get_set_window_size_valid(self):
        props = EndToEndTransformationComSpecProps()
        value = PositiveInteger().setValue("5")

        assert props == props.setWindowSizeValid(None)
        assert props.getWindowSizeValid() is None

        assert props == props.setWindowSizeValid(value)
        assert props.getWindowSizeValid() == value
        assert props.getWindowSizeValid().getValue() == 5

        assert props == props.setWindowSizeValid(None)  # None no-op
        assert props.getWindowSizeValid() == value
        assert props.getWindowSizeValid().getValue() == 5
