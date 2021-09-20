import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="inhouse_models",
    version="0.0.3",
    author='Akash Nagaraj',
    author_email='akash_n@brown.edu',
    description='Package to import in-house models from the Serre Lab at Brown University.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/serre-lab/inhouse_models',
    project_urls={
        "Documentation": "https://github.com/serre-lab/inhouse_models/docs",
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