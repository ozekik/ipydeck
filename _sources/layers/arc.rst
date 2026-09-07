ArcLayer
========

The `deck.gl ArcLayer <https://deck.gl/docs/api-reference/layers/arc-layer>`_
draws great-circle or straight arcs between pairs of coordinates. Use it to
visualize connections such as flights or telecommunication routes. The accessor
props mirror deck.gl's API—``get_source_position`` and ``get_target_position``
accept column names when prefixed with ``@@=``.

.. jupyter-execute::

   from ipydeck import Deck, Layer, ViewState

   flights = Layer(
       type="ArcLayer",
       data=[
           {
               "start": [-122.389977, 37.618972],  # SFO
               "end": [-73.778139, 40.641311],     # JFK
           },
           {
               "start": [-118.40853, 33.94159],    # LAX
               "end": [-87.9048, 41.9742],         # ORD
           },
       ],
       get_source_position="@@=start",
       get_target_position="@@=end",
       get_source_color=[0, 92, 191],
       get_target_color=[255, 89, 94],
       get_width=4,
       great_circle=True,
   )

   Deck(
       layers=[flights],
       initial_view_state=ViewState(latitude=39, longitude=-98, zoom=3.3),
   )

For dense datasets consider supplying a Pandas ``DataFrame`` or GeoPandas
geometry; :class:`ipydeck.Layer` will normalize it before serialization.
