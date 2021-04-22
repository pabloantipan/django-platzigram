# from django.shortcuts import render
"""Posts app views."""
# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

names = ["absolutepositive", "patovillarroel", "calfu23"]
users = ["Pablo Antipan", "Pato Villarroel", "Andres Calfulaf"]
pictures = [1036, 903, 1076]

# punto = [(names[idx], users[idx]) for idx in range(len(names))]

posts = [
    {
        "name": names[idx],
        "user": users[idx],
        "timestamp": datetime.now().strftime("%b %dth, %Y - %H:%M hrs"),
        "picture": f"https://picsum.photos/200/200/?image={pictures[idx]}",
    }
    for idx in range(len(names))
]


def list_posts(request):
    """List existing posts."""
    content = []
    for post in posts:
        content.append(
            """
            <p><strong>{name}</strong></p>
            <p><small>{name} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
            """.format(
                **post
            )
        )
    return HttpResponse("<br>".join(content))
