import json
from typing import Any, List, Optional

from pydantic import BaseModel, ConfigDict, field_validator
from pydantic.alias_generators import to_camel

from ipydeck.utils import (
    has_geo_interface,
    is_geopandas_df,
    is_pandas_df,
    records_from_geo_interface,
)


class Layer(BaseModel):
    model_config = ConfigDict(extra="allow")

    type: str
    id: Optional[str] = None
    data: Optional[Any] = None

    visible: Optional[bool] = None
    pickable: Optional[bool] = None  # True
    opacity: Optional[float] = None  # 1

    @field_validator("data", mode="before")
    @classmethod
    def transform_data(cls, data: Any) -> dict | List[dict]:
        if is_pandas_df(data):
            return data.to_dict(orient="records")
        elif is_geopandas_df(data):
            return json.loads(data.to_json())
        elif has_geo_interface(data):
            return records_from_geo_interface(data)
        else:
            return data

    def serialize(self):
        dump = self.model_dump()
        dump = {to_camel(k): v for k, v in dump.items()}
        # print("dump", dump)
        return dump
