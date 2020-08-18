from django import forms


class services_mess_form (forms.Form):

    full_name = forms.CharField (max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'full_name' }))
    email = forms.CharField (max_length=100, widget =forms.EmailInput(attrs={'class':'form-control', 'placeholder':'email'}))
    message = forms.CharField(max_length=500, widget =forms.Textarea(attrs={'class':'form-control', 'placeholder':'live message'}))
    blogid =forms.IntegerField ()


class like_form (forms.Form):
    like =forms.IntegerField ()
    mess_id =forms.IntegerField ()
