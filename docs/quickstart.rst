Quickstart
==========

Getting Started
---------------

Install ipydeck into your environment. The package ships as a standard Python
wheel, so any installer that understands ``pyproject.toml`` metadata will work.

.. code-block:: bash

   pip install ipydeck

If you prefer using `uv <https://docs.astral.sh/uv/>`_ you can instead run::

   uv add ipydeck

Create Your First Deck
----------------------

Launch a Jupyter notebook and construct a ``Deck`` widget. The example below
renders a scatterplot centered on San Francisco.

.. jupyter-execute::

   from ipydeck import Deck, Layer, ViewState

   scatter = Layer(
       type="ScatterplotLayer",
       data=[{"position": [-122.4, 37.8], "radius": 1200}],
       get_position="@@=position",
       get_radius="@@=radius",
       get_fill_color=[0, 0, 255],
       pickable=True,
   )

   deck = Deck(
       layers=[scatter],
       initial_view_state=ViewState(latitude=37.8, longitude=-122.4, zoom=11),
       tooltip={"text": "Deck.GL"},
   )

   deck

Interacting with the Widget
---------------------------

Updating layer properties updates the rendered map after calling
:meth:`Deck.update`. This is useful for stateful UIs where the same layer
instance is mutated in-place. The example shows the refreshed serialized
payload.

.. jupyter-execute::

   deck2 = Deck(
       layers=[scatter],
       initial_view_state=ViewState(latitude=37.8, longitude=-122.4, zoom=11),
       tooltip={"text": "Deck.GL"},
   )
   deck2.layers[0].data[0]["radius"] = 200
   deck2.update()
   deck2

The :class:`~ipydeck.Layer`, :class:`~ipydeck.ViewState`, and
:class:`~ipydeck.Deck` API references contain additional options that match the
underlying `deck.gl <https://deck.gl/>`_ library.
