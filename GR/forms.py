from django import forms
from .models import Intervention,Favorite
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FavoriteForm(forms.ModelForm):

    class Meta:
        model = Favorite
        fields = ('fav',)
