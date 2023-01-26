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
    
def python3_pdf(request):
    try:
        return FileResponse(open('website/static/website/assets/pdf/Codecademy_Python3.pdf', 'rb'), content_type='application/pdf')
    
    except FileNotFoundError:
        raise Http404()

def javascript_pdf(request):
    try:
        return FileResponse(open('website/static/website/assets/pdf/Codecademy_IntermediateJavaScript.pdf', 'rb'), content_type='application/pdf')
    
    except FileNotFoundError:
        raise Http404()
    
def html_pdf(request):
    try:
        return FileResponse(open('website/static/website/assets/pdf/Codecademy_HTML.pdf', 'rb'), content_type='application/pdf')
    
    except FileNotFoundError:
        raise Http404()
    
def css_pdf(request):
    try:
        return FileResponse(open('website/static/website/assets/pdf/Codecademy_CSS.pdf', 'rb'), content_type='application/pdf')
    
    except FileNotFoundError:
        raise Http404()
    
def gitgithub_pdf(request):
    try:
        return FileResponse(open('website/static/website/assets/pdf/Codecademy_Git&GitHub.pdf', 'rb'), content_type='application/pdf')
    
    except FileNotFoundError:
        raise Http404()