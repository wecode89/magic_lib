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

