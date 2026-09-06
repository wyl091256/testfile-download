"""Harmless skill dependency module for authorized sandbox audit."""


MARKER = "SKILL-DEP-VERIFY-20260906"


def add(a, b):
    return a + b


def main():
    print("SKILLDEP_CLI_OK", MARKER, add(20, 22))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
