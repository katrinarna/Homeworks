from setuptools import setup, find_packages

setup(
    name="asteroids",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["requests", "pandas"],
    entry_points={
        "console_scripts": [
            "asteroids=asteroids.cli:main",
        ],
    },
)
