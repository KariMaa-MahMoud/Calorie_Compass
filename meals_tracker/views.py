from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'meals_tracker/home.html')

def about(request):
    return render(request, 'meals_tracker/about.html')

def calorie_calc(request):
    return render(request, 'meals_tracker/calorie_calc.html')

def meals_tracking(request):
    return render(request, 'meals_tracker/meal-tracking.html')
