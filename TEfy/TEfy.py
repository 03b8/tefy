import requests
from lxml import etree


class OxGaWrap(object):
    """
    Very basic wrapper for a small subset of OxGarage conversions, one-way from doc/docx/odt to TEI XML.
    """
    def __init__(self, path, lang='en'):
        """
        :param path: path to file to be converted
        :param lang: value of the oxgarage.lang conversion property
        """
        self.response = None
        self._req_baseurl = 'https://oxgarage.tei-c.org/ege-webservice/Conversions/'
        self._convcodes = {
            'in': {
                'odt': 'odt%3Aapplication%3Avnd.oasis.opendocument.text/',
                'doc': 'doc%3Aapplication%3Amsword/odt%3Aapplication%3Avnd.oasis.opendocument.text/',
                'docx': 'docx%3Aapplication%3Avnd.openxmlformats-officedocument.wordprocessingml.document/'
            },
            'xmlteip5': 'TEI%3Atext%3Axml/', }
        self._params = {'properties': '<conversions><conversion index="0">'
                                      f'<property id="oxgarage.lang">{lang}</property>'
                                      '</conversion></conversions>'}
        self.path = path
        self.format = path.split('.')[-1]
        if self.format not in self._convcodes['in']:
            self.format = None
            codekeys = ', '.join(self._convcodes['in'])
            raise ValueError(f'Unknown input format. Expected one of the following: {codekeys}.')

    def _request_conversion(self):
        """
        Requests the conversion of the file to TEI P5 XML.
        :return: requests.Response
        """
        url = self._req_baseurl + self._convcodes['in'][self.format] + self._convcodes['xmlteip5']
        with open(self.path, 'rb') as doc_file:
            files = {'upload_file': doc_file}
            response = requests.post(url, files=files, params=self._params)
            if response.status_code == 200:
                return response
            response.raise_for_status()

    @property
    def tei_xml(self):
        """
        Get TEI XML document as etree.Element
        """
        self.response = self._request_conversion()
        return etree.fromstring(self.response.content)

    def convert_to_tei(self):
        raise DeprecationWarning('This method has been deprecated and will be removed.')

    def get_et_output(self):
        raise DeprecationWarning('This method has been deprecated and will be removed.'
                                 'Please use the "tei_xml" property instead.')
        return self.tei_xml
