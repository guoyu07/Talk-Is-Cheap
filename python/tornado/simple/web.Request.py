#!/usr/bin/env python
# coding=utf-8
import logging
import os
import uuid

import tornado.ioloop
import tornado.web
import tornado.gen
import tornado.httpclient
import tornado.escape


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write(
            '<html><body><form action="/form" method="POST">'
            '<input type="text" name="msg">'
            '<input type="text" name="msg">'
            '<input type="submit" value="Submit">'
            '</form></body></html>'
        )

    def post(self):
        self.write(
            'The host is %s, method is %s, remote_ip is %s and UA is %s' % (
                self.request.host, self.request.method, self.request.remote_ip,
                self.request.headers.get('User-Agent')
            )
        )


class FormHandler(tornado.web.RequestHandler):

    def post(self):
        self.set_header('Content-Type', 'text/plain')
        msg = self.get_arguments('msg')
        for i in msg:
            self.write('msg is %s\n' % i)


class FileFormHandler(tornado.web.RequestHandler):

    def get(self):
        self.write(
            '<html><body><form enctype="multipart/form-data" action="/file" method="POST">'
            '<input type="file" name="file">'
            '<input type="submit" value="Submit">'
            '</form></body></html>'
        )

    def post(self):
        fileinfo = self.request.files['file'][0]
        fname = fileinfo['filename']
        ctype = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + ctype

        f = open('./' + cname, 'w')
        f.write(fileinfo['body'])
        self.finish('%s is uploaded! and rename %s, check current folder.'
                    % (fname, cname))


class BaseHandler(tornado.web.RequestHandler):

    def initialize(self, key):
        logging.warning('default keyword argument is %s' % key)

    def prepare(self):
        logging.warning('prepare ..')
        # self.finish()
        # self.send_error()


class SequenceHandler(BaseHandler):

    # def initialize(self, key):
        # logging.warning('SequenceHandler default keyword argument is %s' % key)

    def get(self):
        logging.warn('SequenceHandler get ..')
        self.write_error(200)

    def post(self):
        logging.warn('SequenceHandler post ..')


class RedirectHandler(BaseHandler):

    def initialize(self, url):
        self.url = url

    def get(self):
        self.redirect(self.url, status=302)


class AsyncHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        res = yield http.fetch('http://apis.baidu.com/heweather/pro/attractions')
        json = tornado.escape.json_decode(res.body)
        self.write(json)

    @tornado.web.asynchronous
    def post(self):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch('http://apis.baidu.com/heweather/pro/attractions', callback=self.on_response)

    def on_response(self, res):
        if res.error:
            raise tornado.web.HTTPError(500)

        json = tornado.escape.json_decode(res.body)
        self.write(json)
        self.finish()


class PageHandler(tornado.web.RequestHandler):

    def get(self):
        logging.warning(self.request.path)

        self.render('template.html', title='test', items=map(str, range(10)))


if __name__ == '__main__':
    settings = {
        'debug': True,
        'compiled_template_cache': False
    }

    app = tornado.web.Application([
        (r'/', MainHandler),
        (r'/form', FormHandler),
        (r'/file', FileFormHandler),
        (r'/sequence', SequenceHandler, {'key': 'test'}),
        (r'/redirect', RedirectHandler, {'url': '/file'}),
        (r'/webredirect', tornado.web.RedirectHandler, {'url': '/file'}),
        (r'/async', AsyncHandler),
        (r'/page', PageHandler)
    ], **settings)

    app.listen(9999)
    logging.warning('start ..')
    tornado.ioloop.IOLoop.current().start()
