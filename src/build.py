import base64, pathlib, sys

here = pathlib.Path(__file__).parent
tpl = (here / "template.html").read_text(encoding="utf-8")

MAP = {
    "{{PRODUCT}}": ("assets/product.jpg", "image/jpeg"),
    "{{LOGO}}":    ("assets/logo.png",    "image/png"),
    "{{REL1}}":    ("assets/rel1.jpg",    "image/jpeg"),
    "{{REL2}}":    ("assets/rel2.jpg",    "image/jpeg"),
}

for token, (rel, mime) in MAP.items():
    p = here / rel
    if not p.exists():
        sys.exit("missing asset: " + rel)
    data = base64.b64encode(p.read_bytes()).decode("ascii")
    tpl = tpl.replace(token, "data:%s;base64,%s" % (mime, data))

left = [t for t in MAP if t in tpl]
if left:
    sys.exit("unreplaced tokens: %s" % left)

out = here / "index.html"
out.write_text(tpl, encoding="utf-8")
print("index.html: %.1f KB" % (out.stat().st_size / 1024))
