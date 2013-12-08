import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djandro.settings")
from django.core.management.commands.runserver import Command
runserver = Command()
runserver.execute()