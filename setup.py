from setuptools import setup

setup(
    name="mygit",
    version="0.1",
    py_modules=["cli"],
    entry_points={
        "console_scripts": [
            "mygit=cli:main"
        ]
    }
)