from django import forms
from .models import Services

class NewTopicForm(forms.ModelForm):
    #category = forms.CharField(widget=forms.Textarea(), max_length=400)

    class Meta:
        model = Services
        fields = ['name','category']