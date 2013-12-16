from django.http import HttpResponse
from utils import Borg


def log(request):
    q = Borg().queue
    text = ''
    while not q.empty():
        msg = q.get()
        text += msg + '\n'
    return HttpResponse(text)
