from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
   path('',views.index,name="homepage"),
   path('about',views.about,name="about"),
   path('contact',views.contact,name="contact"),
   path('post/<int:id>',views.post,name="post"),
   path('all',views.all,name='all')
]
