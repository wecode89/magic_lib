from magic_lib.misc.encode import JsonBase


class Url(JsonBase):
    def __init__(self, url, label, selected=False, active=True):
        self.url = url
        self.label = str(label)
        self.selected = selected
        self.active = active


class Choice(JsonBase):
    def __init__(self, label=None, value=None, url=None):
        self.label = label
        self.value = value
        self.url = url


class Filter(JsonBase):
    def __init__(self, key, label, choices):
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


class Paging(JsonBase):
    def __init__(self, urls=None, total=None, page=None, pages=None, offset=None, size=None):
        self.urls = urls
        self.total = total
        self.page = page
        self.pages = pages
        self.offset = offset
        self.size = size


if __name__ == '__main__':
    # demo
    c1 = Choice('c1', 'v1')
    c2 = Choice('c2', 'vv')
    _choices = [c1, c2]

    item = Filter('k', 'v', _choices)
    print(item.to_json())
    print(type(item.to_json()))