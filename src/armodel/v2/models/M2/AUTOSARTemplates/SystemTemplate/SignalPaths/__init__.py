"""
V2 M2::AUTOSARTemplates::SystemTemplate::SignalPaths package.
"""
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.CommonSignalPath import CommonSignalPath
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.ForbiddenSignalPath import ForbiddenSignalPath
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.PermissibleSignalPath import PermissibleSignalPath
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SeparateSignalPath import SeparateSignalPath
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SignalPathConstraint import SignalPathConstraint
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SwcToSwcOperationArguments import SwcToSwcOperationArguments
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.SwcToSwcSignal import SwcToSwcSignal

__all__ = [
    "CommonSignalPath",
    "ForbiddenSignalPath",
    "PermissibleSignalPath",
    "SeparateSignalPath",
    "SignalPathConstraint",
    "SwcToSwcOperationArguments",
    "SwcToSwcOperationArgumentsDirectionEnum",
    "SwcToSwcSignal",
]
