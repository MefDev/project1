from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.files.storage import default_storage
from . import util
import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def obtain_entry(request, name):
    if util.get_entry(name) != None:
        entry_html = convert_to_html(name)
        # render the appropriate entry page as well as send the two vars to the 'entry html page'.
        return render(request, "encyclopedia/entry.html", {
            "render_entry": entry_html, 
            "title": name.upper()
        })
    else:
        return HttpResponse("<h1>The requested page was not found.<h1>")
    

def convert_to_html(entry_name):
    """
    Convert md files to html
    """
    if util.get_entry(entry_name) is not None:
         file = default_storage.open(f"entries/{entry_name}.md", "r")
         md= file.read()
         html = markdown.markdown(md)
         return html
    else:
        return "No such file"
   
 
