# silexsounds.com

The SILEX website: one page (`index.html`) with tabs for Home, Live show, Services, Music, For brands and Contact. Hosted on GitHub Pages at silexsounds.com.

- `index.html` is the whole site (styles and scripts inside it).
- `silex.jpg` is the hero photo; `og.jpg` is the image shown when the link is shared.
- `stats.json` holds the Standard review count and host score. The workflow in `.github/workflows/standard-stats.yml` refreshes it from the public Standard host page every 3 hours.
- `CNAME` points GitHub Pages at silexsounds.com.
- `queue/` is the public page of the song request line (silexsounds.com/queue/), for the LIVE where viewers request songs in chat. It shows how many songs are waiting, what is playing, the line in order, and a box to find your own place. It reads a small snapshot that the SILEX Requests app keeps in an Upstash Redis database while the LIVE is on. `queue/config.json` holds that database's REST URL and its **read-only** token (safe to publish, it can only read). While those are blank, or when no LIVE is on, the page says the line is closed. Nothing links to it from the main page, and it asks search engines not to list it.
