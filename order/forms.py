from django import forms
from order.models import Debtor, SalesType,SalesPrice

class SalesTypeForm(forms.ModelForm):
    CHOICES = (
        (0, 'No'),
        (1, 'Yes')
    )    
    tax = forms.CharField(
        max_length=9,
        widget=forms.Select(choices=CHOICES,
        attrs={'class': 'form-control valdation_check'}
        ),
    )
    default = forms.CharField(
        max_length=9,
        widget=forms.Select(choices=CHOICES,
        attrs={'class': 'form-control valdation_check'}
        ),
    )
    class Meta:
        model = SalesType
        fields = ['types','tax','default']
        widgets = {
            'types': forms.TextInput(
                attrs={
                    'placeholder': 'tax type',
                    'class': 'form-control valdation_check'
                }
            ),
        }

class SalesPriceForm(forms.ModelForm):
    sales_type = forms.ModelChoiceField(queryset=SalesType.objects.all(), empty_label="please select",
                                      to_field_name="id", widget=forms.Select(
            attrs={'class': 'form-control valdation_check'}))
    class Meta:
        model = SalesPrice
        fields = ['sales_type','price','curr_abrev']
        widgets = {
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'price',
                    'class': 'form-control valdation_check'
                }
            ),
            'curr_abrev': forms.TextInput(
                attrs={
                    'placeholder': 'currency',
                    'class': 'form-control valdation_check'
                }
            ),
        }