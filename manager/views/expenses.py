from django.shortcuts import render, get_object_or_404
from manager.models import Expense
from django.core.paginator import Paginator
from django import forms
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Sum, Q
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# Web form
class DateInput(forms.DateInput):
    input_type = 'date'





@csrf_exempt
@login_required
def list(request):
    q = request.GET.get('q', '')
    if q == '':
        expenses = Expense.objects.all()
    else:
        expenses = Expense.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))

    paginator = Paginator(expenses, 10)
    context = {
        'expenses': paginator.get_page(request.GET.get('page')),
        'total'   : Expense.objects.aggregate(Sum('amount'))['amount__sum'],
        'q'       : q
    }
    return render(request, 'expenses/list.html', context=context)

@login_required
def view(request, id):
    context = {
        'expense': Expense.objects.get(id=id)
    }
    return render(request, 'expenses/view.html', context=context)

@login_required
def create(request):
    form = ExpenseForm()

    if request.POST:
        form = ExpenseForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, 'Expense successfully saved')
            return redirect('list_expenses')

    context = {
        'form': form
    }

    return render(request, 'expenses/create.html', context)

@login_required
def update(request, id):
    form = ExpenseForm(model_to_dict(Expense.objects.get(pk=id)))
    if request.POST:
        form = ExpenseForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, 'Expense successfully updated')
            return redirect('list_expenses')

    context = {
        'form': form
    }

    return render(request, 'expenses/create.html', context)


def delete(request, id):
    Expense.objects.filter(pk=id).delete()
    messages.success(request, 'Expense has been deleted')
    return redirect('list_expenses')
