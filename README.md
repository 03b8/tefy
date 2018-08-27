[![Build Status](https://travis-ci.org/ghineaion/TEfy.svg?branch=master)](https://travis-ci.org/ghineaion/TEfy)
# TEfy
TEfy was born out of the need to streamline the conversion of *.doc, 
*.docx and *.odt documents into TEI XML when using Python scripts.
It's a very basic wrapper around the [OxGarage](https://github.com/TEIC/oxgarage) API at 
[oxgarage.tei-c.org/ege-webservice](http://oxgarage.tei-c.org) and covers a small subset of conversions, namely
from doc, docx and odt to TEI XML. The conversion result is output
as an [lxml](https://github.com/lxml/lxml) etree Element.
## Usage
You can install TEfy from [PyPI](https://pypi.org/project/TEfy/)
(```$ pip install TEfy```) and convert let's say an ODT document 
like this:

```python
from TEfy import OxGaWrap
example_file = OxGaWrap('path/to/example.odt')
example_file.convert_to_tei()
etree_object = example_file.get_et_output()
```

