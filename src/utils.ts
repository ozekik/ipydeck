// https://stackoverflow.com/questions/29182244/convert-a-string-to-a-template-string
export function interpolate(template: string, params: any) {
  const names = Object.keys(params);
  const vals = Object.values(params);
  // console.log("names, vals", names, vals);
  // console.log("template", template);

  // Replace invalid characters for identifiers for with underscores in names to avoid errors in `new Function`
  names.map((name, i) => {
    names[i] = name
      .replace(/^[^a-zA-Z_$\p{L}]/u, "_")
      .replace(/[^\w$\p{L}\p{N}]/gu, "_");
  });

  let result = new Function(...names, `return \`${template}\`;`)(...vals);
  // console.log("result", result);

  // if result is not a string, return null
  if (typeof result !== "string") {
    return null;
  }

  // COMPAT: Replace `{name}` with values from params object
  result = result.replace(/\{([^}]+)\}/g, (_, key: string) => {
    return params?.[key] ?? "";
  });

  return result;
}
