class Link:
    @staticmethod
    def get_link(url=None, filters={}, key=None, val=None, reset={'page': 1}):
        filters[key] = val
        for k, v in reset.items():
            filters[k] = v

        url = url + "?"
        url = url + '&'.join(["{}={}".format(k, v) for k, v in filters.items()])
        return url

class LinkModel:
    def __init__(self, link, label, selected=False):
        self.link = link
        self.label = str(label)
        self.selected = selected

    def get_json(self):
        link = {
            'link': link,
            'label': label,
            'selected': self.selected
        }
        return link