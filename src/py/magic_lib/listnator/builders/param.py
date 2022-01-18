import copy

IGNORE_PARAMS = ['page', 'size', 'order', 'order_by', 'sort', 'sort_by']


class ParamBuilder:
    def __init__(self, params, ignore_keys=[]):
        self.params = params
        self.ignore_keys = ignore_keys

    def build(self):
        if not self.params:
            params = {}

        params = copy.copy(self.params)
        for k in self.ignore_keys:
            if k in params:
                del params[k]
        return params


class MongoBuilder:
    def __init__(self, params, ignore_keys=[]):
        self.params = params
        self.ignore_keys = ignore_keys

    def build(self):
        if not self.params:
            params = {}

        # copay params
        params = copy.copy(self.params)

        # delete ignore keys
        for k in self.ignore_keys:
            if k in params:
                del params[k]

        # handle special cases
        new_params = {}
        for k, v in params.items():
            if k.endswith("__lte"):
                new_params[k[:-5]] = {'$lte': float(v)}
            else:
                new_params[k] = v
        return new_params