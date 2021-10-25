import unittest
from ddt import ddt, data, unpack
from magic_lib.listnator.builders.paging import PagingBuilder, Segment


@ddt
class TestSegment(unittest.TestCase):
    @data(
        [1, 1, 10, [1]],
        [5, 25, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9,10]],
        [8, 25, 10, [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]],
        [25, 25, 10, [16, 17, 18, 19, 20, 21, 22, 23, 24, 25]]
    )
    @unpack
    def test_get(self, page, pages, size, expected):
        segment = Segment(page=page, pages=pages, size=size).get()
        self.assertEqual(segment, expected)


class TestPaging(unittest.TestCase):

    def test_filter(self):
        path = "/api/v1/path"
        params = {
            "page": "1",
            "p1": "v1",
            "p2": "v2",
        }
        builder = PagingBuilder(path=path, params=params, page=5, size=10, total=350)
        _json = builder.build()

        self.assertTrue(_json, dict)
        self.assertTrue(_json['urls'][0]['url'])


if __name__ == '__main__':
    unittest.main()