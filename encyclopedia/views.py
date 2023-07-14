from django.shortcuts import render

from . import util
import markdown

def markdown_md_to_html(entry):
    markdowner = markdown.Markdown()
    return markdowner.convert(util.get_entry(entry))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, title):
    return render(request, "encyclopedia/title.html", {
        "title": title.capitalize(),
        "entry_text":  markdown_md_to_html(title)
    })

def search(request):
    if request.method == "POST":
        search_title = request.POST["q"]
        if search_title.lower() in map(str.lower, util.list_entries()):
            return render(request,  "encyclopedia/title.html", {
                "title": search_title.capitalize(),
                "entry_text":  markdown_md_to_html(search_title)
            })
        else:
            return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
         })
    else:
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
         })
    
def create_page(request):
    return render(request, "encyclopedia/newpage.html")
        # util.save_entry(title, content)