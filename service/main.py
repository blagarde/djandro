import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djandro.settings")
from django.core.management.commands.runserver import Command
PORT = 8000
runserver = Command()
runserver.execute(addrport='0.0.0.0:%i' % PORT)
