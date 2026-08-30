from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, String

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class MsrQueryArg(ARObject):
    """
    This represents an argument to the query. Note that the arguments are not standardized and therefore subject to mutual agreement.
    """

    # MsrQueryArg method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.86, p.344
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getArg       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setArg       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSi        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSi        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This is the value of the argument.
        self.arg: Optional[String] = None

        # This denotes the name of the query argument (semantic information)
        self.si: Optional[NameToken] = None

    def getArg(self) -> Optional[String]:
        """
        This is the value of the argument.

        Returns:
            The value of the argument
        """
        return self.arg

    def setArg(self, value: Optional[String]) -> "MsrQueryArg":
        """
        This is the value of the argument. A None value is a no-op and does not overwrite an existing arg.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.arg = value
        return self

    def getSi(self) -> Optional[NameToken]:
        """
        This denotes the name of the query argument (semantic information)

        Returns:
            The name of the query argument
        """
        return self.si

    def setSi(self, value: Optional[NameToken]) -> "MsrQueryArg":
        """
        This denotes the name of the query argument (semantic information). A None value is a no-op and does not overwrite an existing si.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.si = value
        return self


class MsrQueryProps(ARObject):
    """
    This metaclass represents the ability to specificy a query which yields some documentation text. The qualities of the result are determined by the context in which the query is used.
    """

    # MsrQueryProps method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.85, p.344
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getComment        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setComment        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMsrQueryName   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMsrQueryName   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addMsrQueryArg    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMsrQueryArgs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer

    def __init__(self):
        super().__init__()

        # This element contains a commentary in text form.
        self.comment: Optional[String] = None

        # This element specifies the name of the MSR-QUERY triggered.
        self.msrQueryName: Optional[String] = None

        # This element specifies an argument within an MsrQuery.
        self.msrQueryArgs: List[MsrQueryArg] = []

    def getComment(self) -> Optional[String]:
        """
        This element contains a commentary in text form.

        Returns:
            The commentary in text form
        """
        return self.comment

    def setComment(self, value: Optional[String]) -> "MsrQueryProps":
        """
        This element contains a commentary in text form. A None value is a no-op and does not overwrite an existing comment.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.comment = value
        return self

    def getMsrQueryName(self) -> Optional[String]:
        """
        This element specifies the name of the MSR-QUERY triggered.

        Returns:
            The name of the MSR-QUERY triggered
        """
        return self.msrQueryName

    def setMsrQueryName(self, value: Optional[String]) -> "MsrQueryProps":
        """
        This element specifies the name of the MSR-QUERY triggered. A None value is a no-op and does not overwrite an existing msrQueryName.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.msrQueryName = value
        return self

    def addMsrQueryArg(self, value: Optional[MsrQueryArg]) -> "MsrQueryProps":
        """
        This element specifies an argument within an MsrQuery. A None value is a no-op and is not appended.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.msrQueryArgs.append(value)
        return self

    def getMsrQueryArgs(self) -> List[MsrQueryArg]:
        """
        This element specifies an argument within an MsrQuery.

        Returns:
            The arguments within the MsrQuery
        """
        return self.msrQueryArgs


class MsrQueryP2(ARObject):
    """
    This meta-class represents the ability to express a query which yields the content of a Documentation Block as a result.
    """

    # MsrQueryP2 method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.56, p.456
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getMsrQueryProps        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMsrQueryProps        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMsrQueryResultP2     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMsrQueryResultP2     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This is argument and properties of the Documentation Block query.
        self.msrQueryProps: Optional[MsrQueryProps] = None

        # This represents the result of the query.
        self.msrQueryResultP2: Optional["DocumentationBlock"] = None

    def getMsrQueryProps(self) -> Optional[MsrQueryProps]:
        """
        This is argument and properties of the Documentation Block query.

        Returns:
            The argument and properties of the Documentation Block query
        """
        return self.msrQueryProps

    def setMsrQueryProps(self, value: Optional[MsrQueryProps]) -> "MsrQueryP2":
        """
        This is argument and properties of the Documentation Block query. A None value is a no-op and does not overwrite an existing msrQueryProps.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.msrQueryProps = value
        return self

    def getMsrQueryResultP2(self) -> Optional["DocumentationBlock"]:
        """
        This represents the result of the query.

        Returns:
            The result of the query
        """
        return self.msrQueryResultP2

    def setMsrQueryResultP2(self, value: Optional["DocumentationBlock"]) -> "MsrQueryP2":
        """
        This represents the result of the query. A None value is a no-op and does not overwrite an existing msrQueryResultP2.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.msrQueryResultP2 = value
        return self


class MsrQueryP1(ARObject):
    """
    This meta-class represents the ability to express a query which yields the content of a topic as a result.

    NOTE: stub placeholder for the MSR::Documentation::MsrQuery MsrQueryP1 type
    (Table 9.82); the full content model is not yet synced. Referred to by
    TopicContentOrMsrQuery.msrQueryP1.
    """

    # MsrQueryP1 method parity checklist (stub):
    # Spec: not synced (MSR Documentation subtree)
    # (no methods)

    def __init__(self):
        super().__init__()


class MsrQueryChapter(ARObject):
    """
    This meta-class represents the ability to express a query which yields a set of chapters as a result.
    """

    # MsrQueryChapter method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.84, p.343
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setMsrQueryProps       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMsrQueryProps       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [ ] setMsrQueryResultChapter  [x] impl  [ ] docstring  [ ] test  [ ] reader  [ ] writer
    # [ ] getMsrQueryResultChapter  [x] impl  [ ] docstring  [ ] test  [ ] reader  [ ] writer
    #
    # NOTE: msrQueryResultChapter (MsrQueryResultChapter, 0..1, aggr) is not modeled
    # yet — the MsrQueryResultChapter class is a deferred placeholder (Rule 0001.10);
    # the stamp is omitted until the real type lands.

    def __init__(self):
        super().__init__()

        # This is argument and properties of the chapter query.
        self.msrQueryProps: Optional[MsrQueryProps] = None

    def setMsrQueryProps(self, value: Optional[MsrQueryProps]) -> "MsrQueryChapter":
        """
        This is argument and properties of the chapter query.

        A None value is a no-op and does not overwrite an existing msrQueryProps.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.msrQueryProps = value
        return self

    def getMsrQueryProps(self) -> Optional[MsrQueryProps]:
        """
        This is argument and properties of the chapter query.

        Returns:
            The argument and properties of the chapter query
        """
        return self.msrQueryProps


class MsrQueryTopic1(ARObject):
    """
    This meta-class represents the ability to specify a query which yields a set of topics as a result.
    """

    # MsrQueryTopic1 method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.83, p.343
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setMsrQueryProps       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMsrQueryProps       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [ ] setMsrQueryResultTopic1  [x] impl  [ ] docstring  [ ] test  [ ] reader  [ ] writer
    # [ ] getMsrQueryResultTopic1  [x] impl  [ ] docstring  [ ] test  [ ] reader  [ ] writer
    #
    # NOTE: msrQueryResultTopic1 (MsrQueryResultTopic1, 0..1, aggr) is not modeled
    # yet — the MsrQueryResultTopic1 class is a deferred placeholder (Rule 0001.10);
    # the stamp is omitted until the real type lands.

    def __init__(self):
        super().__init__()

        # This is argument and properties of the topic query.
        self.msrQueryProps: Optional[MsrQueryProps] = None

    def setMsrQueryProps(self, value: Optional[MsrQueryProps]) -> "MsrQueryTopic1":
        """
        This is argument and properties of the topic query.

        A None value is a no-op and does not overwrite an existing msrQueryProps.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.msrQueryProps = value
        return self

    def getMsrQueryProps(self) -> Optional[MsrQueryProps]:
        """
        This is argument and properties of the topic query.

        Returns:
            The argument and properties of the topic query
        """
        return self.msrQueryProps
