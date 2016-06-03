from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)

    class Meta:
        model = CustomUser
        fields = ["username", "email"]


class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = CustomUser
        fields = '__all__'


class LoginForm(forms.Form):
    user_exist = False
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            CustomUser.objects.get(email=email)
            self.user_exist = True
        except CustomUser.DoesNotExist:
            raise forms.ValidationError("Are you sure you are registered? We cannot find this user.")
        return email

    def clean_password(self):
        if self.user_exist:
            email = self.cleaned_data.get("email")
            user = CustomUser.objects.get(email=email)
            password = self.cleaned_data.get("password")
            if user.check_password(password):
                return password
            else:
                raise forms.ValidationError("Invalid Password")