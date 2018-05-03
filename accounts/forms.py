from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Customer, User,Service

class CustomerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','position']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        return user


class ServiceSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','position','aadhar_no','aadhar_file','pref_time']

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        print(user)
        user.is_service = True
        user.save()
        service = Service.objects.create(user=user)
        return user        
