import os
import tornado.ioloop
import tornado.web
from tornado.web import url

BASE_DIR = os.path.dirname(__file__)

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")

class PythonHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("python.html")

app = tornado.web.Application([
	url(r"/", IndexHandler, name="index"),
	url(r"/python/", PythonHandler, name="python"),
	],
	template_path=os.path.join(BASE_DIR, "templates"),
	static_path=os.path.join(BASE_DIR, "static"),
)

if __name__ == '__main__':
	app.listen(8000)
	tornado.ioloop.IOLoop.current().start()
	