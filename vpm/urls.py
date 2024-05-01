from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('create-vendor/',views.VendorProfile.as_view()),
    path('test/', views.test),
]

urlpatterns = format_suffix_patterns(urlpatterns)
