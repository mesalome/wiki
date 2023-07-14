from turtle import title
from django.shortcuts import render
from django.core.files.storage import default_storage

from . import util
import markdown
from random import choice

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
            all_entries = util.list_entries()
            desired_entries = []
            for i in range(len(all_entries)):
                if search_title in all_entries[i]:
                    desired_entries.append(all_entries[i])

            return render(request, "encyclopedia/index.html", {
        "entries": desired_entries
         })
    else:
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
         })
    
def create_page(request):
    return render(request, "encyclopedia/newpage.html")

def add_page(request):
    if request.method == "POST":
        added_title = request.POST['title'].capitalize()
        if added_title.lower() in map(str.lower, util.list_entries()):
            return render(request, "encyclopedia/index.html", {
                "already_existed_title" : added_title,
                "entries" : util.list_entries()
            })
        else:
            added_content = request.POST["content"]
            if len(added_content.strip()) == 0:
                return render(request, "encyclopedia/index.html", {
                    "title" : added_title,
                    "content" : "no_content",
                    "entries" : util.list_entries()
                })
            else:
                util.save_entry(added_title, added_content)
        
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def random(request):
    entries = util.list_entries()
    entry = choice(entries)
    return render (request, "encyclopedia/title.html", {
        "title": entry,
        "entry_text":  markdown_md_to_html(entry)
    })

def edit(request):
    if request.method == "POST":
        edit_title = request.POST['soon_to_be_eddited_page']
        return render(request, "encyclopedia/edit.html", 
                    {
                        "title": edit_title,
                        "content": util.get_entry(edit_title)
                    })
    return render(request, "encyclopedia/index.html", 
                    {
                        "entries": util.list_entries()
                    })

def save(request):
    if request.method == "POST":
        title = request.POST['title_of_edited_page']
        new_content = request.POST['content_edit']
        try:
            with default_storage.open(f"entries/{title}.md", "w") as f:
                f.write(new_content)
        except Exception as e:
            print(f"An error occurred while writing to file: {e}")
        return render(request, "encyclopedia/title.html",
                      {
                          "title": title,
                          "entry_text": markdown_md_to_html(title)
                      }
        )
