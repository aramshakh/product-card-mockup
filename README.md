# Product card mockup

Static mockup of a Shopify product page, rebuilt with a new content structure
while keeping the original visual design untouched.

- `index.html` — the mockup. Single self-contained file, all images inlined as data URIs.
- `src/template.html` — source template with `{{IMAGE}}` placeholders.
- `src/build.py` — inlines `src/assets/*` into `index.html`.
- `src/assets/` — original images.

Rebuild:

    python3 src/build.py

The page carries `noindex, nofollow`.
