GeoJsonLayer
============

The `deck.gl GeoJsonLayer <https://deck.gl/docs/api-reference/layers/geojson-layer>`_ is best suited
for rendering vector data such as polygons, lines, and points. You can pass a
Python ``dict`` representing GeoJSON, a filename, or any other serializable
object that deck.gl understands.

The example below renders a short line segment that highlights the Golden Gate
Bridge. Styling options such as ``get_line_color`` and
``line_width_min_pixels`` map directly to deck.gl and are forwarded to the front
end when the widget is rendered.

.. jupyter-execute::

   from ipydeck import Deck, Layer, ViewState

   bridge = {
       "type": "FeatureCollection",
       "features": [
           {
               "type": "Feature",
               "properties": {"name": "Golden Gate Bridge"},
               "geometry": {
                   "type": "LineString",
                   "coordinates": [
                       [-122.483696, 37.832275],
                       [-122.478977, 37.819928],
                   ],
               },
           }
       ],
   }

   geojson_layer = Layer(
    type="GeoJsonLayer",
       data=bridge,
       get_line_color=[255, 99, 71],
       line_width_min_pixels=3,
       pickable=True,
   )

   Deck(
       layers=[geojson_layer],
       initial_view_state=ViewState(latitude=37.8267, longitude=-122.4805, zoom=12.5),
       tooltip={"text": "{name}"},
   )

For larger datasets you can point ``data`` at a remote GeoJSON URL or any
mapping library that yields compatible features.
