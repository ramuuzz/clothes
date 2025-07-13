from django import forms
from .models import shirts, pants, jackets
class ShirtForm(forms.ModelForm):
    class Meta:
        model = shirts
        fields = ['title', 'image']
class PantsForm(forms.ModelForm):
    class Meta:
        model = pants
        fields = ['title', 'image']
class JacketForm(forms.ModelForm):
    class Meta:
        model = jackets
        fields = ['title', 'image']                        