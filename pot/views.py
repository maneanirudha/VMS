from django.http import JsonResponse
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import api_view, authentication_classes , permission_classes
from .models import *
from utility.response_utils import *
from utility.common_messages import *
from utility.common_functions import *
from django.shortcuts import get_object_or_404



"""
Use: To create new vendor with unique vendor_code
endpoint :{{base_url}}/api/pot/create-purchase-order/


request body:
{
            "vendor_code": "LA1B9",
            "items": {
                "item_name":"Galexy S24"
            },
            "quantity":2
        }
"""
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_purchase_order(request):

    try:
        request_body = request.data
        vendor_code = request_body['vendor_code']
        items = request_body['items']
        quantity = request_body['quantity']

        print(vendor_code,items,quantity)
    except KeyError:
        return rokay(jsonKeyError)
    
    vendor = get_object_or_404(Vendor, vendor_code=vendor_code)


    po_number = generate_random_purchase_order_number()
    print(po_number)

    PurchaseOrder.objects.create(po_number=po_number,vendor=vendor,
                                 items=items,quantity=quantity)

    return rokay(orderCreated)