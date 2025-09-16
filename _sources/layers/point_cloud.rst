PointCloudLayer
===============

The `deck.gl PointCloudLayer <https://deck.gl/docs/api-reference/layers/point-cloud-layer>`_
plots 3D point clouds with per-point colors and normals. Use it for lidar or
photogrammetry datasets.

.. jupyter-execute::

   from ipydeck import Deck, Layer, ViewState

   lidar = Layer(
       type="PointCloudLayer",
       data=[
           {"position": [-122.4, 37.8, 12], "color": [200, 92, 173]},
           {"position": [-122.401, 37.799, 18], "color": [80, 176, 230]},
           {"position": [-122.402, 37.797, 9], "color": [245, 207, 66]},
       ],
       get_position="@@=position",
       get_color="@@=color",
       point_size=4,
   )

   Deck(
       layers=[lidar],
       initial_view_state=ViewState(latitude=37.799, longitude=-122.401, zoom=15, pitch=60),
   )

Provide normals through ``get_normal`` to enable eye-dome lighting on dense
clouds.
