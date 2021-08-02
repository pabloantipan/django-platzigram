"""Posts views."""

# Django
# from django.http import HttpResponse
from django.shortcuts import render

# Utilities
from datetime import datetime

# from django.shortcuts import render

posts = [
    {
        "tittle": "Mont Blac",
        "user": {
            "name": "Yesica Cortes",
            "picture": "https://picsum.photos/60/60/?image=1027",
        },
        "timestamp": datetime.now().strftime("%b %dth, %Y - %H:%M hrs"),
        "photo": "https://picsum.photos/800/600/?image=1036",
    },
    {
        "tittle": "Via Lactea",
        "user": {
            "name": "C. Vander",
            "picture": "https://picsum.photos/60/60/?image=1005",
        },
        "timestamp": datetime.now().strftime("%b %dth, %Y - %H:%M hrs"),
        "photo": "https://picsum.photos/800/600/?image=903",
    },
    {
        "tittle": "Nuevo auditorio",
        "user": {
            "name": "Thespianartist",
            "picture": "https://picsum.photos/60/60/?image=883",
        },
        "timestamp": datetime.now().strftime("%b %dth, %Y - %H:%M hrs"),
        "photo": "https://picsum.photos/800/600/?image=1036",
    },
]


def list_posts(request):
    """List existing posts."""
    # posts = [1, 2, 4]
    content = []
    return render(request, "feed.html", {"posts": posts})
