class UrlModel:
    def __init__(self, link, label, selected=False, active=True):
        self.link = link
        self.label = str(label)
        self.selected = selected
        self.active = active

    def get(self):
        link = {
            'link': link,
            'label': label,
            'selected': self.selected,
            'active': active
        }
        return link

class UrlBuilder:
    aux_keys = ['page', 'size', 'order', 'order_by', 'sort', 'sort_by']

    def __init__(self, url=None, filters=None, aux_keys=None):
        self.url = url
        self.filters = self._clean_filters(filters)

        self.aux_keys = aux_keys
        if not self.aux_keys:
            self.aux_keys = UrlBuilder.aux_keys

    def _clean_filters(self):
        # remove aux keys from filters
        filters = copy.copy(self.filters)
        for k in aux_keys:
            if k in filters:
                del filters[k]
        return filters

    def build(self, key=None, val=None, reset={'page': 1}):
        # copy and overwrite filter
        filters = copy.copy(self.filters)
        filters[key] = val

        # reset keys in filters
        for k, v in reset.items():
            filters[k] = v

        # create url
        url = url + "?"
        url = url + '&'.join(["{}={}".format(k, v) for k, v in filters.items()])
        return url