from django.urls import path
from .views import DiseaseViews

urlpatterns = [
    path('diseases/', DiseaseViews.as_view()),
    path('disease/<str:hpoId>', DiseaseViews.as_view())
]
