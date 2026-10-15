from typing import Optional


class PrimitivePatternError(ValueError):
    def __init__(self, class_name: str, value: str, pattern: str, xsd_type: Optional[str] = None) -> None:
        self.class_name = class_name
        self.value = value
        self.pattern = pattern
        self.xsd_type = xsd_type
        type_label = xsd_type if xsd_type is not None else class_name
        super().__init__('value "%s" does not match pattern "%s" (%s)' % (value, pattern, type_label))
