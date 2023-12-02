from pydantic import Field

from typing import Any, List, Optional, Union

from .base import Layer


class GeoJsonLayer(Layer):
    type: str = Field(default="GeoJsonLayer")
    point_type: Optional[str] = None

    visible: Optional[bool] = None
    pickable: Optional[bool] = None
    opacity: Optional[float] = None
    auto_highlight: Optional[bool] = None
    # highlight_color: Optional[List[float]]

    filled: Optional[bool] = None
    get_fill_color: Optional[List[float] | str] = None

    stroked: Optional[bool] = None
    get_line_color: Optional[List[float]] = None
    get_line_width: Optional[float] = None
    line_width_units: Optional[str] = None
    line_width_scale: Optional[float] = None
    line_width_min_pixels: Optional[float] = None
    line_width_max_pixels: Optional[float] = None
    line_joint_rounded: Optional[bool] = None
    line_miter_limit: Optional[float] = None
    line_cap_rounded: Optional[bool] = None
    line_billboard: Optional[bool] = None

    extruded: Optional[bool] = None
    wireframe: Optional[bool] = None
    _full3d: Optional[bool] = None

    get_elevation: Optional[Union[float, str]] = None
    elevation_scale: Optional[float] = None
    material: Optional[Any] = None
