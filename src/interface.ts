export interface ExtraLigature {
  glyphName: string;
  unicodes: [string];
}

export interface Path {
  color: string;
  paths: [InnerPath];
}

export interface InnerPath {
  $: {
    d: string;
    fill: string;
    stroke: string;
    "stroke-width": string | null;
  };
  "#name": "path";
}
