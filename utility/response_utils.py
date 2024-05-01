from django.http import JsonResponse
from rest_framework import status


def rokay(data):
    return JsonResponse(
        {"message": "SUCCESS", "data": data},
        status=status.HTTP_200_OK,
    )



def rerror(data):
    return JsonResponse(
        {"message": "ERROR", "data": data},
        status=status.HTTP_200_OK,
    )