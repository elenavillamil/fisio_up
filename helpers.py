#!/usr/bin/env python
################################################################################
################################################################################
#
# Module: helpers.py
#
# Notes
#
# A bunch of helper functions for the use of index.py
#
################################################################################
################################################################################

from collections import defaultdict

################################################################################
# Globals
################################################################################

title_menu_options_file = "title_menu_options.txt"

################################################################################
################################################################################

def get_title_menu_options():
   title_options = []

   with open(title_menu_options_file) as file_handle:
      for line in file_handle:
         # Make sure the options do not have any new lines, or spaces.
         title_options.append(line.strip())

   return title_options