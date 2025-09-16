PathLayer
=========

The `deck.gl PathLayer <https://deck.gl/docs/api-reference/layers/path-layer>`_
displays lines composed of multiple segments, ideal for routes or boundaries.
The ``path`` column contains a list of coordinates; ipydeck converts it to the
format deck.gl expects.

.. jupyter-execute::

   from ipydeck import Deck, Layer, ViewState

   waterfront = Layer(
       type="PathLayer",
       data=[
           {
               "name": "Embarcadero", 
               "path": [
                   [-122.397, 37.795],
                   [-122.393, 37.806],
                   [-122.399, 37.811],
                   [-122.403, 37.808],
               ],
               "color": [255, 140, 0],
           }
       ],
       get_path="@@=path",
       get_color="@@=color",
       get_width=6,
       pickable=True,
   )

   Deck(
       layers=[waterfront],
       initial_view_state=ViewState(latitude=37.804, longitude=-122.399, zoom=13.5),
       tooltip={"text": "{name}"},
   )

Enable ``rounded=True`` or ``width_units='pixels'`` to fine-tune the rendering
for high-DPI displays.
