from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('create-purchase-order/',views.create_purchase_order),
    path('purchase-orders/',views.get_purchase_order_list),
    path('purchase-orders/<str:po_code>/',views.get_purchase_order_details),
    # path('get-vendor/<str:vendor_id>/',views.get_vendor),
    # path('update-vendor/<str:vendor_id>/',views.update_vendor),
    # path('delete-vendor/<str:vendor_id>/',views.delete_vendor),
]

urlpatterns = format_suffix_patterns(urlpatterns)
