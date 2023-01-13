from django.shortcuts import render
from django.http import HttpResponse, FileResponse, Http404

def index(request):
    try:
        return render(request, 'website/index.html')
    
    except FileNotFoundError:
        raise Http404

def resume_pdf(request):
    try:
        return FileResponse(open('website/static/website/assets/pdf/resume.pdf', 'rb'), content_type='application/pdf')
    
    except FileNotFoundError:
        raise Http404()