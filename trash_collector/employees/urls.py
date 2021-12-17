from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name="create"),
    path('edit_employee_profile/', views.edit_profile, name="edit_employee_profile"),
    path('charge/<int:pk>', views.charge, name="charge"),
    path('monday/', views.filter_monday, name="filter_monday"),
    path('tuesday/', views.filter_tuesday, name="filter_tuesday"),
    path('wednesday/', views.filter_wednesday, name="filter_wednesday"),
    path('thursday/', views.filter_thursday, name="filter_thursday"),
    path('friday/', views.filter_friday, name="filter_friday")
]

