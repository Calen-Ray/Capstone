from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Details, Income_expenses, City, State

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
        income = budget.income
        statistics = False
        
        if income > 5000:
            statistics = get_object_or_404(Income_expenses, income = '5k-10k')
            if income > 10000:
                statistics = get_object_or_404(Income_expenses, income = '10k-15k')
                if income > 15000:
                    statistics = get_object_or_404(Income_expenses, income = '15k-20k')
                    if income > 20000:
                        statistics = get_object_or_404(Income_expenses, income = '20k-30k')
                        if income > 30000:
                            statistics = get_object_or_404(Income_expenses, income = '30k-40k')
                            if income > 40000:
                                statistics = get_object_or_404(Income_expenses, income = '40k-50k')
                                if income > 50000:
                                    statistics = get_object_or_404(Income_expenses, income = '50k-70k')
                                    if income > 70000:
                                        statistics = get_object_or_404(Income_expenses, income = '70k-80k')
                                        if income > 80000:
                                            statistics = get_object_or_404(Income_expenses, income = '80k-100k')
                                            if income > 100000:
                                                statistics = get_object_or_404(Income_expenses, income = '100k-120k')
                                                if income > 120000:
                                                    statistics = get_object_or_404(Income_expenses, income = '120k-150k')
                                                    if income > 150000:
                                                        statistics = get_object_or_404(Income_expenses, income = '150+')
                                            



        states = {}
        for state in State.objects.all():
            states[state.name] = ''
        print(states)


        context = { 
            'ref_number' : reference_number,
            'budget': budget,
            'national_statistics': statistics,
            'states_formatted': states
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


def gettem(request, state):
    if request.method == 'GET':
        state = get_object_or_404(State, name=state)
        cities = City.objects.filter(state=state)

        cities_formatted = list(cities.values())

        context = {
            'cities' : cities_formatted,
        }

        return JsonResponse(context)