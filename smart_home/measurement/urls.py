from django.urls import path
from .views import SensorView, DetailSensorView, MeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', DetailSensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
