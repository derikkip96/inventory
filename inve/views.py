from django.shortcuts import render,get_object_or_404
from django.views.generic import FormView,UpdateView,ListView,TemplateView
from .forms import CategoryForm,UnitForm,ItemForm,TaxForm,StockMaster,LocationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormMixin
from inve.models import Tax,Location,Category,ItemUnit
from django.urls import reverse
from order.forms import SalesPriceForm

# Create your views here.
def showme(request):
    return render(request,'item/list.html')

class CreateCategory(ListView):
    form_class = CategoryForm
    template_name = 'settings/category.html'
    initial = {'key': 'value'}
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form']= self.form_class(initial=self.initial)
        context['categories'] = Category.objects.all()
        return context
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('inve:list'))

        return render(request, self.template_name, {'form': form})


class CreateUnit(FormView):
    form_class = UnitForm
    template_name = 'settings/unit.html'
    initial = {'key': 'value'}
    model = ItemUnit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unitform']= self.form_class(initial=self.initial)
        context['units'] = ItemUnit.objects.all()
        return context
    def post(self, request, *args, **kwargs):
        unitform = self.form_class(request.POST)
        if unitform.is_valid():
            unitform.save()
            return HttpResponseRedirect(reverse('inve:unit'))

        return render(request, self.template_name, {'unitform': unitform})
class Item(FormView):
    form_class = ItemForm
    template_name='item/create.html'
    initial = {'key':'value'}
    def get(self,request,*args,**kwargs):
        itemform = self.form_class(initial=self.initial)
        return render(request,self.template_name, {'itemform':itemform})
    def post(self,request,*args,**kwargs):
        itemform = self.form_class(request.POST,files=request.FILES)
        if itemform.is_valid():
            category = itemform.cleaned_data['category']
            tax_type = itemform.cleaned_data['tax']
            units = itemform.cleaned_data['unit']
            itemform.save()
            StockMaster.objects.get_or_create(
                stock_id = request.POST.get('stock_id'),
                category = category,
                description = request.POST.get('description'),
                long_description = request.POST.get('long_description'),
                units = units,
                tax_type = tax_type
            )
            return HttpResponseRedirect('/')
        return render(request,self.template_name,{'itemform':itemform})


class TaxUpdateView(UpdateView):
    model = Tax
    form_class = TaxForm
    template_name = 'tax/edit_tax.html'

    def get_object(self, *args, **kwargs):
        obj =get_object_or_404(Tax, pk=self.kwargs['pk'])
        return obj

    def form_valid(self,form):
        tax=form.save(commit=False)



class FinanceView(ListView, FormMixin):
    form_class = TaxForm
    initial = {'key': 'value'}
    model = Tax
    template_name = 'tax/list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['taxform']= self.form_class(initial=self.initial)
        context['taxes'] = Tax.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        taxform = self.form_class(request.POST)
        if taxform.is_valid():
            taxform.save()
            return HttpResponseRedirect(reverse('inve:setting_finace'))
        return render(request, self.template_name, {'taxform': taxform})

class LocationView(ListView,FormMixin):
    form_class = LocationForm
    template_name = 'settings/locations.html'
    initial = {'key': 'value'}
    model = Location
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['location_form'] = self.form_class(initial=self.initial)
        context['locations'] = Location.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        location_form = self.form_class(request.POST)
        if location_form.is_valid():
            location_form.save()
            return HttpResponseRedirect(reverse('inve:location'))

        return render(request, self.template_name, {'location_form': location_form})



