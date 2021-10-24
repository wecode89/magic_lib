import unittest
from xspec.listnator.builders.paging import PagingBuilder


class TestFilter(unittest.TestCase):

    def test_filter(self):
        path = "/api/v1/path"
        params = {
            "page": "1",
            "p1": "v1",
            "p2": "v2",
        }
        builder = PagingBuilder(path=path, params=params, segment=10,
                 page=5, size=10, total=350)
        _json = builder.build()

        print(_json)


if __name__ == '__main__':
    unittest.main()