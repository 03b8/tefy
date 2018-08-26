from TEfy import OxGaWrap


def make_req(srcf):
    """
    Makes conversion request and returns HTTP status code
    :param srcf: source format
    :return: HTTP status code
    """
    oxobj = OxGaWrap('tests/in/test.{}'.format(srcf))
    oxobj.convert_to_tei()
    return oxobj.response.status_code


def get_tag_list(frmt):
    """
    Gets a list of tags from the XML conversion output of a specific document.
    :param frmt: format/extension of the input document (document must be present in the tests/in folder)
    :return: list of element tags
    """
    oxobj = OxGaWrap('tests/in/test.{}'.format(frmt))
    oxobj.convert_to_tei()
    tree = oxobj.get_et_output()
    elems = [el.tag for el in tree.xpath('//*')]
    return elems


# Test conversion requests from all source file formats to all target formats by asserting HTTP 200 status codes

def test_doc2xml():
    assert make_req('doc') == 200


def test_docx2xml():
    assert make_req('docx') == 200


def test_odt2xml():
    assert make_req('odt') == 200


# Test TEI XML output for each format by comparing a list of all element tags in document with a list of expected tags

def test_doc_output():
    elems = get_tag_list('doc')
    expected_elems = ['{http://www.tei-c.org/ns/1.0}TEI',          '{http://www.tei-c.org/ns/1.0}teiHeader',
                      '{http://www.tei-c.org/ns/1.0}fileDesc',     '{http://www.tei-c.org/ns/1.0}titleStmt',
                      '{http://www.tei-c.org/ns/1.0}title',        '{http://www.tei-c.org/ns/1.0}author',
                      '{http://www.tei-c.org/ns/1.0}editionStmt',  '{http://www.tei-c.org/ns/1.0}edition',
                      '{http://www.tei-c.org/ns/1.0}date',         '{http://www.tei-c.org/ns/1.0}publicationStmt',
                      '{http://www.tei-c.org/ns/1.0}p',            '{http://www.tei-c.org/ns/1.0}sourceDesc',
                      '{http://www.tei-c.org/ns/1.0}p',            '{http://www.tei-c.org/ns/1.0}revisionDesc',
                      '{http://www.tei-c.org/ns/1.0}listChange',   '{http://www.tei-c.org/ns/1.0}change',
                      '{http://www.tei-c.org/ns/1.0}name',         '{http://www.tei-c.org/ns/1.0}date',
                      '{http://www.tei-c.org/ns/1.0}text',         '{http://www.tei-c.org/ns/1.0}body',
                      '{http://www.tei-c.org/ns/1.0}div',          '{http://www.tei-c.org/ns/1.0}head',
                      '{http://www.tei-c.org/ns/1.0}p']

    assert elems == expected_elems


def test_docx_output():
    elems = get_tag_list('docx')
    expected_elems = ['{http://www.tei-c.org/ns/1.0}TEI',          '{http://www.tei-c.org/ns/1.0}teiHeader',
                      '{http://www.tei-c.org/ns/1.0}fileDesc',     '{http://www.tei-c.org/ns/1.0}titleStmt',
                      '{http://www.tei-c.org/ns/1.0}title',        '{http://www.tei-c.org/ns/1.0}author',
                      '{http://www.tei-c.org/ns/1.0}editionStmt',  '{http://www.tei-c.org/ns/1.0}edition',
                      '{http://www.tei-c.org/ns/1.0}date',         '{http://www.tei-c.org/ns/1.0}publicationStmt',
                      '{http://www.tei-c.org/ns/1.0}p',            '{http://www.tei-c.org/ns/1.0}sourceDesc',
                      '{http://www.tei-c.org/ns/1.0}p',            '{http://www.tei-c.org/ns/1.0}encodingDesc',
                      '{http://www.tei-c.org/ns/1.0}appInfo',      '{http://www.tei-c.org/ns/1.0}application',
                      '{http://www.tei-c.org/ns/1.0}label',        '{http://www.tei-c.org/ns/1.0}revisionDesc',
                      '{http://www.tei-c.org/ns/1.0}listChange',   '{http://www.tei-c.org/ns/1.0}change',
                      '{http://www.tei-c.org/ns/1.0}date',         '{http://www.tei-c.org/ns/1.0}name',
                      '{http://www.tei-c.org/ns/1.0}text',         '{http://www.tei-c.org/ns/1.0}body',
                      '{http://www.tei-c.org/ns/1.0}div',          '{http://www.tei-c.org/ns/1.0}head',
                      '{http://www.tei-c.org/ns/1.0}p']

    assert elems == expected_elems


def test_odt_output():
    elems = get_tag_list('odt')
    expected_elems = ['{http://www.tei-c.org/ns/1.0}TEI',          '{http://www.tei-c.org/ns/1.0}teiHeader',
                      '{http://www.tei-c.org/ns/1.0}fileDesc',     '{http://www.tei-c.org/ns/1.0}titleStmt',
                      '{http://www.tei-c.org/ns/1.0}title',        '{http://www.tei-c.org/ns/1.0}author',
                      '{http://www.tei-c.org/ns/1.0}editionStmt',  '{http://www.tei-c.org/ns/1.0}edition',
                      '{http://www.tei-c.org/ns/1.0}date',         '{http://www.tei-c.org/ns/1.0}publicationStmt',
                      '{http://www.tei-c.org/ns/1.0}p',            '{http://www.tei-c.org/ns/1.0}sourceDesc',
                      '{http://www.tei-c.org/ns/1.0}p',            '{http://www.tei-c.org/ns/1.0}profileDesc',
                      '{http://www.tei-c.org/ns/1.0}langUsage',    '{http://www.tei-c.org/ns/1.0}language',
                      '{http://www.tei-c.org/ns/1.0}revisionDesc', '{http://www.tei-c.org/ns/1.0}listChange',
                      '{http://www.tei-c.org/ns/1.0}change',       '{http://www.tei-c.org/ns/1.0}name',
                      '{http://www.tei-c.org/ns/1.0}date',         '{http://www.tei-c.org/ns/1.0}text',
                      '{http://www.tei-c.org/ns/1.0}body',         '{http://www.tei-c.org/ns/1.0}p',
                      '{http://www.tei-c.org/ns/1.0}p']

    assert elems == expected_elems
