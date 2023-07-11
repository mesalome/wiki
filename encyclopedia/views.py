from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, title):
    return render(request, "encyclopedia/title.html", {
        "title": title.capitalize(),
        "entry_text": util.get_entry(title)
    })