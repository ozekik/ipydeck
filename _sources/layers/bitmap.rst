BitmapLayer
===========

The `deck.gl BitmapLayer <https://deck.gl/docs/api-reference/layers/bitmap-layer>`_
projects a static image over geographic bounds. Provide ``bounds`` that describe
the rectangle in ``[west, south, east, north]`` order and an ``image`` URL or
numpy array.

.. jupyter-execute::

   from ipydeck import Deck, Layer, ViewState

   bitmap = Layer(
       type="BitmapLayer",
       data=None,
       bounds=[-122.519, 37.7045, -122.355, 37.829],
       image="https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/sf-districts.png",
       pickable=True,
   )

   Deck(
       layers=[bitmap],
       initial_view_state=ViewState(latitude=37.76, longitude=-122.43, zoom=11),
       tooltip={"text": "Pixel: {bitmap.pixel}"},
   )

Set ``opacity`` or ``color`` props if you want to tint the bitmap before it is
submitted to WebGL.
