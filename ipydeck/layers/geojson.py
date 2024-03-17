from dataclasses import dataclass
from typing import Any, List, Optional, Union

from .base import Layer

@dataclass
class GeoJsonLayer(Layer):
    def __init__(
        self,
        type: str = "GeoJsonLayer",
        data: Any | None = None,
        id: str | None = None,
        *,
        point_type: Optional[str] = None,
        visible: Optional[bool] = None,
        pickable: Optional[bool] = None,
        opacity: Optional[float] = None,
        auto_highlight: Optional[bool] = None,
        filled: Optional[bool] = None,
        get_fill_color: Optional[List[float] | str] = None,
        stroked: Optional[bool] = None,
        get_line_color: Optional[List[float]] = None,
        get_line_width: Optional[float] = None,
        line_width_units: Optional[str] = None,
        line_width_scale: Optional[float] = None,
        line_width_min_pixels: Optional[float] = None,
        line_width_max_pixels: Optional[float] = None,
        line_joint_rounded: Optional[bool] = None,
        line_miter_limit: Optional[float] = None,
        line_cap_rounded: Optional[bool] = None,
        line_billboard: Optional[bool] = None,
        extruded: Optional[bool] = None,
        wireframe: Optional[bool] = None,
        _full3d: Optional[bool] = None,
        get_elevation: Optional[Union[float, str]] = None,
        elevation_scale: Optional[float] = None,
        material: Optional[Any] = None,
    ):
        self.type = type
        self.data = data
        self.id = id
        self.point_type = point_type
        self.visible = visible
        self.pickable = pickable
        self.opacity = opacity
        self.auto_highlight = auto_highlight
        self.filled = filled
        self.get_fill_color = get_fill_color
        self.stroked = stroked
        self.get_line_color = get_line_color
        self.get_line_width = get_line_width
        self.line_width_units = line_width_units
        self.line_width_scale = line_width_scale
        self.line_width_min_pixels = line_width_min_pixels
        self.line_width_max_pixels = line_width_max_pixels
        self.line_joint_rounded = line_joint_rounded
        self.line_miter_limit = line_miter_limit
        self.line_cap_rounded = line_cap_rounded
        self.line_billboard = line_billboard
        self.extruded = extruded
        self.wireframe = wireframe
        self._full3d = _full3d
        self.get_elevation = get_elevation
        self.elevation_scale = elevation_scale
        self.material = material
