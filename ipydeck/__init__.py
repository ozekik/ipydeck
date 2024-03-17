import importlib.metadata

from .base_map import CartoBaseMap, DefaultBaseMap
from .deck import Deck
from .layers import GeoJsonLayer, Layer
from .view_state import ViewState

try:
    __version__ = importlib.metadata.version("ipydeck")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"

__all__ = [
    "Layer",
    "GeoJsonLayer",
    "ViewState",
    "Deck",
    "DefaultBaseMap",
    "CartoBaseMap",
]
