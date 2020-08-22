import logging
import decimal
import json
from functools import partial

import requests


class BitcoinRPC(object):
    def __init__(self, url, rpcuser, rpcpassword):
        self.idcount = 0
        self.url = url
        self.rpcuser = rpcuser
        self.rpcpassword = rpcpassword

    def __getattr__(self, name):
        return partial(self.call, name)

    def call(self, method, *params):
        c = self.idcount
        self.idcount += 1

        logging.debug("calling bitcoid {} with params {}".format(method, params))
        v = requests.post(
            self.url,
            auth=(self.rpcuser, self.rpcpassword),
            json={"version": "1.1", "method": method, "params": params, "id": c},
        ).text
        logging.debug("got response from bitcoind: " + v)
        resp = json.loads(v, parse_float=decimal.Decimal)

        if "error" in resp and resp["error"] is not None:
            raise JSONRPCError(resp["error"])

        if "result" not in resp:
            raise JSONRPCError({"code": -343, "message": "missing JSON-RPC result"})

        return resp["result"]


class JSONRPCError(Exception):
    pass
