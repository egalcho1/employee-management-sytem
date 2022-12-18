from django import forms 
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class Emp(forms.ModelForm):
    class Meta:
        model=Employe
        fields=['username','fname','lname']
class Registrf(UserCreationForm):
      class Meta:
          model=User
          fields=['username','email','password1','password2']
          

