from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('about/', views.about, name="About"),
    path('contact/', views.contact, name="Contact"),
]