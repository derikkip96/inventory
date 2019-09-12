from django.shortcuts import render
from django.views.generic import FormView
from customer.forms import SupplierForm
from django.http import HttpResponseRedirect

class SupplierView(FormView):
    form_class = SupplierForm
    template_name='supplier/supplier_add.html'
    initial = {'key':'value'}
    def get(self,request,*args,**kwargs):
        supform = self.form_class(initial=self.initial)
        return render(request,self.template_name, {'supform':supform})
    def post(self,request,*args,**kwargs):
        supform = self.form_class(request.POST,files=request.FILES)
        if supform.is_valid():
            supform.save()
            return HttpResponseRedirect('/')
        return render(request,self.template_name,{'supform':supform})


# Create your views here.
