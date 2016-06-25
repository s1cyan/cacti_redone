from django import forms


class LoginForm(forms.ModelForm):
    username_email = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)

    class Meta:
        fields = ('username','password')


class SearchForm(forms.Form):
    search_bar_input = forms.CharField(max_length=64)