from logging import basicConfig

import ipydeck as pdk

basicConfig(level="DEBUG")

def test_bitmap_layer():
    layer = pdk.Layer(
        "BitmapLayer",
        bounds=[-122.5190, 37.7045, -122.355, 37.829],
        image="https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/sf-districts.png",
    )
