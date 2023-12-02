# ipydeck

`ipydeck` is yet another Jupyter widget for [deck.gl](https://deck.gl/), built on [anywidget](https://github.com/manzt/anywidget/).

## Installation

```sh
pip install ipydeck
```

## Usage

```py
from ipydeck import Deck, Layer, ViewState

layer = Layer(
    "ScatterplotLayer",
    data=[{"position": [0, 0], "color": [255, 0, 0]}],
    get_position="position",
    get_fill_color="color",
    get_radius=1000,
)

view_state = ViewState(latitude=0, longitude=0, zoom=1)

deck = Deck(layers=[layer], initial_view_state=view_state)

deck
``````

## Alternatives

- [pydeck](https://deckgl.readthedocs.io/)
- [lonboard](https://github.com/developmentseed/lonboard/)

## License

MIT
