import { BitmapLayer, TileLayer } from "deck.gl";

type BitmapTileSubLayerProps = {
  tile: {
    bbox: {
      west: number;
      south: number;
      east: number;
      north: number;
    };
  };
  [key: string]: unknown;
};

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

  static _renderSubLayers(props: BitmapTileSubLayerProps) {
    console.log("renderSubLayers = BitmapLayer");
    const {
      bbox: { west, south, east, north },
    } = props.tile;

    return new BitmapLayer(props as Record<string, unknown>, {
      data: undefined,
      image: props.data as string | undefined,
      bounds: [west, south, east, north],
    });
  }
}
