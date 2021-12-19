import json
import os
import socket
from flask import Flask, jsonify, request
from pymemcache.client import base
from magic_lib.misc.log import get_logger


logger = get_logger(os.path.basename(__file__), level=os.environ.get('LOG_LEVEL', 'DEBUG'))


def cache(cache_client=None, expire=None):
    def outer(f):
        def inner(*arg, **kwargs):
            # skip cache client
            if os.environ.get('CACHE', '').lower() == 'false' \
                    or not cache_client.client:
                return f(*arg, **kwargs)

            # get cache
            try:
                key = request.url
                # #cache = cache_client.get(key)
                # if cache:
                #     cache['cache'] = True
                #     return jsonify(cache)
            except socket.gaierror as e:
                pass
                #logger.error("MEMCACHE get error {}".format(e))

            # set cache
            try:
                result = f(*arg, **kwargs)
                if result:
                    cache_client.set(key, result, expire=expire)
                result['cache'] = False
                return jsonify(result)
            except socket.gaierror as e:
                pass
                #logger.error("MEMCACHE set error {}".format(e))

            # last call to actual function
            return f(*arg, **kwargs)
        inner.__name__ = f.__name__
        return inner
    return outer


class MemCacheConnector:
    def __init__(self, client=None, host='localhost', port=11211):
        logger.info("MemCache host: {}, port: {}".format(host, port))
        if not client:
            try:
                self.client = base.Client((host, port))
            except Exception as e:
                pass

    def set(self, key, json_val, expire=None):
        return None
        if json_val:
            self.client.set(key, json.dumps(json_val), expire=expire)

    def get(self, key):
        return None
        data = self.client.get(key)
        _json = json.loads(data)
        return _json
