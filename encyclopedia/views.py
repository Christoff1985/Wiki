from django.shortcuts import render

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def content(request, page):
    return render(request, "encyclopedia/content.html", {
        "title": page.upper(),
        "entry": util.get_entry(page)
    })

