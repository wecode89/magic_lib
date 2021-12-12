import copy
import math
from magic_lib.listnator.helpers.models import Url, Paging
from magic_lib.listnator.builders.url import UrlBuilder


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
        start_inclusive = self.page - self.partition_size

        # end
        end_inclusive = self.page - 1

        # form
        leading = [i for i in range(start_inclusive, end_inclusive + 1) if i > 0]
        return leading

    def _get_following(self):
        # start
        start_inclusive = self.page + 1

        # end
        end_inclusive = self.page + self.partition_size

        # form
        following = [i for i in range(start_inclusive, end_inclusive + 1) if i <= self.pages]
        return following

    def _balance_left(self, left, right, partition_size=None):
        diff = partition_size - (len(left) + 1)
        if diff > 0 and right:
            while diff > 0:
                last = right[-1]
                _next = last + 1
                if _next <= self.pages:
                    right.append(_next)
                diff = diff - 1

    def _balance_right(self, left, right, partition_size=None):
        diff = partition_size - (len(right) + 1)
        if diff > 0 and left:
            while diff > 0:
                first = left[0]
                _previous = first - 1

                if _previous > 0:
                    left.insert(0, _previous)
                diff = diff - 1


class PagingBuilder:

    def __init__(self, path=None, params={}, page=1, size=10, total=0):
        self.path = path
        self.params = params

        self.page = page
        self.size = size
        self.total = total

        self.offset = (self.page - 1) * self.size
        self.pages = math.ceil(self.total / self.size)

    def build(self):
        # get pagination segment
        segment = Segment(page=self.page, pages=self.pages, size=self.size).get()

        # build url objects
        url_objects = []
        for page in segment:
            # selected
            selected = False
            if page == self.page:
                selected = True

            # params
            params = copy.copy(self.params)
            params['page'] = page

            # url object
            url_builder = UrlBuilder(label=self.page, path=self.path, params=params, selected=selected)
            url_objects.append(url_builder.build())

        # paging object
        paging = Paging(urls=url_objects, total=self.total, page=self.page, pages=self.pages,
                        offset=self.offset, size=self.size)
        data = paging.to_json()
        return data









