tefy
====

|Build Status| |PyPI version| 

``tefy`` was born out of the need to streamline the conversion of doc,
docx and odt documents into TEI XML when using Python scripts. It's a
very basic wrapper around the OxGarage_
API at https://oxgarage.tei-c.org/ege-webservice/ and
covers a small subset of conversions, namely from doc, docx and odt to TEI
XML. The conversion result is output as an lxml_ etree Element. 

.. _OxGarage: https://github.com/TEIC/oxgarage
.. _lxml: https://github.com/lxml/lxml

Usage 
-----
You can install `tefy` with pip (``$ pip install tefy``) 
and convert let's say an ODT document like this:

.. code:: python

    from tefy import OxGaWrap
    doc = OxGaWrap('path/to/example.odt')
    tei = doc.tei_xml

.. |Build Status| image:: https://travis-ci.org/03b8/tefy.svg?branch=master
   :target: https://travis-ci.org/03b8/tefy
.. |PyPI version| image:: https://badge.fury.io/py/tefy.svg
   :target: https://badge.fury.io/py/tefy
