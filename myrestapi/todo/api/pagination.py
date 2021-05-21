from rest_framework.pagination import PageNumberPagination

class TaskPaginationPage(PageNumberPagination):
    page_size = 2