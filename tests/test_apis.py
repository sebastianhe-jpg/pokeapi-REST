# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
unit test module for modules in mods folder
"""
import unittest
from decorator import print_time_elapsed
from apps import apis


class TestModules(unittest.TestCase):
    """
    module class for unit test
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @print_time_elapsed
    def test_pokeapis_functions(self):
        """
        Tests find closest function from partners class
        """
        names = apis.amount_match_names()
        breeds = apis.amount_breeding_especies()
        minmax_weight = apis.minmax_weights()
        self.assertIsInstance(names, int)
        self.assertIsInstance(breeds, int)
        self.assertIsInstance(minmax_weight, list)


if __name__ == '__main__':
    unittest.main()
