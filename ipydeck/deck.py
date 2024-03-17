from __future__ import annotations

from dataclasses import asdict
from logging import getLogger
from pathlib import Path
from typing import Dict, List

import anywidget
import traitlets

from .base_map import DefaultBaseMap
from .layers.base import Layer
from .view_state import ViewState

logger = getLogger(__name__)


class Deck(anywidget.AnyWidget):
    _esm = Path(__file__).parent / "static/widget.js"
    _css = Path(__file__).parent / "static/widget.css"

    initial_view_state = traitlets.Instance(ViewState)
    layers = traitlets.List()
    width = traitlets.Union([traitlets.Unicode(), traitlets.Int()]).tag(sync=True)
    height = traitlets.Union([traitlets.Unicode(), traitlets.Int()]).tag(sync=True)
    map_style = traitlets.Unicode("dark").tag(sync=True)

    # NOTE: Avoid name collision with ipywidgets' tooltip
    _tooltip = traitlets.Dict(allow_none=True).tag(sync=True)

    _initial_view_state = traitlets.Dict().tag(sync=True)
    _layers = traitlets.List().tag(sync=True)

    # @traitlets.observe("layers")
    # def _update_layers(self, change):
    #     # print(change)
    #     layers = change["new"]
    #     self._layers = list(map(lambda x: x.serialize(), layers))

    def update(self):
        self._layers = list(map(lambda x: x.serialize(), self.layers))

    def __init__(
        self,
        layers: List[Layer] = [],
        # views=None,
        map_style="dark",
        initial_view_state: ViewState = ViewState(latitude=0, longitude=0, zoom=1),
        width: int | str = "100%",
        height: int | str = 500,
        tooltip: Dict | None = None,
        map_provider="carto",
        api_keys=None,
    ):
        self.inital_view_state = initial_view_state
        self.layers = layers
        self.width = width
        self.height = height
        self._tooltip = tooltip

        if map_style in DefaultBaseMap.short_names:
            map_style = DefaultBaseMap.short_names[map_style]
        self.map_style = map_style

        logger.debug(layers[0].serialize())

        self._initial_view_state = asdict(initial_view_state)
        self._layers = list(map(lambda x: x.serialize(), layers))

        super().__init__()
