from django import forms
from django.utils.translation import gettext_lazy as _

from core.models import Contact


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name' : forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": _('Your name')
            }),
            'email' : forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": 'Your email'
            }),
            'subject' : forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": 'subject'
            }),
            'message': forms.Textarea(attrs={
                "class" : "form-control",
                "placeholder": 'Message',
                'cols': 30,
                'rows': 7
                
            })
        }
    
    def clean(self):
        cleaned_data = self.cleaned_data

        if self.data['name'] == 'admin':
            raise forms.ValidationError("You have failed validation!")
        else:
            return cleaned_data 
        

    def clean_email(self):
        # value = self.cleaned_data.get("email")
        value = self.cleaned_data['email']
        if not value.endswith(".com"):
            raise forms.ValidationError("Mail must be .com!")
        return value
    
    def clean_name(self):
        value = self.cleaned_data['name']
        value = value.upper()
        return value

