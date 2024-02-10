from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', home),
    # path('category/',category),
     path('category', category),
     path('about', about),
     path('latest_news', latest_news),
     path('contact', contact),
    path('post/<id>', postiddetail),
    path('postmain/<id>', post),
    path('weekmain/<id>', weekpost),
    path('newnews/<id>', newnews),
    path('sidenews/<id>', sidecont),
   
]
