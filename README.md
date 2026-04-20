# CI Doctor Case: bugsinpy_fastapi_1_multiflag_overflow_plus

Further-expanded BugsInPy-derived FastAPI multiflag gauntlet with an extra overflow layer of late-order wrapper modules that still mishandle alias/default/none propagation after the current deterministic repair bundle fixes the original visible surface.

## Run locally

```bash
python -m pytest -q -x tests
```

This repository is intentionally failing on `main` so CI Doctor can propose a repair and open a PR.
