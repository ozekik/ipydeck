import ipydeck as pdk


class DummyGeo:
    def __init__(self):
        self.__geo_interface__ = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {"name": "Test Feature", "value": 3},
                    "geometry": {
                        "type": "Point",
                        "coordinates": [12.34, 56.78],
                    },
                }
            ],
        }


def test_layer_serializes_geo_interface_records():
    layer = pdk.Layer("GeoJsonLayer", data=DummyGeo())

    serialized = layer.serialize()

    assert serialized["type"] == "GeoJsonLayer"
    assert serialized["data"][0]["name"] == "Test Feature"
    assert serialized["data"][0]["value"] == 3
    assert serialized["data"][0]["geometry"]["type"] == "Point"
    assert serialized["data"][0]["geometry"]["coordinates"] == [12.34, 56.78]


def test_layer_serializes_additional_kwargs_to_camel_case():
    layer = pdk.Layer(
        "GeoJsonLayer",
        data=[{"id": 1}],
        get_line_color=[255, 0, 0],
        on_click=True,
    )

    serialized = layer.serialize()

    assert "getLineColor" in serialized
    assert serialized["getLineColor"] == [255, 0, 0]
    assert serialized["onClick"] is True
