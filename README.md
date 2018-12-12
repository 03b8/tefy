[![Build Status](https://travis-ci.org/03b8/TEfy.svg?branch=master)](https://travis-ci.org/03b8/TEfy)
# TEfy
TEfy was born out of the need to streamline the conversion of *.doc, 
*.docx and *.odt documents into TEI XML when using Python scripts.
It's a very basic wrapper around the [OxGarage](https://github.com/TEIC/oxgarage) API at 
[oxgarage.tei-c.org/ege-webservice](http://oxgarage.tei-c.org) and covers a small subset of conversions, namely
from doc, docx and odt to TEI XML. The conversion result is output
as an lxml etree Element.
