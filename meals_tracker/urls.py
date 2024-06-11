from django.urls import path
from meals_tracker import views

app_name = 'meals_tracker'

urlpatterns = [
    path('', views.home, name = "home_page"),
    path('about/', views.about, name="about_page"),
    path('calorie_calculation/', views.calorie_calc, name="calorie_calc"),
    path('meals_tracking/', views.meals_tracking, name="meals_tracking"),
]