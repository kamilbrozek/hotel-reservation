from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(
        label= "Subject",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email_from = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=True
        )