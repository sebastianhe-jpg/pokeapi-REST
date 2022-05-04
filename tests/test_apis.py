# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
unit test module for modules in mods folder
"""
import unittest
from decorator import print_test_time_elapsed
from .apps import apis


class TestModules(unittest.TestCase):
    """
    module class for unit test
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @print_test_time_elapsed
    def test_view_closest_partner(self):
        """
        Tests find closest function from partners class
        """
        partner = apis.amount_match_names()
        apis.amount_breeding_especies()
        apis.minmax_weights()
        self.assertIsInstance(partner, dict)
        self.assertIsInstance(partner, int)


if __name__ == '__main__':
    unittest.main()
