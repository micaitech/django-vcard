from django.http import HttpResponse

import logging
log = logging.getLogger(__name__)

def index(request):
    return HttpResponse("Hello, world!")


