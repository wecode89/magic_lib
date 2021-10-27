from magic_lib.misc.encode import JsonBase


class ApiResponse(JsonBase):
    def __init__(self, message=None, data=None, status_code=None):
        self.message = message
        self.data = data
        self.status_code = status_code


