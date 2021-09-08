from typing import List, Text
from django.db import models
from django.db.models.fields import BooleanField, CharField, FloatField, IntegerField, TextField, TimeField
from django.db.models.fields.related import ForeignKey

# Create your models here.



class Details(models.Model):

    # basics
    reference_id = CharField(max_length=25)
    name = CharField(max_length=15)
    time = TimeField(auto_now_add=True)
    # income details
    income = IntegerField()
    tax = FloatField()
    # expense details
    expenses = IntegerField()
    # debts
    debt = IntegerField()
    current_savings = FloatField()
    home_owner = BooleanField()

    def giving_rec(self):
        return round(self.monthly_income()*0.1, 2)
    def saving_rec(self):
        return round(self.monthly_income()*0.1, 2)
    def food_rec(self):
        return round(self.monthly_income()*0.1, 2)    
    def utilities_rec(self):
        return round(self.monthly_income()*0.05, 2)
    def housing_rec(self):
        return round(self.monthly_income()*0.25, 2)
    def transportation_rec(self):
        return round(self.monthly_income()*0.1, 2)    
    def health_rec(self):
        return round(self.monthly_income()*0.05, 2)
    def insurance_rec(self):
        return round(self.monthly_income()*0.1, 2)    
    def recreation_rec(self):
        return round(self.monthly_income()*0.05, 2)

    def personal_rec(self):
        return round(self.monthly_income()*0.05, 2)

    def misc_rec(self):
        return round(self.monthly_income()*0.05, 2)

    def monthly_income(self):
        # This code was written as a joke, dont @ me. 
        return float(str(self.income/12).split('.')[0] + '.' + str(self.income/12).split('.')[1][0:2])

    def post_tax(self):
        if self.tax == 0:
            return self.income
        else:
            post_tax_income = self.income * (1 -(self.tax * .01))
            return post_tax_income

    def taxes_paid_yearly(self):
        if self.tax == 0:
            return 0
        else:
            return self.income * (self.tax * .01)

    def taxes_monthly(self):
        monthly_tax_paid = (self.income * (self.tax * .01))/12
        return round(monthly_tax_paid, 2)

    def savings_advice(self):
        if self.debt == 0:
            return self.income*0.1

        if self.debt > 0 and self.current_savings > 1000:
            # if you have more than a G and debt, use savings
            return (self.current_savings-1000)*(-1)

        if self.debt > 0 and self.current_savings < 1000:
            # if we have debt and have less than 1000 in savings:
            return 1000-self.current_savings

        else:
            return f'Error, see savings_advice in models.py'

    def __str__(self):
        return f"{self.name}'s budget"


class State(models.Model):
    name = models.TextField(max_length=20)
    abbrev = models.TextField(max_length=2)

    

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.TextField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name='city')
    index = models.FloatField()
    grocery = models.FloatField()
    housing = models.FloatField()
    utilities = models.FloatField()
    transportation = models.FloatField()
    healthcare = models.FloatField()
    misc = models.FloatField()

    

    def __str__(self):
        return f'{self.name}, {self.state}'


class Income_expenses(models.Model):
    income = models.TextField(max_length=50)
    grocery = models.FloatField()
    housing = models.FloatField()
    # utilities = models.FloatField()
    transportation = models.FloatField()
    healthcare = models.FloatField()
    misc = models.FloatField()

    
    def __str__(self):
        return f'{self.income} '


    def grocery_monthly(self):
        return round(self.grocery/12, 2)

    def housing_monthly(self):
        return round(self.housing/12, 2)

    def transportation_monthly(self):
        return round(self.transportation/12, 2)

    def healthcare_monthly(self):
        return round(self.healthcare/12, 2)

    def misc_monthly(self):
        return round(self.misc/12, 2)
