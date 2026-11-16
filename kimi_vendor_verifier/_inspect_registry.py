"""inspect_ai entry point: registers the ``kimi`` model API.

kimi_model and its siblings import each other as top-level modules (``from utils import``),
so the KVV tree goes on sys.path and kimi_model is imported under that same top-level
name. eval.py imports it the same way, so the registration happens once either way.
"""

import sys

from . import ROOT

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import kimi_model  # noqa: E402,F401  (registers the "kimi" model API)
