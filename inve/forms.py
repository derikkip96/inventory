from django import forms
from inve.models import ItemUnit,Category,Item,StockMaster,Tax
from django.forms import ModelChoiceField


class ItemForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset = Category.objects.all(), empty_label="please select unit",to_field_name="id",widget=forms.Select(
                attrs={'class': 'form-control valdation_check'}))
    unit = forms.ModelChoiceField(queryset=ItemUnit.objects.all(), empty_label="please select unit",
                                        to_field_name="id", widget=forms.Select(
            attrs={'class': 'form-control valdation_check'}))
    tax = forms.ModelChoiceField(queryset=Tax.objects.all(), empty_label="please select unit",
                                        to_field_name="id", widget=forms.Select(
            attrs={'class': 'form-control valdation_check'}))
    long_description = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20, 'class':'form-control valdation_check'}))
    image = forms.ImageField()

    class Meta:
        model=Item
        fields = ['description','stock_id']
        widgets = {
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Name',
                    'class': 'form-control valdation_check'
                }
            ),
            'stock_id': forms.TextInput(
                attrs={
                    'placeholder': 'Abbr',
                    'class': 'form-control valdation_check'
                }
            ),
        }

class CategoryForm(forms.ModelForm):
    dflt_units = forms.ModelChoiceField(queryset = ItemUnit.objects.all(), empty_label="please select unit",to_field_name="id",widget=forms.Select(
                attrs={'class': 'form-control valdation_check'}))

    class ItemUnitChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return obj.name

    class Meta:
        model= Category
        fields = ['description','dflt_units']
        widgets = {
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Name',
                    'class': 'form-control valdation_check'
                }
            ),
        }

class UnitForm(forms.ModelForm):

    class Meta:
        model= ItemUnit
        fields = ['name','abbr']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Name',
                    'class': 'form-control valdation_check'
                }
            ),
            'abbr': forms.TextInput(
                attrs={
                    'placeholder': 'Abbr',
                    'class': 'form-control valdation_check'
                }
            ),
        }

class StockForm(forms.ModelForm):
    class Meta:
        model = StockMaster
        fields = ['category']

class TaxForm(forms.ModelForm):
    class Meta:
        model = Tax
        fields = ['name','tax_rate']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Name',
                    'class': 'form-control valdation_check'
                }
            ),
            'tax_rate': forms.TextInput(
                attrs={
                    'placeholder': 'tax rate',
                    'class': 'form-control valdation_check'
                }
            ),
        }


