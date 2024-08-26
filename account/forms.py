from django import forms
from django.contrib.auth.models import User

class Registration(forms.ModelForm):
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=255, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name' , 'email' , 'password' , 'password2')

    def clean_password(self):
        cd = self.cleaned_data
        password = cd.get('password')
        password2 = cd.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError('Password don\'t Match')
        return password