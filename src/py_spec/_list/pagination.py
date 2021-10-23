import math
import copy
from py_spec._list.link import Link



class PaginationModel:
    def __init__(self, links=None, total=None, pages=None, start=None, end=None):
        self.links = links
        self.total = total
        self.pages = pages
        self.start = start
        self.end = end

    def get_pagination(self, url=None, filters={}, segment=10):
        # vars
        previous, next = [], []
        curr = self.page
        end = self.calc_pages()

        # previous segment
        for i in range(curr - int(segment / 2), curr):
            if i > 0:
                previous.append(i)

        # next segment
        for i in range(curr + 1, curr + segment/ 2 + 1):
            if i <= end:
                next.append(i)

        # if previous segment is too short, expand next segment
        if len(previous) < segment / 2:
            diff = segment / 2 - len(previous)
            for i in range(curr + segment / 2 + 1, curr + segment / 2 + 1 + diff + 1):
                if i <= end and i not in next:
                    next.append(i)

        # if next segment is too short, expand previous segment
        if len(next) < segment / 2:
            diff = segment / 2 - len(next)
            for i in range(curr - int(segment / 2) - diff, curr - int(segment / 2) + 1):
                if i > 0 and i not in previous:
                    previous.append(i)

        # merge
        nums = previous + [curr] + next

        # get links
        links = []
        for num in nums:
            link = self.get_link(self, url=url, filters=filters, key=num, val=num, reset={'page': num})
            selected = False
            if num == selected:
                selected = True
            links.append(LinkModel(link, num, selected=selected).get_json())

        # get pagination
        pagination = PaginationModel(links=link, total=toal, pages=page, start=start, end=end).get_json()
        return pagination

    def get_json(self):
        pagination = {
            'links': self.links,
            'total': self.total,
            'pages': self.pages,
            'start': self.start,
            'end': self.end
        }
        return pagination







