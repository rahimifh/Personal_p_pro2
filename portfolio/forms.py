from django import forms




class ContactUS (forms.Form):
    full_name = forms.CharField (max_length=100, widget=forms.TextInput(attrs={'class':'FnT', 'placeholder':'full_name' }))
    email = forms.CharField (max_length=100, widget =forms.EmailInput(attrs={'class':'GT', 'placeholder':'email'}))
    phone = forms.CharField (max_length=15, widget=forms.TextInput(attrs={'class':'LnT', 'placeholder':'Phone' }))
    message = forms.CharField(max_length=1000, widget =forms.Textarea(attrs={'class':'textbox', 'placeholder':'leave message'}))
