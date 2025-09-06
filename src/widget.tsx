import React, { useEffect, useState } from "react";

import { createRender, useModelState } from "@anywidget/react";

import Map, { AttributionControl } from "react-map-gl/maplibre";

import { BASEMAP } from "@deck.gl/carto";
import { _convertFunctions as convertFunctions } from "@deck.gl/json";
import { DeckGL } from "@deck.gl/react";
import {
  // Layer,
  ArcLayer,
  BitmapLayer,
  ColumnLayer,
  ContourLayer,
  GeoJsonLayer,
  GeohashLayer,
  GridCellLayer,
  GridLayer,
  H3ClusterLayer,
  H3HexagonLayer,
  HeatmapLayer,
  HexagonLayer,
  IconLayer,
  // _WMSLayer as WMSLayer,
  LineLayer,
  MVTLayer,
  PathLayer,
  PointCloudLayer,
  PolygonLayer,
  QuadkeyLayer,
  S2Layer,
  ScatterplotLayer,
  ScreenGridLayer,
  SimpleMeshLayer,
  SolidPolygonLayer,
  TerrainLayer,
  TextLayer,
  Tile3DLayer,
  TileLayer,
  TripsLayer,
} from "deck.gl";

import root from "react-shadow";

import BitmapTileLayer from "./layers/BitmapTileLayer";
import { interpolate } from "./utils";

import maplibreCss from "maplibre-gl/dist/maplibre-gl.css";

const INITIAL_VIEW_STATE = {
  longitude: 0,
  latitude: 0,
  zoom: 1,
};

const LAYER_TYPES: { [key: string]: any } = {
  ArcLayer,
  BitmapLayer,
  BitmapTileLayer,
  ColumnLayer,
  ContourLayer,
  GeoJsonLayer,
  GridCellLayer,
  GridLayer,
  H3ClusterLayer,
  H3HexagonLayer,
  HeatmapLayer,
  HexagonLayer,
  IconLayer,
  LineLayer,
  MVTLayer,
  PathLayer,
  PointCloudLayer,
  PolygonLayer,
  GeohashLayer,
  QuadkeyLayer,
  S2Layer,
  ScatterplotLayer,
  ScreenGridLayer,
  SimpleMeshLayer,
  SolidPolygonLayer,
  TerrainLayer,
  TextLayer,
  TileLayer,
  Tile3DLayer,
  TripsLayer,
};

function deserializeLayer(serializedLayer: any) {
  const { type, ..._args } = serializedLayer;

  let args = Object.entries(_args).reduce((acc, [key, value]) => {
    console.log(key, value);
    return value === null ? acc : { ...acc, [key]: value };
  }, {});

  args = convertFunctions(args, {});

  console.log("type", type, "args", args);

  // TODO: Custom layer support
  if (type in LAYER_TYPES) {
    // TODO: Use CSVLoader for csv data
    return new LAYER_TYPES[type](args);
  }
}

export const render = createRender(() => {
  const [initialViewState] = useModelState<any>("_initial_view_state");
  const [_layers] = useModelState<any[]>("_layers");
  const [width] = useModelState<number | string>("width");
  const [height] = useModelState<number | string>("height");
  const [map_style] = useModelState<string>("map_style");
  const [tooltip] = useModelState<
    { html: string; style?: string } | null | undefined
  >("_tooltip");

  const [layers, updateLayers] = useState<any[]>([]);

  const [_click, setClick] = useModelState<any>("click");

  // useEffect(() => {
  //   console.log("click", _click);
  // }, [_click]);

  useEffect(() => {
    const deserialized = _layers.map((layer) => deserializeLayer(layer));
    // console.log("deserialized", deserialized);

    deserialized.map((layer: any) => {
      if (layer.props.onClick) {
        // NOTE: layer.props is read-only
        layer.onClick = (info: any, event: any) => {
          // const timestamp = new Date().toISOString();
          // TODO: Add layer information
          setClick(info.object);
        };
      }
    });

    updateLayers(deserialized);
  }, [_layers]);

  return (
    <root.div
      style={{
        width: Number.isFinite(width) ? `${width}px` : width,
        height: Number.isFinite(height) ? `${height}px` : height,
        position: "relative",
      }}
    >
      <DeckGL
        initialViewState={
          ["longitude", "latitude", "zoom"].every((key) =>
            Object.keys(initialViewState).includes(key),
          )
            ? initialViewState
            : INITIAL_VIEW_STATE
        }
        getCursor={() => "default"} // TODO: Make this configurable
        controller={true}
        layers={layers}
        style={{ width: "100%", height: "100%" }}
        getTooltip={({ object }) => {
          if (!tooltip || !object) return null;
          return {
            html: interpolate(tooltip.html, {
              ...(object.properties || {}),
              ...object,
            }),
            style: tooltip.style,
          };
        }}
      >
        <Map
          reuseMaps
          mapStyle={map_style || BASEMAP.POSITRON}
          attributionControl={false}
        >
          <AttributionControl compact={true} />
        </Map>
      </DeckGL>
      <style>{maplibreCss}</style>
    </root.div>
  );
});
