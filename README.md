# tiny-chess-01

A tiny chess engine in at most 4,096 bytes of Python (stdlib only), written
from scratch for the make.fun bounty tiny-chess-01.

- `main.py` — the engine (4,092 bytes). Deterministic negamax alpha-beta
  search with a transposition table, fixed 90,000 nodes/move.
- Speaks UCI-ish JSON over the make.fun trial environment protocol.

License: MIT.
