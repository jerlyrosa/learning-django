from nturl2path import url2pathname


from django.urls import path
from . import views

urlpatterns =[
    path('',views.index),
    path('about/',views.about),
    path('hello/<str:username>',views.saludar),
    path('projects/',views.projects),
    path('task/<int:id>',views.tasks),
]