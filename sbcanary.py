"""Harmless canary module for authorized sandbox audit (XYQ-SB-002 evidence)."""

MARKER = "USER-CONTROLLED-PKG-CANARY-20260906"


def add(a, b):
    return a + b
