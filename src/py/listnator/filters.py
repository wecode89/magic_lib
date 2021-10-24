import copy
from py_spec.url import UrlModel, UrlBuilder


class FilterItem:
    def __init__(self, key=None, label=None, choices=None):
        """
        :param key:
        :param label:
        :param choices:
                [{"label": 10 "value: 10},
                 {"label": 20 "value": 20}]
        """
        self.key = key
        self.label = label
        self.choices = choices

    def get(self):
        data = {
            'key': self.key,
            'label': self.label,
            'choices': self.choices
        }
        return data



class FilterBuilder:

    def __init__(self, items=None, url=None, filters=None):
        """
        :param items: FilterItem
        :param url:
        :param filters:
        """
        self.items = items
        self.filters = filters
        self.url = url
        self.url_builder = UrlBuilder(url=self.url, filters=self.filters)

    def build(self):
        # copy config
        filled = copy.copy(self.items)

        # iter filter
        for item in filled:
            key, choices = item['key'], item['choices']

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

                # fill
                choice['url'] = UrlModel(url, label, selected=selected).get()

        filled = [x.get() for x in filled]
        return filled

