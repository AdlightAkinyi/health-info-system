from django.urls import path
from . import api_views

urlpatterns = [
    # API endpoint to list all clients
    path('clients/', api_views.client_list_api, name='client_list_api'),
    # API endpoint to get a specific client by ID
    path('clients/<int:client_id>/', api_views.client_detail_api, name='client_detail_api'),
]
