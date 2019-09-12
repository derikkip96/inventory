from django import forms
from customer.models import Supplier


class SupplierForm(forms.ModelForm):
    email = forms.EmailField(help_text='A valid email address, please.')
    email.widget.attrs.update({'class': 'form-control valdation_check'})
    class Meta:
        model = Supplier
        fields = ['name','email','address','contact','city','state','country','zipcode']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Name',
                    'class': 'form-control valdation_check'
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'placeholder': 'address',
                    'class': 'form-control valdation_check'
                }
            ),
            'contact': forms.TextInput(
                attrs={
                    'placeholder': 'contact',
                    'class': 'form-control valdation_check'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'placeholder': 'city',
                    'class': 'form-control valdation_check'
                }
            ),
            'state': forms.TextInput(
                attrs={
                    'placeholder': 'state',
                    'class': 'form-control valdation_check'
                }
            ),
            'country': forms.TextInput(
                attrs={
                    'placeholder': 'country',
                    'class': 'form-control valdation_check'
                }
            ),
            'zipcode': forms.TextInput(
                attrs={
                    'placeholder': 'zipcode',
                    'class': 'form-control valdation_check'
                }
            ),
        }