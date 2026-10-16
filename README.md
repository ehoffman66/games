# Games

Each game lives in its own folder and is served by GitHub Pages at `https://ehoffman66.github.io/games/<folder>/`.

To add a game: put its files in a new folder with an `index.html`, add a card for it in the top-level `index.html`, and push.

- `killhouse/` — Three.js room-clearing shooter (single `index.html` plus the models it loads from `models/`). Home-screen icon and manifest live next to it; rebuild `index.html` from the game source with `python3 tools/wrap_killhouse.py <source.html>`.
- `breakaway-checkers/` — Three.js AHL hockey shootout with seasons, online play and a recorded announcer (single `index.html` plus the rigs, textures and announcer calls it loads from `models/`; `tools/announcer` rebuilds the calls).
- `plaza-midwood-runner/` — Canvas endless runner down Central Ave, Charlotte (single self-contained `index.html`; the friends leaderboard only works inside Claude and hides itself here).
- `plaza-midwood-quest-3d/` — Three.js first-person open-world quest game in Plaza Midwood (single `index.html`, three.js loaded from jsDelivr).
- `paw-quest/` — Three.js kids' platformer (`index.html` plus `world3d.js`, the bundled three.js world; `kid1.js`/`kid2.js`/`dog3d.js`/`bakery.js`, models as base64 JS; and textures in `tex/`). Built and published as a Claude artifact; copy the files here to update.
