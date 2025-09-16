SolidPolygonLayer
=================

The `deck.gl SolidPolygonLayer <https://deck.gl/docs/api-reference/layers/solid-polygon-layer>`_
generates extruded 3D surfaces from polygons. Unlike :doc:`polygon`, it always
renders as a solid volume and supports complex shapes with holes.

.. jupyter-execute::

   from ipydeck import Deck, Layer, ViewState

   hills = Layer(
       type="SolidPolygonLayer",
       data=[
           {
               "name": "Twin Peaks",
               "polygon": [
                   [-122.4477, 37.7543],
                   [-122.4401, 37.7514],
                   [-122.4436, 37.7447],
                   [-122.4522, 37.748],
               ],
               "elevation": 150,
           }
       ],
       get_polygon="@@=polygon",
       get_elevation="@@=elevation",
       get_fill_color=[102, 205, 170],
       extruded=True,
       pickable=True,
   )

   Deck(
       layers=[hills],
       initial_view_state=ViewState(latitude=37.75, longitude=-122.446, zoom=13, pitch=45),
       tooltip={"text": "{name}"},
   )

Add ``wireframe=True`` to display polygon edges alongside the filled surface.
