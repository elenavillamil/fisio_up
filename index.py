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

import os

import tornado.ioloop
import tornado.web

from collections import defaultdict

################################################################################
# Globals
################################################################################

template_path = os.path.join(os.path.dirname(__file__), "templates")
static_path = template_path = os.path.join(os.path.dirname(__file__), "static")

################################################################################
# Helper Functions
################################################################################

################################################################################
# Handlers
################################################################################

class MainHandler(tornado.web.RequestHandler):
   def get(self):
      self.render(
         os.path.join("templates", "index.html")
      )

def make_app():
   handlers = [(r"/", MainHandler)]
   return tornado.web.Application(
      handlers,
      settings = {
         "template_path": template_path,
         "static_path": static_path
      },
      static_path = static_path,
      debug=True
   )
 
################################################################################
# Main
################################################################################
 
if __name__ == "__main__":
   app = make_app()
   app.listen(8888)
   tornado.ioloop.IOLoop.current().start()
