import os
from colors import add_markup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djandro.settings")
from django.core.servers.basehttp import WSGIServer, WSGIRequestHandler, get_internal_wsgi_application


logpath = os.getenv('PYTHON_SERVICE_ARGUMENT')


class RequestHandler(WSGIRequestHandler):
    stderr = open(logpath, 'w', 0)
    def log_message(self, format, *args):
        # Don't bother logging requests for admin images or the favicon.
        if (self.path.startswith(self.admin_static_prefix)
                or self.path == '/favicon.ico'):
            return

        msg = "[%s] %s\n" % (self.log_date_time_string(), format % args)
        kivymarkup = add_markup(msg, args)
        self.stderr.write(kivymarkup)


server_address = ('0.0.0.0', 8000)
wsgi_handler = get_internal_wsgi_application()
httpd = WSGIServer(server_address, RequestHandler)
httpd.set_app(wsgi_handler)
httpd.serve_forever()
