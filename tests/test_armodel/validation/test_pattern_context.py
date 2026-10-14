import pytest

from armodel.validation import PrimitivePatternError, is_warning_mode, set_warning_mode, warning_mode


class TestPrimitivePatternError:
    def test_fields_and_message_with_xsd_type(self):
        error = PrimitivePatternError("MetaClassName", "bad-name", "[A-Z][a-zA-Z0-9_]*", "META-CLASS-NAME")
        assert error.class_name == "MetaClassName"
        assert error.value == "bad-name"
        assert error.pattern == "[A-Z][a-zA-Z0-9_]*"
        assert error.xsd_type == "META-CLASS-NAME"
        assert str(error) == 'value "bad-name" does not match pattern "[A-Z][a-zA-Z0-9_]*" (META-CLASS-NAME)'

    def test_fields_and_message_without_xsd_type(self):
        error = PrimitivePatternError("CIdentifier", "9bad", "[a-zA-Z_][a-zA-Z0-9_]*")
        assert error.xsd_type is None
        assert str(error) == 'value "9bad" does not match pattern "[a-zA-Z_][a-zA-Z0-9_]*" (CIdentifier)'

    def test_is_value_error(self):
        with pytest.raises(ValueError):
            raise PrimitivePatternError("X", "v", "p")


class TestWarningMode:
    def test_default_is_off(self):
        with warning_mode(False):
            assert is_warning_mode() is False

    def test_scoped_enable(self):
        assert is_warning_mode() is False
        with warning_mode(True, context="file.arxml"):
            assert is_warning_mode() is True
            from armodel.validation import get_context

            assert get_context() == "file.arxml"
        assert is_warning_mode() is False
        assert get_context() is None

    def test_nested_restore(self):
        with warning_mode(True, "outer"):
            with warning_mode(False):
                assert is_warning_mode() is False
            assert is_warning_mode() is True
            from armodel.validation import get_context

            assert get_context() == "outer"

    def test_set_warning_mode_direct(self):
        previous = is_warning_mode()
        try:
            set_warning_mode(True, "ctx")
            assert is_warning_mode() is True
        finally:
            set_warning_mode(previous)

    def test_thread_isolation(self):
        import threading

        result = {}

        def worker():
            result["mode"] = is_warning_mode()

        with warning_mode(True, "main"):
            thread = threading.Thread(target=worker)
            thread.start()
            thread.join()
        assert result["mode"] is False
