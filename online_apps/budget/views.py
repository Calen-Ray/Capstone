from django.shortcuts import get_object_or_404, render
from .models import Details

# Create your views here.


def home(request):

    context = {
        'details': Details.objects.all()
    }

    return render(request, 'budget/index.html', context)




def create(request):
    if request.method == "POST":
        reference_number = request.POST['ref_number']
        budget = get_object_or_404(Details, reference_id=reference_number)
        context = { 
            'ref_number' : reference_number,
            'budget': budget
        }
        return render(request, 'budget/details.html', context)


    if request.method == "GET":
        context = {
            'details': Details.objects.all()
        }

        return render(request, 'budget/details.html', context)



def edit(request, number):
    if request.method == "POST":
        budget = get_object_or_404(Details, reference_id=number)
        context = { 
            'ref_number' : number,
            'budget': budget
        }
        return render(request, 'budget/edit.html', context)


def save(request, number):
    if request.method == "POST":
        budget = get_object_or_404(Details, reference_id=number)
        update = request.POST


        budget.income = float(update['income'])
        budget.tax = float(update['tax'])
        budget.expenses = float(update['expenses'])
        budget.debt = float(update['debt'])
        budget.current_savings = float(update['current_savings'])
        budget.save()





        context = { 
            'ref_number' : number,
            'budget': budget
        }
        return render(request, 'budget/details.html', context)
