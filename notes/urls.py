from django.urls import path
from .views import NoteDetailView, NoteUpdateView, NoteDeleteView
from . import views

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('note/update/<int:pk>', NoteUpdateView.as_view(), name='note-update'),
    path('note/detail/<int:pk>', NoteDetailView.as_view(), name='note-detail'),
    path('note/delete/<int:pk>', NoteDeleteView.as_view(), name='note-delete'),
    path('', views.index, name='index'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)