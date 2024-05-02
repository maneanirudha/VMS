import random
import string
from rest_framework import pagination
from rest_framework.pagination import PageNumberPagination

def generate_random_string():
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(5))

def generate_random_purchase_order_number():
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(25))


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    default_page_size = 10  # Set the default page size

    def get_page_size(self, request):
        # Get the page size from the query parameters
        page_size = super().get_page_size(request)
        
        # If page_size is not provided or invalid, use the default_page_size
        if page_size is None or page_size < 1:
            return self.default_page_size
        return page_size
