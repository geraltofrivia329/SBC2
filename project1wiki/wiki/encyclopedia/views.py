import markdown2
from django.shortcuts import render
from django import forms
from . import util
from markdown2 import Markdown

class TitleForm(forms.Form):
    title = forms.CharField(label = "Title", max_length = 100)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    markdowner = Markdown()
    entryPage = util.get_entry(entry)
    if entryPage is None:
        return render(request, "encyclopedia/nonExistingEntry.html", {
        "entryTitle": entry
        })
    else:
        return render(request, "encyclopedia/entry.html", {
        "entry": markdowner.convert(entryPage),
        "entryTitle": entry
        })
#def search(request):
    #p = util.get.entry(title)
    #q = TitleForm(forms.Form)

    #if request.method == 'GET':
        #form = request.GET.get('q')
        #if form.is_valid():
            #return HttpResponseRedirect(p)
    #else:
        #form = TitleForm()

    #return render(request, 'encyclopedia/layout.html', {'form': form})

def search (request):
    entries = util.list_entries()
    query = request.GET.get("q", "")
    if query in entries:
        return redirect(wiki, query)
    results = [entry for entry in entries if query.lower() in entry.lower()]
    return render(request, "encyclopedia/layout.html", {
        "entries": results,
    })
