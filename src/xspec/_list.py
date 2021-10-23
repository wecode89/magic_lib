import math


class ListSpec:
    spec = {
        'paging': {
            'page': {
                'default': 1
            },
            'size': {
                'default': 10
            },
        },
        'keys': {
            'aux': ['order', 'order_by' 'sort', 'page', 'size']
        }
    }

    def __init__(self, selected_page=1, selected_size=10, selected_order=None):
        self.order = order
        self.page = page
        self.size = size

    @staticmethod
    def calc_total_pages(total=None, size=None):
        total_pages = math.ceil(total / size)
        return total_pages

    @staticmethod
    def calc_offset(page=None, size=None):
        offset = (page - 1) * size;
        return offset
