// Derived from https://github.com/developmentseed/lonboard/blob/main/build.mjs (MIT)
// build.js
import esbuild from "esbuild";

esbuild.build({
  entryPoints: ["./src/widget.tsx"],
  bundle: true,
  minify: true,
  target: ["es2020"],
  outdir: "ipydeck/static/",
  format: "esm",
  // Ref https://github.com/manzt/anywidget/issues/369#issuecomment-1792376003
  define: {
    "define.amd": "false",
  },
  // Code splitting didn't work initially because it tried to load from a local
  // relative path ./chunk.js
  // splitting: true,
});
