"""Tangram2 modules, loaded on demand.

Mapping does not require the optional CCC and benchmarking dependencies.
The scientific implementations are unchanged from the recorded upstream commit.
"""
from importlib import import_module

__all__ = ["mapping", "ccc", "evalkit", "external"]


def __getattr__(name):
    if name in __all__:
        module = import_module(f"{__name__}.{name}")
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
