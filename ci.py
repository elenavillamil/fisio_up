#!/usr/bin/env python
################################################################################
################################################################################
#
# Module: ci.py
#
# Notes:
#
# Small script to automate running unit tests on each PR.
#
################################################################################
################################################################################

import helpers
import os
import shutil
import unittest
import xmlrunner

from collections import defaultdict

################################################################################
# Unit Tests
################################################################################

class RestTests(unittest.TestCase):
   def test_setup(self):
      # Simple test to make sure the unit tester is working correctly.
      pass

   # index.py takes a dependency on the function helpers.get_title_menu_options
   # returning a list of strings when called.
   def test_get_title_menu_options(self):
      menu_options_first_call = helpers.get_title_menu_options()

      for menu_option in menu_options_first_call:
         if not isinstance(menu_option, str):
            error_str = "Error, menu option must be a string."
            self.fail("%s Type: %s" % (error_str, type(menu_option)))

      # Sanity check, make sure repeated calls returns the same values
      menu_options_second_call = helpers.get_title_menu_options()

      if len(menu_options_first_call) !=  len(menu_options_second_call):
         error_str = "Error, repeated calls to get_title_menu_options yielded"
         error_str += " different results."
         first = menu_options_first_call
         second = menu_options_second_call

         self.fail("%s: %s, %s" % (error_str, first, second))

      for index, menu_option in enumerate(menu_options_second_call):
         if not isinstance(menu_option, str):
            error_str = "Error, menu option must be a string."
            self.fail("%s Type: %s" % (error_str, type(menu_option)))

         if menu_option != menu_options_first_call[index]:
            error_str = "Error, repeated calls to get_title_menu_options yielded"
            error_str += " different results."
            first = menu_options_first_call
            second = menu_options_second_call

            self.fail("%s: %s, %s" % (error_str, first, second))

################################################################################
# Main
################################################################################

if __name__ == "__main__":
   # Remove previous xml files.
   shutil.rmtree("test-reports")

   unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
