from django import forms
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class ProfileRegistrationForm(UserCreationForm):
    username = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}), label="Password")

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit: 
            user.save()

        profile = Profile(user = user, first_name = self.cleaned_data['first_name'],
                          last_name = self.cleaned_data['last_name'])

        if commit:
            profile.save()
        
        return profile
    
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise forms.ValidationError("User already exists")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise forms.ValidationError("Email already used")
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords doesnt match")
        return password2
    
        


class ProfileLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
    

