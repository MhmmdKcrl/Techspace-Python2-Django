from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(attrs={
            "placeholder": "Username",
            "class": "form-control",
        })
    )
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": "form-control",
        })
    )


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget = forms.PasswordInput(attrs={
            "placeholder": "Confirm Password",
            "class": "form-control",
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            "first_name": forms.TextInput(attrs={
                "placeholder": "First Name",
                "class": "form-control",
                }),
            "last_name": forms.TextInput(attrs={
                "placeholder": "Last Name",
                "class": "form-control",
                }),
            "username": forms.TextInput(attrs={
                "placeholder": "Username",
                "class": "form-control",
                }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Email",
                "class": "form-control",
                }),
            "password": forms.PasswordInput(attrs={
                "placeholder": "Password",
                "class": "form-control",
                }),
        }


    def save(self, commit):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.is_active = False
        user.save()
        return user
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data