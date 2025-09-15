import ipydeck as pdk


def build_point_layer(identifier):
    return pdk.Layer(
        "ScatterplotLayer",
        data=[{"position": [-122.4, 37.8], "size": 100}],
        id=identifier,
    )


def test_deck_initializes_layers_and_map_style_alias():
    layer = build_point_layer("start")

    deck = pdk.Deck(layers=[layer], map_style="light")

    assert deck.map_style == pdk.DefaultBaseMap.short_names["light"]
    assert deck._layers[0]["type"] == "ScatterplotLayer"
    assert deck._layers[0]["id"] == "start"


def test_deck_update_synchronizes_serialized_layers():
    initial_layer = build_point_layer("initial")
    updated_layer = build_point_layer("updated")

    deck = pdk.Deck(layers=[initial_layer])

    deck.layers = [updated_layer]
    deck.update()

    assert deck._layers[0]["id"] == "updated"
    assert deck._layers[0]["type"] == "ScatterplotLayer"
