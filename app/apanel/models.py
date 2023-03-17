from django.db import models
from django import forms

class FileUpload(models.Model):
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "files/")