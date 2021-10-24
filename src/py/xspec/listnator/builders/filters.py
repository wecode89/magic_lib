import copy
from xspec.listnator.helpers.models import Url
from xspec.listnator.builders.url import UrlBuilder


class FilterBuilder:

    def __init__(self, path=None, params=None, filters=None):
        self.filters = filters
        self.params = params
        self.url = path
        self.url_builder = UrlBuilder(path=self.url, params=self.params)

    def build(self):
        # copy config
        filters = copy.copy(self.filters)

        # iter filter
        for _filter in filters:
            key, choices = _filter['key'], _filter['choices']

            # iter choices
            for choice in choices:
                # get url
                label, value = choice['label'], choice['value']
                url_string = self.url_builder.build(self, key=key, val=value, reset={'page': 1})

                # selected
                selected = False
                if key in self.params and str(self.params[key]) == str(value):
                    selected = True

                # fill
                url = Url(url_string, label, selected=selected)
                choice['url'] = url.to_json()

        enriched = [_filter.to_json() for _filter in filters]
        return enriched

