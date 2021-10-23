import math
import copy
from py_spec._list.models import LinkModel, PaginationModel

class List:
    page = 1
    size = 10
    aux_keys = ['page', 'size', 'order', 'order_by', 'sort', 'sort_by']

    def __init__(self, page=1, size=size, total=None):
        self.page = page
        self.size = size

    def calc_pages(self):
        pages = self.total / self.size
        return pages

    def calc_offset(self):
        offset = (self.page - 1) * self.size
        return offset

    def get_filters(self, filters, aux_keys=None):
        if not aux_keys:
            aux_keys = self.aux_keys

        filters = copy.copy(filters)
        for k in aux_keys:
            if k in filters:
                del filters[k]
        return filters






