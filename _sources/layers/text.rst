TextLayer
=========

The `deck.gl TextLayer <https://deck.gl/docs/api-reference/layers/text-layer>`_
renders geolocated labels with font-based glyphs. You can size or rotate labels
with familiar accessor props.

.. jupyter-execute::

   from ipydeck import Deck, Layer, ViewState

   labels = Layer(
       type="TextLayer",
       data=[
           {"position": [-122.42, 37.78], "label": "Market"},
           {"position": [-122.406, 37.795], "label": "North Beach"},
       ],
       get_position="@@=position",
       get_text="@@=label",
       get_color=[0, 0, 0],
       get_size=16,
       size_units="pixels",
       background=True,
       font_family="Helvetica, Arial, sans-serif",
   )

   Deck(
       layers=[labels],
       initial_view_state=ViewState(latitude=37.79, longitude=-122.41, zoom=12),
   )

Use the ``get_angle`` accessor to rotate labels when aligning them to features
such as roads or rivers.
