import math
from xspec.listnator.helpers.models import Url, Paging
from xspec.listnator.builders.url import UrlBuilder


class Segment:
    def __init__(self, page=1, pages=0, size=10):
        self.page = page
        self.pages = pages
        self.size = size
        self.partition_size = math.floor(size / 2)

    def get(self):
        leading = self._get_leading()
        following = self._get_following()

        self._balance_left(leading, following, partition_size=self.partition_size)
        self._balance_right(leading, following, partition_size=self.partition_size)

        segment = leading + [self.page] + following
        return segment

    def _get_leading(self):
        # start
        start = self.page - self.partition_size
        if start < 0:
            start = 1

        # end
        end = self.page

        # form
        leading = [i for i in range(start, end)]
        return leading

    def _get_following(self):
        # start
        start = self.page + 1
        if start > self.pages:
            start = self.pages

        # end
        end = start + self.partition_size + 1
        if end > self.pages:
            end = self.pages + 1

        following = [i for i in range(start, end)]
        return following

    def _balance_left(self, left, right, partition_size=None):
        diff = (len(left) + 1) - partition_size
        if diff > 0:
            while diff > 0:
                last = right[-1]
                _next = last + 1
                if _next <= self.pages:
                    right.append(_next)
                diff = diff - 1

    def _balance_right(self, left, right, partition_size=None):
        diff = len(right) + 1 - partition_size
        if diff > 0:
            while diff > 0:
                first = left[0]
                _previous = first - 1
                if _previous > 0:
                    left.insert(0, _previous)
                diff = diff - 1


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

    def _get_urls(self):
        # get links
        urls = []

        segment = Segment(page=self.page, pages=self.pages, size=self.size).get()
        for page in segment:
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









