import { BitmapLayer, TileLayer } from "deck.gl";

export default class BitmapTileLayer extends TileLayer {
  static defaultProps = {
    ...TileLayer.defaultProps,
    // Default to a 256x256 image
    tileSize: 256,
    renderSubLayers: {
      type: "function",
      value: BitmapTileLayer._renderSubLayers,
    },
  };

  static _renderSubLayers(props) {
    console.log("renderSubLayers = BitmapLayer");
    const {
      bbox: { west, south, east, north },
    } = props.tile;

    return new BitmapLayer(props, {
      data: undefined,
      image: props.data,
      bounds: [west, south, east, north],
    });
  }
}
