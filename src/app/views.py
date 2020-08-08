from django.http import HttpResponse
import logging
from random import randint

logger = logging.getLogger(__name__)


def index(request):
    logger.info("Hello from log", extra={'random': randint(1, 100)})

    return HttpResponse(f'Hello')
