from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .base import Layer


@dataclass
class BitmapTileLayer(Layer):
    def __init__(
        self,
        type: str = "BitmapTileLayer",
        data: Any | None = None,
        id: str | None = None,
        *,
        tile_size: int = 256,
        max_zoom: int | None = None,
        min_zoom: int = 0,
    ):
        self.type = type
        self.data = data
        self.id = id
        self.tile_size = tile_size
        self.max_zoom = max_zoom
        self.min_zoom = min_zoom
