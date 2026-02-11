PolygonLayer
============

The `deck.gl PolygonLayer <https://deck.gl/docs/api-reference/layers/polygon-layer>`_
renders filled polygons from GeoJSON-like structures. The ``polygon`` column can
be a list of coordinates or a GeoJSON feature geometry.

.. jupyter-execute::

   from ipydeck import Deck, Layer, ViewState

   neighborhoods = Layer(
       type="PolygonLayer",
       data=[
           {
               "name": "Mission",
               "polygon": [
                   [-122.422, 37.759],
                   [-122.411, 37.759],
                   [-122.411, 37.747],
                   [-122.422, 37.747],
               ],
               "color": [255, 99, 71],
           }
       ],
       get_polygon="@@=polygon",
       get_fill_color="@@=color",
       stroked=True,
       extruded=False,
       pickable=True,
   )

   Deck(
       layers=[neighborhoods],
       initial_view_state=ViewState(latitude=37.755, longitude=-122.416, zoom=13),
       tooltip={"text": "{name}"},
   )

Set ``extruded=True`` and provide ``get_elevation`` for 3D effects.
