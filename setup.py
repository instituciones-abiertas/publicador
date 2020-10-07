import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="publicador",
    version="0.0.1",
    author="José Luis Di Biase",
    author_email="josx@camba.coop",
    description="Publicador de archivos en diferentes plataformas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cambalab/publicador",
    packages=setuptools.find_packages(),
    install_requires=[
        'dropbox',
        'cd-drive'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    python_requires='>=3.6',
)
