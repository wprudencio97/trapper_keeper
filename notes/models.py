from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Note(models.Model):
    note_title = models.CharField(max_length=50)
    #note_content = models.TextField()
    note_content = RichTextUploadingField(blank=True, null=True)
    date_created = models.DateField(default=timezone.now)

    def __str__(self):
        return self.note_title

    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk':self.pk})