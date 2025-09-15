from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass
class ViewState:
    """Camera state for a deck.gl scene.

    Attributes mirror the fields that deck.gl expects when instantiating a
    ``ViewState`` object on the JavaScript side.

    Examples
    --------
    >>> from ipydeck.view_state import ViewState
    >>> view_state = ViewState(latitude=37.8, longitude=-122.4, zoom=11)
    >>> view_state.serialize()["zoom"]
    11
    """
    longitude: float | None = None
    latitude: float | None = None
    zoom: int | None = None
    min_zoom: int | None = None
    max_zoom: int | None = None
    pitch: float | None = None
    bearing: float | None = None

    def serialize(self) -> dict:
        """Return a JSON-serializable dict that matches deck.gl's schema.

        Examples
        --------
        >>> from ipydeck.view_state import ViewState
        >>> ViewState(latitude=51.5, longitude=-0.1).serialize()["latitude"]
        51.5
        """
        return asdict(self)
