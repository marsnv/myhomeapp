from django.urls import path
from hr import views as hr_views


urlpatterns = [
    path('hr_create', hr_views.hr_create, name='hr_create'),
    path('', hr_views.hr_index, name='hr_index'),
    path('<int:pk>', hr_views.Hr_Staff_DetailView.as_view(), name='hr_detail'),
    path('<int:pk>/update', hr_views.Hr_Staff_UpdateView.as_view(), name='hr_update'),
    path('<int:pk>/delete', hr_views.Hr_Staff_DeleteView.as_view(), name='hr_delete'),
]
