from django.urls import path
from .views import NoteDetailView, NoteUpdateView, NoteDeleteView
from . import views

urlpatterns = [
    path('note/update/<int:pk>', NoteUpdateView.as_view(), name='note-update'),
    path('note/detail/<int:pk>', NoteDetailView.as_view(), name='note-detail'),
    path('note/delete/<int:pk>', NoteDeleteView.as_view(), name='note-delete'),
    path('', views.index, name='index'),
]