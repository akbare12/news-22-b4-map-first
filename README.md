# The World Today — 22 November 2026

[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/akbare12/news-22-b4-map-first/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/akbare12/news-22-b4-map-first/reward.svg)](https://make.fun/bounty/news-image-20261122)

One image summing up the world's news of Sunday 22 November 2026 — a map-first
front page: a big world map with 16 numbered pins, three heroes (Hormuz tankers
hit mines, COP31 collapses with no deal, Democrats win 258 House seats), 31
stories in all, verification legend, numbers strip, UTC timeline, NOT YET strip
and a date-check footer.

`main.py` (Python 3.13, stdlib only) copies `entry.png` to the output
directory and verifies the copy byte for byte (size + sha256).

## How it was made

The image was drawn from scratch with PIL from news researched for 22 Nov 2026
(cutoff: late wires to 23:00 UTC). Every headline was checked against at least
two sources; items first reported on other dates were excluded and named in the
date-check footer (El Chapo Isidro captured 20 Nov, Shenzhen Trump–Xi–Putin
summit 19–20 Nov, Wall St rout 20 Nov, FBI NCIC hack 21 Nov, India poverty
estimate 23 Nov).

## License

MIT — see [LICENSE](LICENSE).
