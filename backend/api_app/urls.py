from django.urls import path
from .views import CartItemViews, DiseaseViews

urlpatterns = [
    path('cart-items/', CartItemViews.as_view()),
    path('cart-items/<int:id>', CartItemViews.as_view()),
    path('diseases/', DiseaseViews.as_view()),
    path('disease/<str:hpoId>', DiseaseViews.as_view())
]
