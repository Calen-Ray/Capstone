from django.urls import path
from .views import home, create, edit, save, gettem

app_name = 'budget'
urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='details'),
    path('edit/<str:number>/', edit, name='edit'),
    path('save/<str:number>/', save, name='save'),
    path('fetch/<str:state>/', gettem, name='fetch'),
]