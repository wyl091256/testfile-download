from setuptools import setup

setup(
    name="skilldep",
    version="0.0.3",
    description="Harmless skill dependency for canvas template testing",
    py_modules=["skilldep"],
    entry_points={"console_scripts": ["skilldep-run=skilldep:main"]},
)
