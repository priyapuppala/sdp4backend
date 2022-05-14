from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('userregister/', RegisterView.as_view()),
    path('userlogin/', LoginView.as_view()),
]