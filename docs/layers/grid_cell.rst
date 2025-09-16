GridCellLayer
=============

The `deck.gl GridCellLayer <https://deck.gl/docs/api-reference/layers/grid-cell-layer>`_
renders extruded grid cells, a lightweight alternative to `ColumnLayer` when you
already have evenly spaced data. Supply positions at cell centers and control
height via ``get_elevation``.

.. jupyter-execute::

   from ipydeck import Deck, Layer, ViewState

   heatmap = [
       {"position": [-122.42, 37.78], "value": 10},
       {"position": [-122.41, 37.78], "value": 30},
       {"position": [-122.42, 37.77], "value": 50},
       {"position": [-122.41, 37.77], "value": 5},
   ]

   grid = Layer(
       type="GridCellLayer",
       data=heatmap,
       cell_size=200,
       elevation_scale=100,
       extruded=True,
       get_position="@@=position",
       get_elevation="@@=value",
       get_fill_color=[255, 140, 0],
   )

   Deck(
       layers=[grid],
       initial_view_state=ViewState(latitude=37.775, longitude=-122.415, zoom=13, pitch=45),
   )

The ``cell_size`` prop is defined in meters when using a geographic view state.
