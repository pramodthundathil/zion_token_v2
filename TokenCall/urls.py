from django.urls import path
from .import views

urlpatterns = [
    path("TokenDisplayer",views.TokenDisplayer,name="TokenDisplayer"),
    path("TokenAdmin",views.TokenAdmin,name="TokenAdmin"),
    path("TokenGenerator",views.TokenGenerator,name="TokenGenerator"),
    path("CallToken",views.CallToken,name="CallToken"),
    path("",views.SignIn,name="SignIn"),
    path("SignOut",views.SignOut,name="SignOut"),
    path("ReCallToken",views.ReCallToken,name="ReCallToken"),
    path("RestTokenNewDay",views.RestTokenNewDay,name="RestTokenNewDay"),
]
