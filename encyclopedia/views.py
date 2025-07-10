from django.shortcuts import render

#entries files are in md file type, and need to be converted into html:
#using markdown.converter() function from the markdown library
import markdown

import random #for step 7: random page

from . import util

#step 1: Markdown to HTML Conversion: converting file types to readable
def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)
    

def index(request):
    '''
    this is how util funcions work: 
    entries = util.list_entries() #returns a list of all entries available
    css_file = util.get_entry("CSS") #checking if css file exists
    coffee = util.get_entry("coffee") #returns none because this entry doesn't exist
    '''
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

#step 2: Entry Page: if file doesn't exist in entries, display error page
def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "message": "this entry does not exist"
        }) 
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })#content of entry file

#step 4: Search: 
def search(request): 
    if request.method == "POST":
        entry_search = request.POST['q'] #grab data from form input
        html_content = convert_md_to_html(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": entry_search,
                "content": html_content
            })
        else: #second part, if the search deosn't exist, so we choose the closes result to searched str
            #check if searched-str is part of our html-contnet str name
            allEntries = util.list_entries()
            recommendations = []
            for entry in allEntries:
                if entry_search.lower() in entry.lower(): #all lowercase, easier search
                    recommendations.append(entry)
            return render(request, "encyclopedia/search.html", {
                "recommendation": recommendations
            })
        

#step 5: New Page
def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html") 
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExist = util.get_entry(title)
        if titleExist is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "entry page already exists"
            })
        else:
            util.save_entry(title, content)
            html_content = convert_md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content
            })

#step 6: edit page
def edit(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })
    

def save_edit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_md_to_html(title)
        return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content
            })
    
#step 7: random page
def random(request):
    allEntries = util.list_entries()
    rand_entry = random.choice(allEntries)
    html_content = convert_md_to_html(rand_entry)
    return render(request, "encyclopedia/entry.html", {
                "title": rand_entry,
                "content": html_content
            })

# 47:30 / 57:30
