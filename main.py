#!/usr/bin/env python

import os
from tornado import ioloop,web
from tornado.escape import json_encode

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html")

settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug" : True
}

application = web.Application([
    (r'/', IndexHandler),
    (r'/index', IndexHandler),
],**settings)

if __name__ == "__main__":
    application.listen(8888)
    ioloop.IOLoop.instance().start()