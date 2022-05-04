# -*- coding: utf-8 -*-
"""
decorator for test functions
"""
import json
import time


def print_time_elapsed(method):
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
