from django.urls import path
from main import views as main_views
from hr import views as hr_views


urlpatterns = [
    path('', main_views.index, name='home'),
    path('about', main_views.about, name='about'),

]
