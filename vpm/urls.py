from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('create-vendor/',views.create_vendor),
    path('vendors/',views.get_all_vendors),
    path('get-vendor/<str:vendor_id>/',views.get_vendor),
    path('update-vendor/<str:vendor_id>/',views.update_vendor),
    path('delete-vendor/<str:vendor_id>/',views.delete_vendor),
]

urlpatterns = format_suffix_patterns(urlpatterns)
