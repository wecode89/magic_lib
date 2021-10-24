import copy
from py.listnator.helpers.models import Url
from py.listnator.builders.url import UrlBuilder


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
                url = self.url_builder.build(self, key=key, val=value, reset={'page': 1})

                # selected
                selected = False
                if key in self.filters and str(self.filters[key]) == str(value):
                    selected = True

                # fill
                choice['url'] = Url(url, label, selected=selected).get()

        filled = [x.to_json() for x in filled]
        return filled

