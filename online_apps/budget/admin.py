from django.contrib import admin

# Register your models here.

from .models import Details,City,State,Income_expenses

admin.site.register(Details)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Income_expenses)