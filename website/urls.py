from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), 
    path('resume/', views.resume_pdf, name='resume'),
    path('python3/', views.python3_pdf, name='python3'),
    path('javascript/', views.javascript_pdf, name='javascript'),
    path('html/', views.html_pdf, name='html'),
    path('css/', views.css_pdf, name='css'),
    path('gitgithub/', views.gitgithub_pdf, name='gitgithub'),
]