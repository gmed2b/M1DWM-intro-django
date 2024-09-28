from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
      "placeholder": "Username",
      "class": "px-5 py-3 rounded-md bg-martinique-950"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
      "placeholder": "Enter your password",
      "class": "px-5 py-3 rounded-md bg-martinique-950"
    }))


class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
      "placeholder": "First name",
      "class": "px-5 py-3 rounded-md bg-martinique-950"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
      "placeholder": "Last name",
      "class": "px-5 py-3 rounded-md bg-martinique-950"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
      "placeholder": "Email address",
      "class": "px-5 py-3 rounded-md bg-martinique-950"
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
      "placeholder": "Username",
      "class": "px-5 py-3 rounded-md bg-martinique-950"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
      "placeholder": "Enter your password",
      "class": "px-5 py-3 rounded-md bg-martinique-950"
    }))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={
      "placeholder": "Confirm your password",
      "class": "px-5 py-3 rounded-md bg-martinique-950"
    }))