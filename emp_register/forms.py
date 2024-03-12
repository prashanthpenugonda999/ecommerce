from django import forms


class info_forms(forms.Form):
    name=forms.CharField()
    pwd=forms.CharField()