from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'phone']
        labels = {
            'first_name': 'Voornaam',
            'last_name': 'Achternaam',
            'phone': 'Telefoonnummer',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'field-input',
                'autocomplete': 'given-name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'field-input',
                'autocomplete': 'family-name',
            }),
            'phone': forms.TelInput(attrs={
                'class': 'field-input',
                'autocomplete': 'tel',
            }),
        }