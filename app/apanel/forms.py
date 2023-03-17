from django import forms
from .models import FileUpload

class fileForm(forms.ModelForm):

   class Meta:
      model = FileUpload
      fields = ['title','uploadedFile']