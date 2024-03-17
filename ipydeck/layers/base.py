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
    type: str
    data: Any | None = None
    id: str | None = None
    visible: bool | None = None
    pickable: bool | None = None
    opacity: float | None = None

    def __init__(
        self,
        type: str,
        data: Any | None = None,
        id: str | None = None,
        *,
        visible: bool | None = None,
        pickable: bool | None = None,
        opacity: float | None = None,
        **kwargs,
    ):
        if data is not None:
            if is_pandas_df(data):
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
        self._kwargs = kwargs

    def serialize(self):
        dump = asdict(self)
        dump.update(self._kwargs)
        dump = {to_camel(k): v for k, v in dump.items()}
        return dump
