import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

    setuptools.setup(
            name="TEfy",
            version="0.1.3",
            author="Theo Costea",
            author_email="theo.costea@gmail.com",
            description="A very basic wrapper for conversions from doc, docx and odt to TEI XML",
            long_description=long_description,
            long_description_content_type="text/markdown",
            url="https://github.com/03b8/tefy",
            packages=setuptools.find_packages(),
            classifiers=[
                "Programming Language :: Python :: 3.6",
                "License :: OSI Approved :: MIT License",
            ],
    )
