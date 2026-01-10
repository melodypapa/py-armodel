from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat, ARLiteral, ARNumerical, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean


class TestARObject:

    def test_ARNumerical(self):
        numerical = ARNumerical()
        numerical.value = 123
        assert (numerical.value == 123)
        assert (numerical.getValue() == 123)
        assert (str(numerical) == "123")
        assert (numerical.getText() == "123")

        numerical = ARNumerical()
        numerical.setValue(123)
        assert (numerical.value == 123)
        assert (numerical.getValue() == 123)
        assert (str(numerical) == "123")
        assert (numerical.getText() == "123")

        numerical = ARNumerical()
        numerical.value = "1234"
        assert (numerical.value == 1234)
        assert (numerical.getValue() == 1234)
        assert (str(numerical) == "1234")
        assert (numerical.getText() == "1234")

        numerical = ARNumerical()
        numerical.setValue("0xFF")
        assert (numerical.value == 255)
        assert (numerical.getValue() == 255)
        assert (str(numerical) == "0xFF")
        assert (numerical.getText() == "0xFF")

    def test_ARLiteral(self):
        literal = ARLiteral()
        assert (literal.value == "")
        assert (str(literal) == "")
        assert (literal.getValue() == "")
        assert (literal.getText() == "")

        literal = ARLiteral()
        literal.value = "Literal"
        assert (literal.value == "Literal")
        assert (str(literal) == "Literal")
        assert (literal.getValue() == "Literal")
        assert (literal.getText() == "Literal")

        literal = ARLiteral()
        literal.setValue("Literal1")
        assert (literal.value == "Literal1")
        assert (str(literal) == "Literal1")
        assert (literal.getValue() == "Literal1")
        assert (literal.getText() == "Literal1")

        literal = ARLiteral()
        literal.setValue(1234)
        assert (literal.value == "1234")
        assert (str(literal) == "1234")
        assert (literal.getValue() == "1234")
        assert (literal.getText() == "1234")

    def test_ARFloat(self):
        numerical = ARFloat()
        numerical.value = 123
        assert (numerical.value == 123.0)
        assert (numerical.getValue() == 123.0)
        assert (str(numerical) == "123.0")
        assert (numerical.getText() == "123.0")

        numerical = ARFloat()
        numerical.setValue(123)
        assert (numerical.value == 123)
        assert (numerical.getValue() == 123)
        assert (str(numerical) == "123.0")
        assert (numerical.getText() == "123.0")

        numerical = ARFloat()
        numerical.value = 1234.12
        assert (numerical.value == 1234.12)
        assert (numerical.getValue() == 1234.12)
        assert (str(numerical) == "1234.12")
        assert (numerical.getText() == "1234.12")

        numerical = ARFloat()
        numerical.value = "1234.12"
        assert (numerical.value == 1234.12)
        assert (numerical.getValue() == 1234.12)
        assert (str(numerical) == "1234.12")
        assert (numerical.getText() == "1234.12")

        numerical = ARFloat()
        numerical.value = "1234.0"
        assert (numerical.value == 1234)
        assert (numerical.getValue() == 1234)
        assert (str(numerical) == "1234.0")
        assert (numerical.getText() == "1234.0")

        numerical = ARFloat()
        numerical.value = "1234.000000"
        assert (numerical.value == 1234)
        assert (numerical.getValue() == 1234)
        assert (str(numerical) == "1234.000000")
        assert (numerical.getText() == "1234.000000")

    def test_ARBoolean(self):
        flag = ARBoolean()
        flag.value = False
        assert not flag.value
        assert (flag.getValue() == False)
        assert (str(flag) == "false")
        assert (flag.getText() == "false")

        flag = ARBoolean()
        flag.value = 0
        assert (flag.value == False)
        assert (flag.getValue() == False)
        assert (str(flag) == "0")
        assert (flag.getText() == "0")

        flag = ARBoolean()
        flag.value = "0"
        assert (flag.value == False)
        assert (flag.getValue() == False)
        assert (str(flag) == "0")
        assert (flag.getText() == "0")

        flag = ARBoolean()
        flag.value = True
        assert (flag.value == True)
        assert (flag.getValue() == True)
        assert (str(flag) == "true")
        assert (flag.getText() == "true")

        flag = ARBoolean()
        flag.value = 1
        assert (flag.value == True)
        assert (flag.getValue() == True)
        assert (str(flag) == "1")
        assert (flag.getText() == "1")

        flag = ARBoolean()
        flag.value = "100"
        assert (flag.value == True)
        assert (flag.getValue() == True)
        assert (str(flag) == "100")
        assert (flag.getText() == "100")

    def test_TimeValue(self):
        value = TimeValue()
        value.setValue("0.01")
        assert (value.getValue() == 0.01)
        assert (value.getText() == "0.01")
