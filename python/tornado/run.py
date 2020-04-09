from tornado import ioloop, web


class MainHandler(web.RequestHandler):

    def get(self):
        self.write('Hello World!')


def make_app():
    return web.Application([
        (r'/', MainHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8000)
    ioloop.IOLoop.current().start()
