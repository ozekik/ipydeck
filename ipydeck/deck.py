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
    """Interactive deck.gl map widget for Jupyter front ends.

    The widget mirrors the deck.gl JavaScript API and keeps a serialized
    representation of the scene in sync with the front-end bundle that lives
    in :mod:`ipydeck.static`. Only a subset of the traitlets are exposed to the
    browser; internal counterparts prefixed with an underscore are used for the
    JSON payload that is consumed by the client.

    Examples
    --------
    Instantiate a :class:`Deck` with a custom view state and inspect one of the
    synchronized attributes:

        >>> from ipydeck import Deck, ViewState
        >>> deck = Deck(
        ...     layers=[],
        ...     initial_view_state=ViewState(latitude=37.8, longitude=-122.4, zoom=11),
        ... )
        >>> deck.initial_view_state.latitude
        37.8
    """
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

    # Reactive properties
    click = traitlets.Dict(allow_none=True).tag(sync=True)

    # @traitlets.observe("click")
    # def _handle_click(self, change):
    #     print(change)

    # @traitlets.observe("layers")
    # def _update_layers(self, change):
    #     # print(change)
    #     layers = change["new"]
    #     self._layers = list(map(lambda x: x.serialize(), layers))

    def update(self):
        """Recompute the serialized layer payload.

        Call this after mutating a layer in-place so that the front end receives
        an updated list of serialized layers.

        Examples
        --------
        >>> from ipydeck import Deck
        >>> from ipydeck.layers.base import Layer
        >>> layer = Layer(type="ScatterplotLayer", data=[{"value": 1}])
        >>> deck = Deck(layers=[layer])
        >>> layer.opacity = 0.5
        >>> deck.update()
        >>> deck._layers[0]["opacity"]
        0.5
        """
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
        """Create a :class:`Deck` widget configured with one or more layers.

        Parameters
        ----------
        layers
            Sequence of :class:`~ipydeck.layers.base.Layer` instances to render.
        map_style
            Basemap identifier understood by deck.gl or one of the short names
            defined on :class:`ipydeck.base_map.DefaultBaseMap`.
        initial_view_state
            Camera configuration for the first render.
        width
            Widget width expressed in pixels or CSS units.
        height
            Widget height expressed in pixels.
        tooltip
            Mapping passed straight through to deck.gl's tooltip handler.
        map_provider
            Map tile provider identifier; stored for compatibility with the
            JavaScript side even though it is not consumed directly in Python.
        api_keys
            Provider specific API keys. Retained for symmetry with the front
            end even if the Python class does not use the value directly.
        """
        self.initial_view_state = initial_view_state
        self.layers = layers
        self.width = width
        self.height = height
        self._tooltip = tooltip

        if map_style in DefaultBaseMap.short_names:
            map_style = DefaultBaseMap.short_names[map_style]
        self.map_style = map_style

        logger.debug(layers[0].serialize() if layers else "no layers")

        self._initial_view_state = asdict(initial_view_state)
        self._layers = list(map(lambda x: x.serialize(), layers))

        super().__init__()
