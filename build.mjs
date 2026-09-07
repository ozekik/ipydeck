// Derived from https://github.com/developmentseed/lonboard/blob/main/build.mjs (MIT)
// build.js
import esbuild from "esbuild";
import { mkdir } from "fs/promises";
import { dirname, join } from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const outdir = join(__dirname, "ipydeck/static");

await mkdir(outdir, { recursive: true });

// Bundle the worker first
const workerBuild = await esbuild.build({
  entryPoints: ["node_modules/maplibre-gl/dist/maplibre-gl-worker.mjs"],
  bundle: true,
  platform: "browser",

  // IIFE means we can use it as a normal classic Worker
  format: "iife",

  write: false,
  minify: true,
});

const workerSource = workerBuild.outputFiles[0].text;

await esbuild.build({
  entryPoints: ["./src/widget.tsx"],
  bundle: true,
  minify: true,
  target: ["es2022"],
  // Cf. https://stackoverflow.com/questions/69088135/
  loader: { ".css": "text" },
  outdir,
  format: "esm",
  // Ref https://github.com/manzt/anywidget/issues/369#issuecomment-1792376003
  define: {
    "define.amd": "false",
    __WORKER_SOURCE__: JSON.stringify(workerSource),
  },
  // Code splitting didn't work initially because it tried to load from a local
  // relative path ./chunk.js
  // splitting: true,
});

await esbuild.build({
  entryPoints: ["./src/widget.css"],
  bundle: true,
  minify: true,
  outfile: join(outdir, "widget.css"),
});
