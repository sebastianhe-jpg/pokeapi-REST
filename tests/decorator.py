# -*- coding: utf-8 -*-
"""
asdf
"""
import json
import time


def print_test_time_elapsed(method):
    """
    Utility method for print verbalizing test suite, prints out
    time taken for test and functions name, and status
    """
    def run(*args, **kw):
        tss = time.time()
        method_name = method.__name__
        print(f'testing function {method_name}')
        method(*args, **kw)
        tee = time.time() - tss
        print(f'[OK] in {tee} %2.2f sec')
    return run


def is_json(myjson):
    """
    a
    :param myjson:
    :return:
    """
    try:
        json_object = json.loads(myjson)
        del json_object
    except ValueError as err:
        del err
        return False
    return True
