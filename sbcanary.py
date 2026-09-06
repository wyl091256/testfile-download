"""Harmless canary module for authorized sandbox audit (XYQ-SB-002 evidence)."""

MARKER = "USER-CONTROLLED-PKG-CANARY-20260906"


def add(a, b):
    return a + b


def main():
    print("CANARY_CLI_OK", MARKER, add(20, 22))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
