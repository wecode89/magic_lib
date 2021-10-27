import json


class EncoderBase(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, bool):
            return super().default(o)
        if isinstance(o, int):
            return super().default(o)
        if isinstance(o, float):
            return super().default(o)
        if isinstance(o, str):
            return super().default(o)
        return o.__dict__


class JsonBase:
    def __init__(self):
        pass

    def to_json(self, encoder=EncoderBase):
        # dump data
        string = json.dumps(self, cls=encoder)
        data = json.loads(string)
        return data