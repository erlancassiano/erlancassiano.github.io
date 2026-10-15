# erlancassiano.github.io

Static portfolio for **Erlan Cassiano**, Spacecraft Mechanical Design Engineer.

## Stack

Plain HTML + CSS + a little JS. Hosted on GitHub Pages (user site). `.nojekyll` is present. KaTeX is loaded from jsDelivr on case-study pages for math.

## Local preview

```bash
python3 -m http.server 8080 --directory .
# open http://localhost:8080/
```

## Regenerating case-study pages

```bash
python3 scripts/build_pages.py
```

## Featured items (`data-featured`)

Every list-type section on the site (work, education, certifications, projects, media, publications, skills, languages, calculations, gallery) supports a **featured** flag so the page can open focused and expand on demand.

- On each item set `data-featured="true"` or `data-featured="false"`.
- Put the list container on `data-featured-list` (and a stable `id` when practical).
- With JavaScript: only featured items show; a **See more** / **See less** button (`aria-expanded`) reveals the rest. The button is omitted when a list has no non-featured items.
- Without JavaScript, and in print: **all** items show (no collapsed state).

Projects also carry `"featured": true|false` in [`scripts/projects.json`](scripts/projects.json) for the same defaults (keep HTML `data-featured` in sync when flipping).

Initial defaults and flip checklist: [CONTENT_TODO.md](CONTENT_TODO.md#featured-flags).

## Content checklist

See [CONTENT_TODO.md](CONTENT_TODO.md) for images, prose, and notebooks Erlan still needs to supply.
