from django import forms
from .models import Services,Service_category,Page

class NewTopicForm(forms.ModelForm):
    #category = forms.CharField(widget=forms.Textarea(), max_length=400)
    class Meta:
        model = Services
        fields = ['name','category']

class NewTopicForm2(forms.ModelForm):
	desc = forms.CharField(widget=forms.Textarea())
	class Meta:
		model =  Service_category
		fields = ['namee','location','Address','desc','price','position','pref_time','handle']


class NewTopicForm3(forms.ModelForm):
	Review = forms.CharField(widget=forms.Textarea())
	class Meta:
		model =  Page
		fields = ['Review']

# class verifyform(forms.ModelForm):
# 	class Meta:
# 		model = verify
# 		fields = ['aadhar']