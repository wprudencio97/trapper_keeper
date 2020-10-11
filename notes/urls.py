from django.urls import path
from .views import NoteListView
from . import views

urlpatterns = [
    #path('', NoteListView.as_view(), name='index')
    path('', views.index, name='index'),
]