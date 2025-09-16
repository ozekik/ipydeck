ColumnLayer
===========

The `deck.gl ColumnLayer <https://deck.gl/docs/api-reference/layers/column-layer>`_
creates cylindrical columns at supplied coordinates. Pair ``get_elevation`` with
``extruded=True`` to produce 3D charts, and tweak ``radius`` or
``disk_resolution`` to control shape.

.. jupyter-execute::

   from ipydeck import Deck, Layer, ViewState

   population = [
       {"position": [-122.42, 37.78], "value": 1000},
       {"position": [-122.41, 37.76], "value": 4000},
       {"position": [-122.39, 37.75], "value": 2500},
   ]

   columns = Layer(
       type="ColumnLayer",
       data=population,
       disk_resolution=12,
       radius=250,
       extruded=True,
       elevation_scale=20,
       get_position="@@=position",
       get_elevation="@@=value",
       get_fill_color=[24, 128, 56],
   )

   Deck(
       layers=[columns],
       initial_view_state=ViewState(latitude=37.77, longitude=-122.41, zoom=12.5, pitch=45),
   )

Feed GeoJSON features or pandas data frames directly; ipydeck converts them into
a serializable form behind the scenes.
