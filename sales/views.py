from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Sales
from django.contrib.auth.mixins import LoginRequiredMixin
from sales.forms import SalesForm
from django.views.generic import DetailView, ListView
import datetime
from django.db.models import Sum


class SalesCreateView(LoginRequiredMixin, CreateView):
    model = Sales
    template_name = 'sales/form.html'
    form_class = SalesForm

    def form_valid(self, form):
        form.instance.author_id = self.request.user
        return super().form_valid(form)

class SalesDetailView(LoginRequiredMixin, DetailView):
    model = Sales
    template_name = 'sales/detail.html'

class SalesListView(LoginRequiredMixin, ListView):
    queryset = Sales.objects.all()
    template_name = 'sales/list.html'
    context_object_name = 'sales'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['month_sales'] = Sales.objects.filter(date__month=datetime.datetime.now().month).aggregate(Sum('amount'))['amount__sum']
        context['total_sales'] = Sales.objects.aggregate(Sum('amount'))['amount__sum']
        return context


