from rest_framework import pagination

# class LargeResultsSetPagination(pagination.PageNumberPagination):
#     page_size = 2
#     page_size_query_param = 'page_size'
#     max_page_size = 50
#     page_query_param = 'p'

# class LargeResultsSetPagination(pagination.PageNumberPagination):
#     page_size = 5
#     page_size_query_param = 'page_size' 
#     max_page_size = 200
#     last_page_strings = ('the_end',)

class LargeResultsSetPagination(pagination.LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'l'
    offset_query_param = 'o'
    max_limit = 50