LineLayer
=========

The `deck.gl LineLayer <https://deck.gl/docs/api-reference/layers/line-layer>`_
renders straight lines between coordinates. Configure widths and colors using
the standard accessor props.

.. jupyter-execute::

   from ipydeck import Deck, Layer, ViewState

   bike_routes = Layer(
       type="LineLayer",
       data=[
           {
               "start": [-122.425, 37.77],
               "end": [-122.412, 37.785],
               "color": [34, 139, 34],
           },
           {
               "start": [-122.404, 37.79],
               "end": [-122.401, 37.793],
               "color": [70, 130, 180],
           },
       ],
       get_source_position="@@=start",
       get_target_position="@@=end",
       get_color="@@=color",
       get_width=5,
       pickable=True,
   )

   Deck(
       layers=[bike_routes],
       initial_view_state=ViewState(latitude=37.78, longitude=-122.41, zoom=13),
       tooltip={"text": "Segment"},
   )

Swap in ``great_circle=True`` when you need to draw curved connections instead
of straight segments.
