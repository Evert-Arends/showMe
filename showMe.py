# -*- coding: utf-8 -*-
import settings
from gevent import monkey
from gevent.pywsgi import WSGIServer
from showMe import app

monkey.patch_all()
__author__ = "Evert Arends"

app.debug = settings.DEBUG
http_server = WSGIServer((settings.BIND_HOST, settings.BIND_PORT), app)
print ' * Running on http://%s:%s/ (Press CTRL+C to quit)' % (settings.BIND_HOST, str(settings.BIND_PORT))
http_server.serve_forever()

if __name__ == '__main__':
    app.run()
