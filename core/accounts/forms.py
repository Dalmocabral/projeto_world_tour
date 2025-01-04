from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms



class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Adicionando placeholders
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last Name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'E-mail Address'})
        self.fields['username_IFC'].widget.attrs.update({'placeholder': 'Username IFC'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})
        self.fields['country'].widget.attrs.update({'placeholder': 'Country'})

    

    def clean(self):
        cleaned_data = super().clean()

        for field_name, field_value in cleaned_data.items():
            if isinstance(field_value, str):
                if field_name in ['first_name', 'last_name']:
                    cleaned_data[field_name] = field_value.capitalize()

        return cleaned_data

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username_IFC', 'email', 'country', 'password1', 'password2']
