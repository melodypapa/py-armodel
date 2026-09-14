from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import AlignEnum, FloatEnum, FrameEnum, PgwideEnum, ValignEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import MultilanguageReferrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import MimeTypeString, UriString

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph


class Caption(MultilanguageReferrable):
    """
    This meta-class represents the ability to express a caption which is a title, and a shortName.
    """

    # Caption method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.18, p.432
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDesc      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDesc      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This represents a general but brief (one paragraph) description what the object in question is about. It is only one paragraph! This property helps a human reader to identify the object in question. Tags: xml.sequenceOffset=10
        self.desc: Optional[MultiLanguageOverviewParagraph] = None

    def getDesc(self) -> Optional[MultiLanguageOverviewParagraph]:
        """
        This represents a general but brief (one paragraph) description what the object in question is about. It is only one paragraph! This property helps a human reader to identify the object in question. Tags: xml.sequenceOffset=10

        Returns:
            The description of the object in question
        """
        return self.desc

    def setDesc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "Caption":
        """
        This represents a general but brief (one paragraph) description what the object in question is about. It is only one paragraph! This property helps a human reader to identify the object in question. Tags: xml.sequenceOffset=10. A None value is a no-op and does not overwrite an existing desc.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.desc = value
        return self


class Url(ARObject):
    """
    This meta-class specifies an Uniform Resource Locator (URL).
    """

    # Url method parity checklist:
    # Spec: AUTOSAR_00052.xsd, complexType URL line 128502 (XSD-only; no own table in repo corpus)
    # XSD verified: AUTOSAR_00052.xsd
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] setMimeType    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMimeType    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setValue       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getValue       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # this denotes the mime type of the resource located by the url.
        self.mimeType: Optional[MimeTypeString] = None

        # The URL value represented by this object.
        self.value: Optional[UriString] = None

    def setMimeType(self, value: Optional[MimeTypeString]) -> "Url":
        """
        this denotes the mime type of the resource located by the url. A None value is a no-op and does not overwrite an existing mimeType.
        """
        if value is not None:
            self.mimeType = value
        return self

    def getMimeType(self) -> Optional[MimeTypeString]:
        """
        this denotes the mime type of the resource located by the url.
        """
        return self.mimeType

    def setValue(self, value: Optional[UriString]) -> "Url":
        """
        The URL value represented by this object. A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.value = value
        return self

    def getValue(self) -> Optional[UriString]:
        """
        The URL value represented by this object.
        """
        return self.value


__all__ = ["AlignEnum", "FloatEnum", "FrameEnum", "PgwideEnum", "ValignEnum", "Caption", "Url"]
