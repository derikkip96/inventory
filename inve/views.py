from django.shortcuts import render
from django.views.generic import FormView
from .forms import CategoryForm,UnitForm,ItemForm,TaxForm,StockMaster
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def showme(request):
    return render(request,'tax/create.html')

class CreateCategory(FormView):
    form_class = CategoryForm
    template_name = 'categories/create.html'
    initial = {'key': 'value'}

    def get(self,request, *args, **kwargs):
        form =self.form_class(initial=self.initial)
        return render(request,self.template_name, {'form':form})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})


class CreateUnit(FormView):
    form_class = UnitForm
    template_name = 'unit/unit_add.html'
    initial = {'key': 'value'}
    def get(self,request, *args, **kwargs):
        unitform =self.form_class(initial=self.initial)
        return render(request,self.template_name, {'unitform':unitform})

    def post(self, request, *args, **kwargs):
        unitform = self.form_class(request.POST)
        if unitform.is_valid():
            unitform.save()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'unitform': unitform})
class Item(FormView):
    form_class = ItemForm
    template_name='item/create.html'
    initial = {'key':'value'}
    def get(self,request,*args,**kwargs):
        itemform = self.form_class(initial=self.initial)
        return render(request,self.template_name, {'itemform':itemform})
    def post(self,request,*args,**kwargs):
        itemform = self.form_class(request.POST)
        if itemform.is_valid():
            itemform.save()
            StockMaster.objects.create(
                stock_id = request.POST.get('stock_id'),
                category = request.POST.get('category'),
                description = request.POST.get('description'),
                long_description = request.POST.get('long_description'),
                units = request.POST.get('unit'),
                tax_type = request.POST.get('tax')
            )
            return HttpResponseRedirect('/')
        return render(request,self.template_name,{'itemform':itemform})


class TaxCreate(FormView):
    form_class = TaxForm
    template_name = 'tax/create.html'
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        taxform = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'taxform': taxform})

    def post(self, request, *args, **kwargs):
        taxform = self.form_class(request.POST)
        if taxform.is_valid():
            taxform.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'taxform': taxform})





