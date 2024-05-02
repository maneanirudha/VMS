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


"""
Use: To list all purchase order with unique vendor_code
endpoint without pagination:{{base_url}}/api/pot/purchase-orders/?vendor_code=6KNA0
endpoint with pagination :{{base_url}}/api/pot/purchase-orders/?vendor_code=LA1B9&page=2&page_size=5
query params :  1.vendor_code
                2.page
                3.page_size


"""

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_purchase_order_list(request):

    try:
        vendor_code = request.query_params.get('vendor_code')
        print(vendor_code)
    except KeyError:
        return rokay(queryParamError)
    
    vendor = get_object_or_404(Vendor, vendor_code=vendor_code)
    
    purchase_order_obj = PurchaseOrder.objects.filter(vendor=vendor)
    purchase_order_list = [pol.json for pol in purchase_order_obj]
    paginator = StandardResultsSetPagination()
    result_page = paginator.paginate_queryset(purchase_order_list,request)
    total_count = purchase_order_obj.count()

    

    print(purchase_order_list)

    # total_count = len(purchase_order_list)
    filtered_list = {
        "total_count":total_count,
        "data":result_page
    }

    
    return JsonResponse(
                filtered_list,
                status=status.HTTP_200_OK,
            )



"""

Use: To get purchase order with unique po_code
endpoint without pagination:{{base_url}}/api/pot/purchase-orders/78YZQG5RWP6YTHP9LMJLRX6KE/

"""

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_purchase_order_details(request,po_code):

    try:
        po_code = PurchaseOrder.objects.get(po_number=po_code)
        print(po_code)
    except PurchaseOrder.DoesNotExist:
        return rerror(orderNotFound)
    
    purchase_order_obj = po_code.json

    return JsonResponse(
                purchase_order_obj,
                status=status.HTTP_200_OK,
            )


"""
Use: To update specific purchase order by purchase order number
endpoint : {{base_url}}/api/vpm/update-vendor/789YV/

"""
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_purchase_order(request,po_number):

    print(po_number)


    try:
        request_body = request.data
        delivery_date = request_body['delivery_date']
        status = request_body['status']
        quality_rating = request_body['quality_rating']

        print(delivery_date,status,quality_rating)
    except KeyError:
        return rokay(jsonKeyError)
    
    try:
        po_obj = PurchaseOrder.objects.get(po_number=po_number)

        po_obj.delivery_date = delivery_date
        po_obj.status = status
        po_obj.quality_rating = quality_rating
        po_obj.save()
        return rokay(purchaseOrderUpdated)
    except PurchaseOrder.DoesNotExist:
        return rerror(orderNotFound)