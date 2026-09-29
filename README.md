# Letter Bluff — website

The public site for the store listings: `https://letterbluff.app`.
Same shape as letterhex.app (home, how-to-play, support, privacy,
account deletion, invite landing, app-ads.txt), rebuilt in Letter
Bluff's Notebook look. Plain static files — no build step.

Everything under `public/` is the site. Nothing outside it is served.

## Pages

| URL | File | Used for |
| --- | --- | --- |
| `/` | `public/index.html` | Store listing "Website" / Apple "Marketing URL" |
| `/help` | `public/help.html` | How to play |
| `/support` | `public/support.html` | Store listing "Support URL" |
| `/privacy` | `public/privacy.html` | Store listing "Privacy policy" |
| `/delete-account/` | `public/delete-account/index.html` | Play Console ▸ Data safety ▸ account deletion URL |
| `/i/?c=BLF-XXXX` | `public/i/index.html` | Invite landing (shows the friend's code) |
| `/app-ads.txt` | `public/app-ads.txt` | AdMob verifies it against the listing's website |
| any miss | `public/404.html` | — |

Contact everywhere: `support@letterbluff.app`.

## Preview locally

    python preview.py

then open http://localhost:8787. The script serves `public/` with the
host's clean URLs (`/help` finds `help.html`). Opening the files
straight from disk won't work — paths are root-absolute.

## Deploy (Cloudflare, like letterhex-site)

`wrangler.jsonc` describes a static-assets Worker that serves
`public/`. Letter Hex serves its repo root; this repo serves a
subfolder so the README and tooling are never published.

1. Add `letterbluff.app` to Cloudflare (DNS on Cloudflare).
2. Workers & Pages ▸ Create ▸ import this repository. No build
   command; the deploy command is `npx wrangler deploy`. Pushes to
   `main` deploy from then on.
3. The Worker ▸ Settings ▸ Domains & Routes ▸ add the custom domain
   `letterbluff.app`.
4. Email ▸ Email Routing: route `support@letterbluff.app` to the
   studio inbox.
5. Check every row of the table above on the live domain.

## Before going live — check these

The pages describe the game as it will ship. These lines depend on
work that was still open when the site was written (2026-09-29):

- **Sign-in** (support: "How do I keep my progress on a new device?",
  privacy: "If you sign in"). Needs the platform-auth pass. If launch
  ships without it, cut the support answer.
- **`app-ads.txt`** is a copy of letterhex.app's, on the assumption
  that both games share one AdMob account. Confirm the publisher id in
  AdMob ▸ Apps ▸ app-ads.txt.
- **Privacy policy** — written to match what the build does (AdMob
  ads, Supabase backend, store billing). It differs from Letter Hex's
  because this game shows ads. Read it as a draft: it has not had legal
  review. Update it, and the effective date, when any of these land:
  EEA consent (UMP), push notifications / Firebase, analytics.
- **Play Console ▸ Data safety** must agree with the policy: device
  or other IDs (advertising, by Google), app activity and purchase
  history (ours), email only if signed in.
- **Store buttons** both read "coming soon" on the home and invite
  pages. Swap in the real links as each listing goes live — Play:
  `https://play.google.com/store/apps/details?id=app.letterbluff.game`
  (as an `<a class="btn">`, not the ghost `<span>`).
- **Social preview image** — none yet (`og:image`); add one from the
  store assets.

## Editing

The header and footer are repeated in each page (no templating); a
change to the nav means touching every file in `public/`. Colours,
type and components live in `public/assets/site.css`. Numbers that
can be retuned from the game's server (coin amounts, prices, reward
sizes) are deliberately left out of the copy.

The icons are the game's own set (the game repo's `assets/icons/`),
recoloured to ink. Urbanist is self-hosted under the SIL Open Font
License (`public/assets/fonts/OFL.txt`).
