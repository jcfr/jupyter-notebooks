import requests
from urllib.parse import urlparse
from cdashapi.querybuilder import QueryBuilder

class Downloader(QueryBuilder):

    def __init__(self, url, project, filtercombine=QueryBuilder.AND, date=None):
        QueryBuilder.__init__(self, project, filtercombine, date)
        parsed_url = urlparse(url)
        sheme = parsed_url.scheme if parsed_url.scheme else 'http'
        netloc = parsed_url.netloc if parsed_url.netloc else parsed_url.path
        self._api_url = sheme + "://" + netloc + '/api/v1'
        self._debug = False

    def debug(self, value=True):
        self._debug = value
        return self

    def _print_debug(self, title, content):
        if self._debug:
            print("*" * 20 + title  + "*" * 20)
            print(content)

    @staticmethod
    def _submissions(data):
        info = []
        if data is None:
            return info
        for group in data['buildgroups']:
            info.extend(group['builds'])
        return info

    def __call__(self):
        return self.data()

    def data(self):
        if not hasattr(self, '_data'):
            req = requests.get(self._api_url + "/index.php", params=self.params())
            self._print_debug("req.url", req.url)
            self._data = req.json()
            self._print_debug("self._data", self._data)
        return Downloader._submissions(self._data)

