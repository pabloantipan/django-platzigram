"""Platzigram views."""
#  Django
from django.http.response import HttpResponse

#  Utilities
from datetime import datetime
import json


def hello_world(request):
    """Return a greeting"""
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse(f"Oh, hi! Current server time is {now}")


def order_numbers(request):
    try:
        numbers = [int(x) for x in request.GET["numbers"].split(",")]
        numbers.sort()
        return numbers
    except Exception as err:
        print(err)


def sort_integers(request):
    """Return a JSON response with sorted integers."""
    # import pdb
    # pdb.set_trace()

    # numbers = {"numbers": }
    data = {
        "status": "ok",
        "numbers": order_numbers(request),
        "message": "Integer sorted successfully",
    }

    return HttpResponse(
        json.dumps(data, indent=4),
        content_type="application/json",
    )


def say_hi(request, name, age):
    """Return a greeting."""
    if age < 12:
        message = "Sorry {}, you are not allowed here".format(name)
    else:
        message = "Hello {}, Welcome to Platzigram".format(name)

    return HttpResponse(message)
