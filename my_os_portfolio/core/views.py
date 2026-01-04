from django.shortcuts import render
from .models import Project, Document

def index(request):

    # 1. Fetch all projects for the 'Projects' window
    projects = Project.objects.all()

    # 2. Fetch the specific document for VS Code
    # We look for a document with the slug 'readme'
    readme = Document.objects.filter(slug='readme').first()

    # 3. (Optional) Fetch all documents if you want a file explorer inside VS Code
    all_docs = Document.objects.all()

    context = {
        'projects': projects,
        'readme': readme,
        'all_docs': all_docs,
    }

    return render(request, 'desktop.html', context)
