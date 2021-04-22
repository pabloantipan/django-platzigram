# from django.http import HttpResponse
"""Posts app views."""
# Django
from django.shortcuts import render

# Utilities
from datetime import datetime

titles = ["Mont Blanc", "Via Lactea", "Nuevo Auditorio"]
# names = ["absolutepositive", "patovillarroel", "calfu23"]
names = ["Yesica Cortez", "C. Vander", "AnArtist"]
pictures = [1027, 1005, 883]
photos = [
    "https://picsum.photos/800/600?image=1036",
    "https://picsum.photos/800/800?image=903",
    "https://picsum.photos/60/60?image=883",
]

# punto = [(names[idx], users[idx]) for idx in range(len(names))]

posts = [
    {
        "title": titles[idx],
        "user": {
            "name": names[idx],
            "picture": f"https://picsum.photos/200/200/?image={pictures[idx]}",
        },
        "timestamp": datetime.now().strftime("%b %dth, %Y - %H:%M hrs"),
        "photo": photos[idx],
    }
    for idx in range(len(names))
]


def list_posts(request):
    """List existing posts."""
    return render(request, "feed.html", {"posts": posts})
