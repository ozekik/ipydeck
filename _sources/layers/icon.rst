IconLayer
=========

The `deck.gl IconLayer <https://deck.gl/docs/api-reference/layers/icon-layer>`_
places textured billboards on the map. Provide an ``icon_atlas`` image containing
sprites and an ``icon_mapping`` that describes sprite bounds. The mapping below
reuses the public deck.gl icon atlas.

.. jupyter-execute::

   from ipydeck import Deck, Layer, ViewState

   cities = Layer(
       type="IconLayer",
       data=[
           {"position": [-122.4, 37.8], "name": "San Francisco"},
           {"position": [-73.98, 40.75], "name": "New York"},
       ],
       icon_atlas="https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/icon-atlas.png",
       icon_mapping="https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/icon-atlas.json",
       get_position="@@=position",
       get_size=40,
       get_icon="@@='marker'",
       get_color=[0, 0, 255],
       pickable=True,
   )

   Deck(
       layers=[cities],
       initial_view_state=ViewState(latitude=39.5, longitude=-96, zoom=3),
       tooltip={"text": "{name}"},
   )

To drive the icon accessor from data, return the sprite key with
``get_icon="@@=icon_id"`` and include an ``icon_id`` field in each row.
