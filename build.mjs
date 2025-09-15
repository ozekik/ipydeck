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

await esbuild.build({
  entryPoints: ["./src/widget.tsx"],
  bundle: true,
  minify: true,
  target: ["es2020"],
  // Cf. https://stackoverflow.com/questions/69088135/
  loader: { ".css": "text" },
  outdir,
  format: "esm",
  // Ref https://github.com/manzt/anywidget/issues/369#issuecomment-1792376003
  define: {
    "define.amd": "false",
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
