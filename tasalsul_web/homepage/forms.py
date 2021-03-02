from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    from_email = forms.EmailField(required=True)
    phone_number = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea, required=True)