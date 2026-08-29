import base64, pathlib, sys

here = pathlib.Path(__file__).parent

MAP = {
    "{{PRODUCT}}": ("assets/product.jpg", "image/jpeg"),
    "{{LOGO}}":    ("assets/logo.png",    "image/png"),
    "{{REL1}}":    ("assets/rel1.jpg",    "image/jpeg"),
    "{{REL2}}":    ("assets/rel2.jpg",    "image/jpeg"),
}

# template -> output. v2 is the working surface; index.html is the approved one.
BUILDS = [
    ("template.html",    "index.html"),
    ("template-v2.html", "v2/index.html"),
]

data_uris = {}
for token, (rel, mime) in MAP.items():
    p = here / rel
    if not p.exists():
        sys.exit("missing asset: " + rel)
    data_uris[token] = "data:%s;base64,%s" % (mime, base64.b64encode(p.read_bytes()).decode("ascii"))

for src, dst in BUILDS:
    sp = here / src
    if not sp.exists():
        continue
    html = sp.read_text(encoding="utf-8")
    for token, uri in data_uris.items():
        html = html.replace(token, uri)
    left = [t for t in MAP if t in html]
    if left:
        sys.exit("unreplaced tokens in %s: %s" % (src, left))
    out = here / dst
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("%-16s -> %-16s %.1f KB" % (src, dst, out.stat().st_size / 1024))
