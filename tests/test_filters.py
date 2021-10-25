import unittest
from magic_lib.listnator.helpers.models import Choice, Filter
from magic_lib.listnator.builders.filters import FilterBuilder


class TestFilter(unittest.TestCase):

    def test_filter(self):
        c1 = Choice(label='c1', value='v1')
        c2 = Choice(label='c2', value='v2')
        cx = Choice(label='cx', value='vx')
        cy = Choice(label='cy', value='vy')

        f1 = Filter(label='f1', key='f1', choices=[c1, c2])
        fx = Filter(label='f1', key='f1', choices=[cx, cy])

        filters = [f1, fx]

        path = "/api/v1/path"
        params = {
            "page": "1",
            "p1": "v1",
            "p2": "v2",
        }
        builder = FilterBuilder(path=path, params=params, filters=filters)
        filters = builder.build()
        self.assertTrue(isinstance(filters, list))

        for _filter in filters:
            self.assertTrue(isinstance(_filter, dict))
            for choice in _filter['choices']:
                self.assertTrue('url' in choice)


if __name__ == '__main__':
    unittest.main()