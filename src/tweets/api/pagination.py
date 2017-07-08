from rest_framework import pagination

class StandardResultsPagination(pagination.PageNumberPagination):
    page_size = 10 # result num show in one page
    page_size_query_param = 'page_size'
    max_page_szie = 1000