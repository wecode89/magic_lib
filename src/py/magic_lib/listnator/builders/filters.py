import copy
from magic_lib.listnator.helpers.models import Url, Paging
from magic_lib.listnator.builders.url import UrlBuilder

class FilterBuilder:

    def __init__(self, path=None, params=None, filters=None):
        self.filters = filters
        self.params = params
        self.path = path

    def build(self):
        # copy config
        filters = copy.copy(self.filters)

        # iter filter
        for _filter in filters:
            key, choices = _filter.key, _filter.choices

            # iter choices
            for choice in choices:
                # get url
                label, value = choice.label, choice.value

                # params
                params = copy.copy(self.params)
                params['page'] = 1
                params[label] = value

                # selected
                selected = False
                if key in self.params and str(self.params[key]) == str(value):
                    selected = True

                # fill
                url_builder = UrlBuilder(label=label, path=self.path, params=params, selected=selected)
                url_object = url_builder.build()
                choice.path = url_object

        enriched = [_filter.to_json() for _filter in filters]
        return enriched

