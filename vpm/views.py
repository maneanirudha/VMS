from django.http import JsonResponse
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import api_view, authentication_classes , permission_classes
from .models import *
from utility.response_utils import *
from utility.common_messages import *
from utility.common_functions import *



"""
Use: To create new vendor with unique vendor_code
endpoint :{{base_url}}/api/create-vendor/


request body:
{
        "name": "Anirudha",
        "address": "Satara",
        "contact_details":8600395045
    }
"""
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_vendor(request):

    try:
        request_body = request.data
        vendor_name = request_body['name']
        vendor_address = request_body['address']
        contact_details = request_body['contact_details']

        print(vendor_name,vendor_address)
    except KeyError:
        return rokay(jsonKeyError)


    v_code = generate_random_string()
    print(v_code)

    Vendor.objects.create(name=vendor_name,address=vendor_address,contact_details=contact_details,
                        vendor_code=v_code)

    return rokay(profileCreated)

"""
Use: To get all vendor list
endpoint :{{base_url}}/api/vendors/
"""
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_all_vendors(request):

    vendor_obj = Vendor.objects.all()

    vendor_list = [vend.json for vend in vendor_obj]
    vendor_count = len(vendor_list)
    all_vendors = {
        "total_count":vendor_count,
        "data":vendor_list
    }

    print(vendor_list)

    return JsonResponse(
                all_vendors,
                status=status.HTTP_200_OK,
            )

"""
Use: To get specific vendor by vendor_code
endpoint : {{base_url}}/api/get-vendor/789YV/

"""
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_vendor(request,vendor_id):

    try:
        vendor_obj = Vendor.objects.get(vendor_code=vendor_id)
        print(vendor_obj)

        vendor_profile = vendor_obj.json

        return JsonResponse(
                    vendor_profile,
                    status=status.HTTP_200_OK,
                )
    except Vendor.DoesNotExist:
        return rerror(profileNotFound)

"""
Use: To update specific vendor by vendor_code
endpoint : {{base_url}}/api/update-vendor/789YV/

"""
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_vendor(request,vendor_id):

    vendor_profile = request.data

    try:
        request_body = request.data
        vendor_name = request_body['name']
        vendor_address = request_body['address']
        contact_details = request_body['contact_details']

        print(vendor_name,vendor_address,contact_details)
    except KeyError:
        return rokay(jsonKeyError)
    
    try:
        vendor_obj = Vendor.objects.get(vendor_code=vendor_id)

        vendor_obj.name = vendor_name
        vendor_obj.address = vendor_address
        vendor_obj.contact_details = contact_details
        vendor_obj.save()
        return rokay(profileUpdated)
    except Vendor.DoesNotExist:
        return rerror(profileNotFound)


"""
Use: To delete specific vendor by vendor_code
endpoint : {{base_url}}/api/delete-vendor/789YV/

"""
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])

def delete_vendor(request, vendor_id):
    try:
        vendor_obj = Vendor.objects.get(vendor_code=vendor_id)
        vendor_obj.delete()  # Call delete method to delete the vendor
        return rokay(profileDeleted)
    except Vendor.DoesNotExist:
        return rerror(profileNotFound)


    