from django import forms




class ContacOthers (forms.Form):

    full_name = forms.CharField (max_length=100, widget=forms.TextInput(attrs={'class':'FnT', 'placeholder':'full_name' }))


    email = forms.CharField (max_length=100, widget =forms.EmailInput(attrs={'class':'GT', 'placeholder':'email'}))

    message = forms.CharField(max_length=500, widget =forms.Textarea(attrs={'class':'textbox', 'placeholder':'live message'}))
    blogid =forms.IntegerField ()

class like_form (forms.Form):
    like =forms.IntegerField ()
    mess_id =forms.IntegerField ()
