from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="calories_app-home"),
    path('meals', views.MealsViewAggregate.as_view(), name="calories_app-meals"),
    path('meals/<int:id>', views.MealsViewPiecemeal.as_view(), name="calories_app-meals_by_id"),
    path('meals/day', views.MealsViewDay.as_view(), name="calories_app-meals_sum"),
]
