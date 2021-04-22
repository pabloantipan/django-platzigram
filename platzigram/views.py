"""Platzigram views"""
# Django
from django.http import HttpResponse, QueryDict

#  Utilities
from datetime import datetime
import json


def hello_world(request):
    """Return a greeting."""
    now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
    return HttpResponse(f"Oh, hi! Current server time is {now}")


def sorted(request):
    """Returns sorted numbers as JSON."""
    # print("request.scheme:", request.scheme)
    # print("request.body:", request.body)
    print("request.GET:", request.GET)

    numbers = [int(x) for x in request.GET["numbers"].split(",")]
    numbers.sort()
    print("numbers:", numbers)

    data = {
        "status": "ok",
        "numbers": numbers,
        "message": "Integer sorted successfully!",
    }

    # import pdb
    # pdb.set_trace()
    return HttpResponse(json.dumps(data, indent=4), content_type="application/json")


def hi(request, name, age):
    """Hi, accord age."""
    if age < 12:
        message = f"You are not allowed here! Sorry {name.capitalize()} :c"
    else:
        message = f"{name.capitalize()}, Welcome to Platzigram  :D"

    return HttpResponse(message)
