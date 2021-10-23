class FilterModel:
    def __init__(self, filter_options=None, filter_params=None):
        """
        :param filter_options:
        [
            {
                "key": "price",
                "options": [
                   {"label": 10
                    "value: 10},
                   {"label": 20
                    "value": 20},
                ]
            },
            {
                "key": "distance",
                "options": [
                   {"label": "10 Miles"
                    "value: 10},
                   {"label": "20 Miles"
                    "value:: 20},
                ]
            },
        ]
        """
        self.filter_options = filter_options

    def get_json(self):
        for row in filter_options():
            key = row['key']
            options = row['options']
            for option in options:
                label = options['label']
                value = options['value']
                Link.get_link(self, url=url, filters=filters, key=num, val=num)