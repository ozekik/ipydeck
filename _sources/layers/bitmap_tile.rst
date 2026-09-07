BitmapTileLayer
===============

Use :class:`~ipydeck.layers.BitmapTileLayer` to display XYZ raster tiles such as
OpenStreetMap or custom imagery. The class wraps deck.gl's `TileLayer
<https://deck.gl/docs/api-reference/geo-layers/tile-layer>`_ with an embedded
``BitmapLayer`` for each tile. The ``data`` argument accepts either a tile URL
template (with ``{x}``, ``{y}``, ``{z}`` placeholders) or a callable that returns
per-tile metadata.

The snippet below wires ipydeck to the public OpenStreetMap tile service. When
rendered in Jupyter the widget requests tiles dynamically as you pan and zoom.
You can tweak ``tile_size``, ``min_zoom``, and ``max_zoom`` to match the backing
service.

.. jupyter-execute::

   from ipydeck import Deck, ViewState
   from ipydeck.layers import BitmapTileLayer

   tiles = BitmapTileLayer(
       data="https://tile.openstreetmap.org/{z}/{x}/{y}.png",
       tile_size=256,
       min_zoom=0,
       max_zoom=19,
   )

   Deck(
       layers=[tiles],
       initial_view_state=ViewState(latitude=37.7749, longitude=-122.4194, zoom=9),
   )

If your imagery is hosted privately, configure authentication headers in the
front-end ``Deck`` ``getTooltip`` callback or proxy requests through your
application server before handing URLs to the layer.
