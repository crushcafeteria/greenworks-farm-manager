from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Sales
from django.contrib.auth.mixins import LoginRequiredMixin
from sales.forms import SalesForm
from django.views.generic import DetailView, ListView
import datetime
from django.db.models import Sum, Q
from sales.models import Product
from django.contrib import messages
from django.shortcuts import redirect


class SalesListView(LoginRequiredMixin, ListView):
    template_name = 'sales/list.html'
    context_object_name = 'sales'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        month = datetime.datetime.now().month
        context['month_sales'] = Sales.objects.filter(date__month=month).aggregate(Sum('amount'))['amount__sum']
        context['total_sales'] = Sales.objects.aggregate(Sum('amount'))['amount__sum']
        context['q'] = self.request.GET.get('q', '')
        context['products'] = Product.objects.all()

        return context

    def get_queryset(self):
        queryset = Sales.objects.all()

        # Search keywords
        if self.request.GET.get('q'):
            q = self.request.GET.get('q')
            queryset = queryset.filter(Q(description__icontains=q))

        # Filter by validation
        if self.request.GET.get('valid'):
            queryset = queryset.filter(valid__exact=self.request.GET.get('valid'))

        # Filter by product
        if self.request.GET.get('product'):
            queryset = queryset.filter(product=self.request.GET.get('product'))

        queryset = queryset.order_by('-date')
        return queryset


class SalesCreateView(LoginRequiredMixin, CreateView):
    model = Sales
    template_name = 'sales/form.html'
    form_class = SalesForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SalesDetailView(LoginRequiredMixin, DetailView):
    model = Sales
    template_name = 'sales/view.html'
    context_object_name = 'sale'


class SalesUpdateView(UpdateView):
    model = Sales
    form_class = SalesForm
    template_name = 'sales/form.html'
    context_object_name = 'sale'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['editing'] = True
        return context

    def get_initial(self):
        pass
        # initial = super(SalesUpdateView, self).get_initial()
        # initial['product'] = self.sale.product
        # return initial


class SalesValidate(UpdateView):
    template_name = 'sales/validate.html'
    context_object_name = 'sale'
    model = Sales
    fields = ['product', 'amount', 'date', 'quantity', 'description']

    # Form will always be invalid. Intercept request here to validate expense
    def form_invalid(self, form):
        pk = self.kwargs['pk']
        sale = Sales.objects.filter(pk=pk)
        sale.update(valid='YES')
        messages.success(self.request, 'You have validated this sale')
        return redirect('/sales?valid=NO')


class SalesDeleteView(DeleteView):
    model = Sales
    success_url = '/sales'
