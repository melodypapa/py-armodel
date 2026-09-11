from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum


class ChapterEnumBreak(AREnum):
    """
    This allows to specify the page break policy of a paginatable element.
    """

    # ChapterEnumBreak method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.61, p.330
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Paginateable.break (BREAK attribute)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # This indicates the a page break shall be applied before the current block. Tags: atp.EnumerationLiteralIndex=0
    BREAK = "BREAK"

    # This indicates that there is no need to force a page break before this block. Tags: atp.EnumerationLiteralIndex=1
    NO_BREAK = "NO-BREAK"

    def __init__(self):
        super().__init__((ChapterEnumBreak.BREAK, ChapterEnumBreak.NO_BREAK))


class KeepWithPreviousEnum(AREnum):
    """ """

    # KeepWithPreviousEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.76, p.340
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on Paginateable.keepWithPrevious (KEEP-WITH-PREVIOUS attribute)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # This indicates that the block shall be kept together with the previous block. Tags: atp.EnumerationLiteralIndex=0
    KEEP = "KEEP"

    # This indicates that there is no need to keep the block with the previous one. This is the same as if the attribute itself is missing. Tags: atp.EnumerationLiteralIndex=1
    NO_KEEP = "NO-KEEP"

    def __init__(self):
        super().__init__((KeepWithPreviousEnum.KEEP, KeepWithPreviousEnum.NO_KEEP))


class DocumentViewSelectable(ARObject, ABC):
    """
    Abstract base class for elements that can be selected in a document
    view.
    """

    # DocumentViewSelectable method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is DocumentViewSelectable:
            raise TypeError("DocumentViewSelectable is an abstract class.")
        super().__init__()


class Paginateable(DocumentViewSelectable, ABC):
    """
    This meta-class represents the ability to control the pagination policy when creating documents.
    """

    # Paginateable method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.75, p.339
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBreak            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBreak            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getKeepWithPrevious [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setKeepWithPrevious [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is Paginateable:
            raise TypeError("Paginateable is an abstract class.")
        super().__init__()

        # This attributes allows to specify a forced page break. Tags: xml.attribute=true
        self.chapterBreak: Optional[ChapterEnumBreak] = None

        # This attribute denotes the pagination policy. In particular it defines if the containing text block shall be kept together with the previous block. Tags: xml.attribute=true
        self.keepWithPrevious: Optional[KeepWithPreviousEnum] = None

    def getBreak(self) -> Optional[ChapterEnumBreak]:
        """
        This attributes allows to specify a forced page break. Tags: xml.attribute=true
        """
        return self.chapterBreak

    def setBreak(self, value: Optional[ChapterEnumBreak]) -> "Paginateable":
        """
        This attributes allows to specify a forced page break. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing chapterBreak.
        """
        if value is not None:
            self.chapterBreak = value
        return self

    def getKeepWithPrevious(self) -> Optional[KeepWithPreviousEnum]:
        """
        This attribute denotes the pagination policy. In particular it defines if the containing text block shall be kept together with the previous block. Tags: xml.attribute=true
        """
        return self.keepWithPrevious

    def setKeepWithPrevious(self, value: Optional[KeepWithPreviousEnum]) -> "Paginateable":
        """
        This attribute denotes the pagination policy. In particular it defines if the containing text block shall be kept together with the previous block. Tags: xml.attribute=true. A None value is a no-op and does not overwrite an existing keepWithPrevious.
        """
        if value is not None:
            self.keepWithPrevious = value
        return self


__all__ = ["ChapterEnumBreak", "DocumentViewSelectable", "KeepWithPreviousEnum", "Paginateable"]
