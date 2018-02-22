import os

import tornado.ioloop
import tornado.web
from tornado.web import url

BASE_DIR = os.path.dirname(__file__)

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		# queryからnameの値を取得、第2引数にデフォルトの値をセット
		name = self.get_argument("name", "Taro")
		fruits = ["apple", "orange", "banana"]
		# パラメータを全て取得、複数あればリスト形式に変換
		# items = self.get_arguments("items")
		items = self.get_query_arguments("items")
		self.render("index.html", title = "TornadoSampleApp1", name = name, items = items)

application = tornado.web.Application([
	(r"/", MainHandler),
	],
	template_path = os.path.join(BASE_DIR, "templates"),
	static_path = os.path.join(BASE_DIR, "static"),
)

if __name__ == '__main__':
	application.listen(8000)
	tornado.ioloop.IOLoop.current().start()
