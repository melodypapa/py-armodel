from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical
from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARType

class ARLiteral(ARType):
    def __init__(self) -> None:
        super().__init__()              

    @property
    def value(self) -> str:
        if self._value is None:
            return ""
        return self._value
    
    @value.setter
    def value(self, val: any):
        if isinstance(val, str):
            self._value = val
        else:
            self._value = str(val)
    
    def __str__(self) -> str:
        return self.value
    
    def upper(self) -> str:
        return self.value.upper()

class ARPositiveInteger(ARNumerical):
    def __init__(self) -> None:
        super().__init__()

    @property
    def value(self) -> int:
        return self._value
    
    @value.setter
    def value(self, val: any):
        if isinstance(val, int):
            if val < 0:
                raise ValueError("Invalid Positive Integer <%s>" % val)
            self._value = val
        elif isinstance(val, str):
            self._text = val
            self._value = self._convertStringToNumberValue(val)
        else:
            raise ValueError("Unsupported Type <%s>", type(val))

class ARBoolean(ARType):
    def __init__(self) -> None:
        super().__init__()

        self._text = None   

    def _convertNumberToBoolean(self, value: int) -> bool:
        if value == 0:
            return False
        return True

    def _convertStringToBoolean(self, value: str) -> bool:
        value = value.lower()
        if value == "true":
            return True
        elif value == "false":
            return False
        else:
            return self._convertNumberToBoolean(int(value))

    @property
    def value(self) -> int:
        return self._value
    
    @value.setter
    def value(self, val: any):
        if isinstance(val, bool):
            self._value = val
        elif isinstance(val, int):
            self._value = self._convertNumberToBoolean(val)
            self._text = str(val)
        elif isinstance(val, str):
            self._text = val
            self._value = self._convertStringToBoolean(val)
        else:
            raise ValueError("Unsupported Type <%s>", type(val))

    def __str__(self) -> str:
        if self._text is not None:
            return self._text
        else:
            if self._value:
                return "true"
            else:
                return "false"
                