from .view_state import ViewState  # noqa
from .layers import Layer, GeoJsonLayer  # noqa
from .deck import Deck  # noqa
from .base_map import DefaultBaseMap, CartoBaseMap  # noqa

import importlib.metadata

try:
    __version__ = importlib.metadata.version("ipydeck")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"
