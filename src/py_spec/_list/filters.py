import copy
from py_spec.url import UrlModel, UrlBuilder

class FilterModel:
    def __init__(self, key=None, choices=None):
        pass


class FilterBuilder:

    def __init__(self, config=None, url=None, filters=None):
        """
        :param options:
        [
            {
                "key": "price",
                "choices": [
                   {"label": 10
                    "value: 10},
                   {"label": 20
                    "value": 20},
                ]
            }
        ]
        """
        self.config = config
        self.filters = filters
        self.url = url
        self.url_builder = UrlBuilder(url=self.url, filters=self.filters)

    def build(self):
        # copy config
        enriched = copy.copy(config)

        # iter filter
        for row in enriched:
            key, choices = row['key'], row['choices']

            # iter choices
            for choice in choices:
                # get url
                label = choice['label']
                value = choice['value']
                url = self.url_builder.get_url(self, key=key, val=value, reset={'page': 1})

                # selected
                selected = False
                if key in self.filters and str(self.filters[key]) == str(value):
                    selected = True

                # enrich
                choice['url'] = UrlModel(url, label, selected=selected).get()

        return enriched

