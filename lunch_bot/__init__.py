# routes.py depends on main.py and thus must be loaded after it.
from __future__ import annotations  # isort:skip

from .api import error_handlers, routes  # isort:skip
from .api.main import app  # isort:skip

__all__ = ["app", "routes", "error_handlers"]
