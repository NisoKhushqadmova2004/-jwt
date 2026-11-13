from django.urls import path
from .views import debt_list, debt_detail
urlpatterns = [
    path('debts/', debt_list),
    path('debts/<int:pk>/', debt_detail),
]
