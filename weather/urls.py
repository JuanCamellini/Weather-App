from django.contrib import admin
from django.urls import path

from .views import index, cameras, results, contact, thankyou

urlpatterns = [
    path('', index, name="home" ),
    path('results/', results, name="results"),
    path('live-cameras/', cameras, name="cameras"),
    path('contact/', contact, name="contact"),
    path('contact/thankyou/', thankyou, name="thankyou")
]
