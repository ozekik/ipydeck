from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass
class ViewState:
    longitude: float | None = None
    latitude: float | None = None
    zoom: int | None = None
    min_zoom: int | None = None
    max_zoom: int | None = None
    pitch: float | None = None
    bearing: float | None = None

    def serialize(self) -> dict:
        return asdict(self)
