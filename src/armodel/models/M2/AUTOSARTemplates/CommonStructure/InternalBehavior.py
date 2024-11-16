from enum import Enum

class ReentrancyLevelEnum(Enum):

    multicoreReentrant = "multicoreReentrant"
    nonReentrant = "nonReentrant"
    singleCoreReentrant = "singleCoreReentrant"