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