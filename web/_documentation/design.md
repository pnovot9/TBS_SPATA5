# Design system

The site uses the "Atlas" design: a calm encyclopedia look chosen from four
prototypes (see `web/designs/index.html` for the other three). Serif
display headings, sans body text, a dark slate left menu in both themes,
and a light or dark content area.

## Brand colors

Taken from zazracnedeti.cz, the website of the SPATA5 CZ parents
association:

- Orange `#f57f17` is the site accent (links, active states, highlights).
  On light backgrounds it darkens to `#e56f0b` for contrast.
- Purple `#6a1b9a` is the secondary accent (blockquotes, selected marks).
- Slate blue-gray `#373f51` family for text and the sidebar panel.

## Tokens

Every color, font, and shadow is a CSS custom property on `:root` in
`web/styles.css`. Dark mode redefines the same tokens under
`[data-theme="dark"]`. Rules reference `var(--token)` only. Adding a raw
hex value mid-stylesheet is a bug.

Sidebar tokens (`--sidebar-*`) are separate because the sidebar stays dark
in both themes.

## Typography

- Display: Source Serif 4 (headings, brand). Fallback Georgia.
- Body: Inter. Fallback system sans.
- Both load from Google Fonts with real fallback stacks.

## Dark mode

Three states. Default follows `prefers-color-scheme`. The slider in the
sidebar overrides it and stores the choice in `localStorage`
(`spata5-theme`, wrapped in try/catch). `app.js` sets `data-theme="dark"`
on `<html>` or removes it.

## Motion

Personality is Premium/Corporate: 150 to 250 ms, easing
`cubic-bezier(.2,0,0,1)`, no overshoot. Menu groups reveal with a small
fade and 4 px rise. The theme knob slides in 200 ms. Everything is wrapped
by a `prefers-reduced-motion` block that disables transitions and
animations.

## Accessibility floor

Visible `:focus-visible` outline, semantic `<details>` menu, the theme
toggle is a `role="switch"` button with `aria-checked` and a Czech
`aria-label`, tables scroll inside `.table-wrap` instead of overflowing the
page, and the layout works down to mobile widths (sidebar stacks on top
under 860 px).
