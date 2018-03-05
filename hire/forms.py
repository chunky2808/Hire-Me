from django import forms
from .models import Services,Service_category

class NewTopicForm(forms.ModelForm):
    #category = forms.CharField(widget=forms.Textarea(), max_length=400)
    class Meta:
        model = Services
        fields = ['name','category']

class NewTopicForm2(forms.ModelForm):
	desc = forms.CharField(widget=forms.Textarea())
	class Meta:
		model =  Service_category
		fields = ['namee','location','desc','price']
