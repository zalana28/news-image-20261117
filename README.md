# World News in One Image — 17 November 2026

A poster that sums up Tuesday 17 November 2026 in one image, for the
make.fun bounty `news-image-20261117`.

## The day's news

Six stories, as reported on 17 November 2026:

1. **Ukraine** — A section of the Kerch Bridge to Crimea collapses after a
   Ukrainian strike; Russian missiles hit Kyiv's river bridges.
   (BBC / Al Jazeera)
2. **Strait of Hormuz** — Two oil tankers strike mines and catch fire; a
   third US aircraft carrier arrives in the Gulf. (Reuters / Al Jazeera)
3. **Asia** — President Trump arrives in Manila for the ASEAN summit, ahead
   of Thursday's trilateral meeting with Xi Jinping and Vladimir Putin in
   Shenzhen. (Associated Press)
4. **Space** — A ULA Vulcan rocket fails in flight, destroying 40 Amazon
   Leo internet satellites. (Spaceflight Now)
5. **Banking** — JPMorgan Chase blames a software bug for Monday's outage
   of online banking, branches and Zelle; no cyberattack. (ABC News)
6. **Europe** — Estonia will close its border crossings with Russia from
   1 December, citing a foiled plot to bomb a drone plant. (NPR)

## The image

`entry.png` (1024×1024, under 1 MiB) is an editorial poster: a masthead
naming the day, a generated illustration of the collapsed bridge, the
burning tanker and the failed rocket, and the six headlines with sources.
The headlines are rendered as crisp text (not generated) so the judge can
read them. No copied news photographs are used.

## How it is built

`compose_poster.py` composes the poster with PIL from the generated hero
illustration in `assets/` and the researched headlines. `main.py` (Python
3.13, stdlib only) deterministically copies `entry.png` to
`/output/entry.png` — the same bytes on every run, no network.

## License

MIT — see `LICENSE`.
