from setuptools import setup

setup(
    name="sbcanary",
    version="0.0.2",
    description="Harmless canary package for authorized sandbox audit",
    py_modules=["sbcanary"],
    entry_points={"console_scripts": ["sbcanary-run=sbcanary:main"]},
)
