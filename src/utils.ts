// https://stackoverflow.com/questions/29182244/convert-a-string-to-a-template-string
export function interpolate(template: string, params: any) {
  const names = Object.keys(params);
  const vals = Object.values(params);
  // console.log("names, vals", names, vals);

  // Replace invalid characters for identifiers for with underscores in names to avoid errors in `new Function`
  names.map((name, i) => {
    names[i] = name
      .replace(/^[^a-zA-Z_$\p{L}]/u, "_")
      .replace(/[^\w$\p{L}\p{N}]/gu, "_");
  });

  const result = new Function(...names, `return \`${template}\`;`)(...vals);
  // console.log("result", result);

  return result;
}
