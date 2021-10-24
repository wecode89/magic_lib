import unittest
from xspec.listnator.helpers.models import Choice, Filter
from xspec.listnator.builders.filters import FilterBuilder


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
        _json = builder.build()

        print(_json)


if __name__ == '__main__':
    unittest.main()