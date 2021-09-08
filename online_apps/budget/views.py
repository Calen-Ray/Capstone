from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Details, Income_expenses, City, State
import json
import string
import random
text = list(string.ascii_letters)
intigers = list(string.digits)

# Create your views here.


def home(request):

    context = {
        'details': Details.objects.all()
    }

    return render(request, 'budget/index.html', context)


def create(request, number=False):
    if not number:
        reference_number = request.POST['ref_number']
    else:
        reference_number = number

    budget = get_object_or_404(Details, reference_id=reference_number)
    income = budget.income
    statistics = get_object_or_404(Income_expenses, income = '5k-10k')
    
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


def edit(request, number):
    if request.method == "POST":
        budget = get_object_or_404(Details, reference_id=number)
        context = { 
            'ref_number' : number,
            'budget': budget,
            'new': False,
            'error': False
        }
        return render(request, 'budget/edit.html', context)

    if request.method == "GET":
        if number == 'error':
            error_status = True
        else:
            error_status = False
        
        ref = f""
        while True:
            ref = ''.join([f"{random.choice(intigers)}{random.choice(text)}" for x in range(5)])
            print(ref)
            try:
                budget = get_object_or_404(Details, reference_id=ref)
            except:
                break

        context = { 
            'ref_number' : ref,
            'budget': False,
            'new': True,
            'error': error_status,
        }
        return render(request, 'budget/edit.html', context)


def library(request):
    return render(request, 'budget/resources.html')


def save(request, number):
    if request.method == "POST":
        try:
            budget = get_object_or_404(Details, reference_id=number)
        except:
            budget = Details()
        update = request.POST

        try:
            budget.name = (update['name'])
            budget.income = float(update['income'])
            budget.tax = float(update['tax'])
            budget.expenses = float(update['expenses'])
            budget.debt = float(update['debt'])
            budget.current_savings = float(update['current_savings'])
            budget.home_owner = False
            budget.reference_id = number
            budget.save()
        except:
            return HttpResponseRedirect('http://localhost:8000/budget/edit/'+'error')





        context = { 
            'ref_number' : number,
            'budget': budget
        }
        return HttpResponseRedirect('http://localhost:8000/budget/create/'+number)


def faq(request):
    return render(request, 'budget/faq.html')


def about(request):
    return render(request, 'budget/about.html')


def contact(request):
    return render(request, 'budget/contact.html')


def get_state(request, state):
    if request.method == 'GET':
        state = get_object_or_404(State, name=state)
        cities = City.objects.filter(state=state)

        cities_formatted = list(cities.values())

        context = {
            'cities' : cities_formatted,
        }

        return JsonResponse(context)


def get_city(request, state, city, income_level):
    if request.method == 'GET':

        income_details = get_object_or_404(Income_expenses, income=income_level)
        print('deets', income_details.grocery)
        state_data = get_object_or_404(State, name=state)
        city_data = get_object_or_404(City, name=city, state=state_data)

        context = {
            'name': city_data.name,
            'index': city_data.index,
            'grocery': city_data.grocery,
            'housing': city_data.housing,
            'utilities': city_data.utilities,
            'transportation': city_data.transportation,
            'healthcare': city_data.healthcare,
            'misc': city_data.misc,

            'index_percent': f'{"+" if city_data.index-100>0 else ""}{round(city_data.index-100, 2)}%',
            'grocery_percent': f'{"+" if city_data.grocery-100>0 else ""}{round(city_data.grocery-100, 2)}%',
            'housing_percent': f'{"+" if city_data.housing-100>0 else ""}{round(city_data.housing-100, 2)}%',
            'utilities_percent': f'{"+" if city_data.utilities-100>0 else ""}{round(city_data.utilities-100, 2)}%',
            'transportation_percent': f'{"+" if city_data.transportation-100>0 else ""}{round(city_data.transportation-100, 2)}%',
            'healthcare_percent': f'{"+" if city_data.healthcare-100>0 else ""}{round(city_data.healthcare-100, 2)}%',
            'misc_percent': f'{"+" if city_data.misc-100>0 else ""}{round(city_data.misc-100, 2)}%',         

            'grocery_local': round((income_details.grocery/12)*(city_data.grocery*.01), 2),
            'housing_local': round((income_details.housing/12)*(city_data.housing*.01), 2),
            # 'utilities_local': round((income_details.utilities/12)*(city_data.utilities*.01), 2),
            'transportation_local': round((income_details.transportation/12)*(city_data.transportation*.01), 2),
            'healthcare_local': round((income_details.healthcare/12)*(city_data.healthcare*.01), 2),
            'misc_local': round((income_details.misc/12)*(city_data.misc*.01), 2),  

            'grocery_difference': round(((income_details.grocery/12)*(city_data.grocery*.01))-(income_details.grocery/12), 2),
            'housing_difference': round(((income_details.housing/12)*(city_data.housing*.01))-(income_details.housing/12), 2),
            # 'utilities_difference': round(((income_details.utilities/12)*(city_data.utilities*.01))-(income_details.utilities/12), 2),
            'transportation_difference': round(((income_details.transportation/12)*(city_data.transportation*.01))-(income_details.transportation/12), 2),
            'healthcare_difference': round(((income_details.healthcare/12)*(city_data.healthcare*.01))-(income_details.healthcare/12), 2),
            'misc_difference': round(((income_details.misc/12)*(city_data.misc*.01))- (income_details.misc/12), 2),  

            'national_housing': income_details.housing/12,
            'national_grocery': income_details.grocery/12,
            'national_transportation': income_details.transportation/12,
            'national_healthcare': income_details.healthcare/12,
            'national_misc': income_details.misc/12,
        }
        print(context)
        return JsonResponse(context)