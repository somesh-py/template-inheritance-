from django.urls import path
from . import views


urlpatterns = [
    path('',views.parent),
    path('frontend/',views.frontend),
    path('backend/',views.backend),
]

