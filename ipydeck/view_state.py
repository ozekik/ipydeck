from dataclasses import asdict, dataclass
from typing import Optional


@dataclass
class ViewState:
    longitude: float = None
    latitude: float = None
    zoom: int = None
    min_zoom: Optional[int] = None
    max_zoom: Optional[int] = None
    pitch: Optional[float] = None
    bearing: Optional[float] = None

    def serialize(self) -> dict:
        return asdict(self)
