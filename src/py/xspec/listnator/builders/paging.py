import math
from xspec.listnator.helpers.models import Url, Paging
from xspec.listnator.builders.url import UrlBuilder


class PagingBuilder:

    def __init__(self, path=None, params={}, segment=10,
                 page=1, size=10, total=0):
        self.path = path
        self.params = params
        self.segment = segment

        self.page = page
        self.size = size
        self.total = total

        self.offset = (self.page - 1) * self.size
        self.pages = self.total / self.size

        self.url_builder = UrlBuilder(path=self.path, params=self.params)

    def _get_visible(self):
        # vars
        previous, next = [], []
        curr = self.page
        end = self.pages
        half_segment = int(math.floor(self.segment/2))

        # previous segment
        for i in range(curr - half_segment, curr):
            if i > 0:
                previous.append(i)

        # next segment
        for i in range(curr + 1, curr + half_segment + 1):
            if i <= end:
                next.append(i)

        # if previous segment is too short, expand next segment
        if len(previous) < half_segment:
            diff = half_segment - len(previous)
            for i in range(curr + half_segment + 1, curr + half_segment + 1 + diff + 1):
                if i <= end and i not in next:
                    next.append(i)

        # if next segment is too short, expand previous segment
        if len(next) < half_segment:
            diff = half_segment - len(next)
            for i in range(curr - half_segment - diff, curr - half_segment + 1):
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
            url_string = self.url_builder.build(key=page, val=page, reset={'page': page})

            # selected
            selected = False
            if page == self.page:
                selected = True

            # add to list
            url = Url(url_string, page, selected=selected)
            urls.append(url)
        return urls

    def build(self):
        urls = self._get_urls()
        paging = Paging(urls=urls, total=self.total, pages=self.pages, offset=self.offset)
        data = paging.to_json()
        return data









