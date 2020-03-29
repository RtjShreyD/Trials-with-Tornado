import tornado.ioloop
import tornado.web

class QueryStringHandler(tornado.web.RequestHandler):
    def get(self):
        n=int(self.get_argument("n"))
        r= "odd" if n%2 else "even"
        self.write("The number is" + r)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class StaticRequesthandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/blog", StaticRequesthandler),
        (r"/isEven", QueryStringHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Listening on port 8888")
    tornado.ioloop.IOLoop.current().start()