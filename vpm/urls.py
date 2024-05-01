from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('vendors/',views.VendorProfile.as_view()),
    path('vendors/<str:vendor_id>/',views.VendorProfile.as_view()),
    path('test/', views.test),
]

urlpatterns = format_suffix_patterns(urlpatterns)
