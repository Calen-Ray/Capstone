from django.db import models
from django.db.models.fields import CharField, FloatField, IntegerField, TimeField

# Create your models here.


class Details(models.Model):
    '''
    what does a budget need?
    name,
    date,
    projected income,
    projected taxes, optional? maybe a dict of state tax rates?
    expenses
    debts
    savings payment
    '''


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


    def monthly_income(self):
        return round(self.income/12, 2)



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




