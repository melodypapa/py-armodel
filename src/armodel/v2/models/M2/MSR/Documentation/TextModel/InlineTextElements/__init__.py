"""
V2 M2::MSR::Documentation::TextModel::InlineTextElements package.
"""
from armodel.v2.models.M2.MSR.Documentation.TextModel.Br import Br
from armodel.v2.models.M2.MSR.Documentation.TextModel.EmphasisText import (
    EmphasisText,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.IndexEntry import (
    IndexEntry,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.Std import Std
from armodel.v2.models.M2.MSR.Documentation.TextModel.Tt import Tt
from armodel.v2.models.M2.MSR.Documentation.TextModel.Xdoc import Xdoc
from armodel.v2.models.M2.MSR.Documentation.TextModel.Xfile import Xfile
from armodel.v2.models.M2.MSR.Documentation.TextModel.Xref import Xref
from armodel.v2.models.M2.MSR.Documentation.TextModel.XrefTarget import (
    XrefTarget,
)

__all__ = [
    Br,
    "EmphasisText",
    "IndexEntry",
    Std,
    "Superscript",
    Tt,
    Xdoc,
    Xfile,
    Xref,
    "XrefTarget",
]
