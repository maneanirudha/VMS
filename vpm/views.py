from django.http import JsonResponse
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import api_view, authentication_classes , permission_classes
from rest_framework.views import APIView
from .models import *
from utility.response_utils import *
from utility.common_messages import *
from utility.common_functions import *


class VendorProfile(APIView):


    """
    Use: To create new vendor with unique vendor_code
    endpoint :{{base_url}}/api/vendors/


    request body:
    {
            "name": "Anirudha",
            "address": "Satara",
            "contact_details":8600395045
        }
    """

    def post(self,request):

        vendor_profile = request.data

        try:
            request_body = request.data
            vendor_name = request_body['name']
            vendor_address = request_body['address']
            contact_details = request_body['contact_details']

            print(vendor_name,vendor_address)
        except KeyError:
            return rokay(jsonKeyError)

        print(vendor_profile)

        v_code = generate_random_string()
        print(v_code)

        Vendor.objects.create(name=vendor_name,address=vendor_address,contact_details=contact_details,
                            vendor_code=v_code)

        return JsonResponse(
                    vendor_profile,
                    status=status.HTTP_200_OK,
                )
    
    """
    Use: To get all vendor list
    endpoint :{{base_url}}/api/vendors/
    """

    def get(self,request):

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
    endpoint : {{base_url}}/api/vendors/789YV/

    """
    
    def get(self,request,vendor_id):

        vendor_obj = Vendor.objects.get(vendor_code=vendor_id)
        print(vendor_obj)

        vendor_profile = vendor_obj.json

        return JsonResponse(
                    vendor_profile,
                    status=status.HTTP_200_OK,
                )


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def test(request):
    dict = {
        'Test':'Hello from backend!'
    }
    return JsonResponse(
                dict,
                status=status.HTTP_200_OK,
            )