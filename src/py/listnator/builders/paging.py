from py.listnator.helpers.models import Url, Paging
from py.listnator.builders.url import UrlBuilder


class PagingBuilder:

    def __init__(self, url=None, filters={}, segment=10,
                 page=1, size=10, total=0):
        self.url = url
        self.filters = filters
        self.segment = segment

        self.page = page
        self.size = size
        self.total = total

        self.offset = offset = (self.page - 1) * self.size
        self.pages = self.total / self.size

        self.url_builder = UrlBuilder(url=self.url, filters=self.filters)

    def _get_visible(self):
        # vars
        previous, next = [], []
        curr = self.page
        end = self.pages

        # previous segment
        for i in range(curr - int(self.segment / 2), curr):
            if i > 0:
                previous.append(i)

        # next segment
        for i in range(curr + 1, curr + self.segment/ 2 + 1):
            if i <= end:
                next.append(i)

        # if previous segment is too short, expand next segment
        if len(previous) < self.segment / 2:
            diff = self.segment / 2 - len(previous)
            for i in range(curr + self.segment / 2 + 1, curr + self.segment / 2 + 1 + diff + 1):
                if i <= end and i not in next:
                    next.append(i)

        # if next segment is too short, expand previous segment
        if len(next) < self.segment / 2:
            diff = self.segment / 2 - len(next)
            for i in range(curr - int(self.segment / 2) - diff, curr - int(self.segment / 2) + 1):
                if i > 0 and i not in previous:
                    previous.append(i)

        # merge
        visible = previous + [curr] + next
        return visible

    def _get_urls(self):
        # get links
        urls = []

        visible = self._get_visible()
        for page in visible:
            # url
            url = self.url_builder.build(self.url, key=page, val=page, reset={'page': page})

            # selected
            selected = False
            if page == self.page:
                selected = True

            # add to list
            model = Url(url, page, selected=selected)
            urls.append(model)
        return urls

    def build(self):
        url = self._get_urls()
        paging = Paging(urls=url, total=self.total, pages=self.pages, offset=self.offset)
        data = paging.to_json()
        return data









