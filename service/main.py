import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djandro.settings")
from colors import add_markup
from django.core.servers.basehttp import WSGIServer, WSGIRequestHandler, get_internal_wsgi_application
from djandro.utils import Borg

#logpath = os.getenv('PYTHON_SERVICE_ARGUMENT')

class RequestHandler(WSGIRequestHandler):
    def log_message(self, format, *args):
        # Don't bother logging requests for admin images or the favicon.
        if (self.path.startswith(self.admin_static_prefix)
                or self.path.startswith('/logging/')
                or self.path == '/favicon.ico'):
            return

        msg = "[%s] %s" % (self.log_date_time_string(), format % args)
        kivymarkup = add_markup(msg, args)
        Borg().queue.put(kivymarkup)


server_address = ('0.0.0.0', 8000)
wsgi_handler = get_internal_wsgi_application()
httpd = WSGIServer(server_address, RequestHandler)
httpd.set_app(wsgi_handler)
httpd.serve_forever()
