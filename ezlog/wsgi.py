"""
WSGI config for ezlog project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname( os.path.realpath(__file__) )))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ezlog.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)

if __name__ == '__main__':
    from wsgiref import simple_server
    host='127.0.0.1'
    port=8000
    server = simple_server.make_server(app=application, host=host, port=port)
    print 'listen on %s:%d'%(host, port)
    server.serve_forever()
