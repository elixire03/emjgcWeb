from django import forms

class ContactUs(forms.Form):
    name = forms.CharField(max_length=50,min_length=2)
    email = forms.EmailField()
    subject = forms.CharField(max_length=50, min_length=2)
    message = forms.CharField(widget=forms.Textarea)
    