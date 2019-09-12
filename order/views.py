from django.shortcuts import render,HttpResponseRedirect
from order.forms import SalesTypeForm,SalesPriceForm
from django.views.generic import ListView,FormView
from order.models import SalesType

# Create your views here.

class SalesTypeView(ListView):
    form_class = SalesTypeForm
    template_name = 'settings/sales_type.html'
    initial = {'key': 'value'}
    model = SalesType

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['salesform']= self.form_class(initial=self.initial)
        context['sales_type'] = SalesType.objects.all()
        return context
    def post(self, request, *args, **kwargs):
        salesform = self.form_class(request.POST)
        if salesform.is_valid():
            salesform.save()
            return HttpResponseRedirect('sales_list')

        return render(request, self.template_name, {'salesform': salesform})

