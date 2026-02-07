from typing import TYPE_CHECKING, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)

if TYPE_CHECKING:
    from armodel.v2.models.M2.MSR.Documentation.TextModel.BlockElements import (
        DocumentationBlock,
    )


class MsrQueryProps(ARObject):
    def __init__(self) -> None:
        super().__init__()

        self.queryString: Union[String, None] = None

    def getQueryString(self) -> Union[String, None]:
        return self.queryString

    def setQueryString(self, value: String) -> "MsrQueryProps":
        self.queryString = value
        return self


class MsrQueryP2(ARObject):
    def __init__(self) -> None:
        super().__init__()

        self.msrQueryProps: Union[MsrQueryProps, None] = None
        self.msrQueryResultP2: Union["DocumentationBlock", None] = None

    def getMsrQueryProps(self) -> Union[MsrQueryProps, None]:
        return self.msrQueryProps

    def setMsrQueryProps(self, value: MsrQueryProps) -> "MsrQueryP2":
        self.msrQueryProps = value
        return self

    def getMsrQueryResultP2(self) -> Union["DocumentationBlock", None]:
        return self.msrQueryResultP2

    def setMsrQueryResultP2(self, value: "DocumentationBlock") -> "MsrQueryP2":
        self.msrQueryResultP2 = value
        return self


__all__ = [
    'MsrQueryProps',
    'MsrQueryP2',
]
