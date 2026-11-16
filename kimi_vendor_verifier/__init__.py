"""Kimi Vendor Verifier as an installable package.

KVV is a tree of scripts and pytest suites, not a library. The wheel copies that tree,
unchanged, into this package directory; ``ROOT`` is where it lives, so a caller can run
the suites from there:

    pytest <ROOT>/tests/params ...
    python <ROOT>/eval.py ocrbench ...
    python <ROOT>/beam/beam_generate.py ...

In a checkout (or an editable install) the tree is the repository root, one level up.
"""

from __future__ import annotations

from pathlib import Path

_HERE = Path(__file__).resolve().parent


def _root() -> Path:
    # Installed wheel: the tree sits next to this file. Checkout: one directory up.
    for candidate in (_HERE, _HERE.parent):
        if (candidate / "eval.py").is_file() and (candidate / "tests").is_dir():
            return candidate
    raise ImportError(f"kimi_vendor_verifier: no KVV tree at {_HERE} or {_HERE.parent}")


ROOT: Path = _root()

__all__ = ["ROOT"]
