from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from expenses.models import Expenses
from django.contrib.auth.mixins import LoginRequiredMixin
from expenses.forms import ExpenseForm
import datetime
from django.db.models import Sum, Q
from django.shortcuts import redirect
from django.contrib import messages


class ExpensesListView(LoginRequiredMixin, ListView):
    template_name = 'expenses/list.html'
    context_object_name = 'expenses'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        month = datetime.datetime.now().month

        context['month_expenses'] = Expenses.objects.filter(when__month=month).aggregate(Sum('amount'))['amount__sum']
        context['total_expenses'] = Expenses.objects.aggregate(Sum('amount'))['amount__sum']

        context['q'] = self.request.GET.get('q', '')
        context['types'] = Expenses.EXPENSE_TYPES

        return context

    def get_queryset(self):
        queryset = Expenses.objects.all()

        # Search keywords
        if self.request.GET.get('q'):
            q = self.request.GET.get('q')
            queryset = queryset.filter(Q(name__icontains=q) | Q(description__icontains=q))

        # Filter by validation
        if self.request.GET.get('valid'):
            queryset = queryset.filter(valid__exact=self.request.GET.get('valid'))

        if self.request.GET.get('type'):
            queryset = queryset.filter(type__exact=self.request.GET.get('type'))

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
    fields = ['id', 'name', 'when', 'description', 'type', 'amount', 'author', 'valid']


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


class ValidateExpense(UpdateView):
    template_name = 'expenses/validate.html'
    context_object_name = 'expense'
    model = Expenses
    fields = ['id', 'name', 'when', 'description', 'type', 'amount', 'author']
    success_url = '/test'

    # Form will always be invalid. Intercept request here to validate expense
    def form_invalid(self, form):
        pk = self.kwargs['pk']
        expense = Expenses.objects.filter(pk=pk)
        expense.update(valid='YES')
        messages.success(self.request, 'You have validated this expense')
        return redirect('/expenses?valid=NO')
