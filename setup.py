import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wordler-eirkkr",
    version="0.0.1",
    author="Eric Parkin",
    author_email="eric.parkin@protonmail.com",
    description="Helps solve wordle puzzles.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eirkkr/wordler",
    project_urls={
        "Bug Tracker": "https://github.com/eirkkr/wordler/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)