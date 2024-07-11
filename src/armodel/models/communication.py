from . import ARObject

class TransmissionAcknowledgementRequest(ARObject):
    def __init__(self):
        super().__init__()

        self.timeout = None     # type: float

