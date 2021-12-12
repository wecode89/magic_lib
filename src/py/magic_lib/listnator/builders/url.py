import copy
from magic_lib.listnator.helpers.models import Url


class UrlBuilder:

    def __init__(self, label=None, path=None, params={}, selected=None):
        # path
        self.path = path
        self.params = params
        self.label = label
        self.selected = selected

        # assert
        assert ('?' not in path)
        assert (isinstance(self.params, dict))

    def build(self):
        url = self.path + "?" + '&'.join(["{}={}".format(k, v) for k, v in self.params.items()])
        url_object = Url(url, self.label, selected=self.selected)
        return url_object


