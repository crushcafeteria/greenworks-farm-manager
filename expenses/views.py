from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from expenses.models import Expenses
from django.contrib.auth.mixins import LoginRequiredMixin
from expenses.forms import ExpenseForm
import datetime
from django.db.models import Sum, Q
from django.core.paginator import Paginator


class ExpensesListView(LoginRequiredMixin, ListView):
    template_name = 'expenses/list.html'
    context_object_name = 'expenses'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        month = datetime.datetime.now().month
        context['month_expenses'] = 'Ksh ' + str(
            Expenses.objects.filter(when__month=month).aggregate(Sum('amount'))['amount__sum'])
        context['total_expenses'] = 'Ksh ' + str(Expenses.objects.aggregate(Sum('amount'))['amount__sum'])
        context['q'] = self.request.GET.get('q', '')
        return context

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        if q is not None:
            q = self.request.GET['q']
            queryset = Expenses.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
        else:
            queryset = Expenses.objects.all()

        queryset = queryset.order_by('-when')
        return queryset


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expenses
    template_name = 'expenses/form.html'
    form_class = ExpenseForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ExpenseDetailView(LoginRequiredMixin, DetailView):
    model = Expenses
    template_name = 'expenses/view.html'
    context_object_name = 'expense'


class ExpensesDeleteView(DeleteView):
    model = Expenses
    success_url = '/expenses/'


class ExpensesUpdateView(UpdateView):
    model = Expenses
    form_class = ExpenseForm
    template_name = 'expenses/form.html'
    context_object_name = 'expense'

    def get_context_data(self, **kwargs):
        context = super(ExpensesUpdateView, self).get_context_data()
        context['editing'] = True
        return context
