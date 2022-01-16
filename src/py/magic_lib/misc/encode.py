import json


class EncoderBase(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, bool):
            return super().default(o)
        elif isinstance(o, int):
            return super().default(o)
        elif isinstance(o, float):
            return super().default(o)
        elif isinstance(o, str):
            return super().default(o)
        elif hasattr(o, 'to_json'):
            return o.to_json()
        return o.__dict__


class JsonBase:
    def __init__(self):
        pass

    def to_json(self, encoder=EncoderBase):
        # dump data
        string = json.dumps(self, cls=encoder)
        data = json.loads(string)
        return data