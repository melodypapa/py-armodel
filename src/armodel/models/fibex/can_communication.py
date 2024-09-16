from ..ar_object import ARObject
from .fibex_core import Frame

class CanFrame(Frame):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)