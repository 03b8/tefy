import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

    setuptools.setup(
            name="TEfy",
            version="0.1.1",
            author="Theo Costea",
            author_email="theo.costea@gmail.com",
            description="A very basic wrapper for conversions from doc, docx and odt to TEI XML",
            long_description=long_description,
            long_description_content_type="text/markdown",
            url="https://github.com/ghineaion/tefy",
            packages=setuptools.find_packages(),
            classifiers=[
                "Programming Language :: Python :: 3.5",
                "License :: OSI Approved :: MIT License",
            ],
    )
