from django import forms
from .models import *

class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
        
    confirm_password = forms.CharField(
        widget=forms.PasswordInput()
    )

    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('confirm_password', 'Password does not match.')
        
        return cleaned_data
    
    # def save(self):
    #     user = super().save()
    #     user.set_password(self.cleaned_data['password'])
    #     user.save()
    #     return user