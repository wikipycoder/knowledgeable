from django.urls import path
from . import views

urlpatterns = [

    path("wallet", views.WalletAPIView.as_view(), name="wallet")
]