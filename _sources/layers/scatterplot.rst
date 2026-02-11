ScatterplotLayer
================

The `deck.gl ScatterplotLayer <https://deck.gl/docs/api-reference/layers/scatterplot-layer>`_
is a versatile point renderer. Provide numeric ``radius`` values and let deck.gl
handle device-independent sizing by passing ``radius_units='meters'`` or
``'pixels'``.

.. jupyter-execute::

   from ipydeck import Deck, Layer, ViewState

   stops = Layer(
       type="ScatterplotLayer",
       data=[
           {"position": [-122.41, 37.784], "name": "Powell St", "ridership": 1200},
           {"position": [-122.419, 37.776], "name": "Civic Center", "ridership": 900},
           {"position": [-122.393, 37.776], "name": "Embarcadero", "ridership": 1500},
       ],
       get_position="@@=position",
       get_radius="@@=ridership",
       get_fill_color=[64, 170, 191],
       radius_scale=0.5,
       radius_units="meters",
       pickable=True,
   )

   Deck(
       layers=[stops],
       initial_view_state=ViewState(latitude=37.78, longitude=-122.41, zoom=10),
       tooltip={"text": "{name}"},
   )

For categorical styling, provide an array to ``get_fill_color`` or map values to
palettes in Python before serialization.
