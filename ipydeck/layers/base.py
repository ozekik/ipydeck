from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from typing import Any

from ipydeck.utils import (
    has_geo_interface,
    is_geopandas_df,
    is_pandas_df,
    records_from_geo_interface,
)


def to_camel(s: str):
    parts = iter(s.split("_"))
    return next(parts) + "".join(i.title() for i in parts)


@dataclass
class Layer:
    """Base representation of a deck.gl layer.

    The class normalizes Python data structures so they can be serialized and
    consumed by the front-end widget. Subclasses typically provide sensible
    defaults for ``type`` along with any layer-specific keyword arguments.

    Examples
    --------
    >>> from ipydeck.layers.base import Layer
    >>> layer = Layer(
    ...     type="ScatterplotLayer",
    ...     data=[{"position": [-122.4, 37.8]}],
    ... )
    >>> layer.serialize()["type"]
    'ScatterplotLayer'
    """
    type: str
    data: Any | None = None
    id: str | None = None
    visible: bool | None = None
    pickable: bool | None = None
    opacity: float | None = None
    on_click: bool | None = None

    def __init__(
        self,
        type: str,
        data: Any | None = None,
        id: str | None = None,
        *,
        visible: bool | None = None,
        pickable: bool | None = None,
        opacity: float | None = None,
        on_click: bool | None = None,
        **kwargs,
    ):
        """Instantiate a deck.gl layer definition.

        Parameters
        ----------
        type
            deck.gl layer type, for example ``ScatterplotLayer``.
        data
            Optional source data. Pandas, GeoPandas, and Geo Interface objects
            are automatically converted into JSON-friendly structures.
        id
            Stable identifier used to diff layers between renders.
        visible
            Whether the layer is drawn in the current frame.
        pickable
            Enables pointer interaction in deck.gl if ``True``.
        opacity
            Base alpha multiplier provided to deck.gl.
        on_click
            Whether click events should be forwarded to Python.
        **kwargs
            Additional properties that are passed through to deck.gl unchanged.
        """
        if data is not None:
            if is_pandas_df(data):
                # NOTE: This doesn't work for GeoJSON, but could be useful for other formats
                data = data.to_dict(orient="records")
            elif is_geopandas_df(data):
                data = json.loads(data.to_json())
            elif has_geo_interface(data):
                data = records_from_geo_interface(data)

        self.type = type
        self.id = id
        self.data = data
        self.visible = visible
        self.pickable = pickable
        self.opacity = opacity
        self.on_click = on_click
        self._kwargs = kwargs

    def serialize(self):
        """Return a JSON-serializable representation of the layer.

        Examples
        --------
        >>> from ipydeck.layers.base import Layer
        >>> Layer(type="TextLayer", data=[{"text": "hello"}]).serialize()["type"]
        'TextLayer'
        """
        dump = asdict(self)
        dump.update(self._kwargs)
        dump = {to_camel(k): v for k, v in dump.items()}
        return dump
