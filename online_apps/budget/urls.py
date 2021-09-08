from django.urls import path
from .views import home, create, edit, save, get_state, get_city, library, faq,about, contact

app_name = 'budget'
urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='details'),
    path('create/<str:number>/', create, name='details'),
    path('faq/', faq, name='faq'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('library/', library, name='library'),
    path('edit/<str:number>/', edit, name='edit'),
    path('save/<str:number>/', save, name='save'),
    path('fetch/<str:state>/', get_state, name='fetch'),
    path('fetch_city/<str:state>/<str:city>/<str:income_level>/', get_city, name='fetch_city'),
]