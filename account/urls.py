from django.urls import path, include
from . import views

app_name = "account"
urlpatterns = [path("", views.AccountView.as_view(), name="index")]
