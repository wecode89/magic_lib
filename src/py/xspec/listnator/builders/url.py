import copy


class UrlBuilder:
    ignore_keys = ['page', 'size', 'order', 'order_by', 'sort', 'sort_by']

    def __init__(self, path=None, params=None, ignore_keys=None):
        # path
        self.path = path

        # params
        self.params = params
        if not self.params:
            self.params = {}
        self._clean_params()

        # ignore_keys
        self.ignore_keys = ignore_keys
        if not self.ignore_keys:
            self.ignore_keys = UrlBuilder.ignore_keys

        # assert
        assert ('?' not in path)
        assert (isinstance(self.params, dict))
        assert (isinstance(self.ignore_keys, list))

    def _clean_params(self):
        # remove aux keys from filters
        params = copy.copy(self.params)
        for k in self.ignore_keys:
            if k in params:
                del params[k]

    def build(self, key=None, val=None, reset={'page': 1}):
        # copy and overwrite filter
        params = copy.copy(self.params)
        params[key] = val

        # reset keys in filters
        for k, v in reset.items():
            params[k] = v

        # create url
        url_string = self.path + "?"
        url_string = url_string + '&'.join(["{}={}".format(k, v) for k, v in params.items()])
        return url_string


