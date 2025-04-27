from django.http import JsonResponse
from .models import Client

def client_list_api(request):
    """
    API endpoint to return a list of clients in JSON format.
    """
    clients = Client.objects.all().values('id', 'full_name', 'gender', 'date_of_birth')
    return JsonResponse(list(clients), safe=False)

def client_detail_api(request, client_id):
    """
    API endpoint to return details of a specific client based on their ID.
    """
    try:
        client = Client.objects.get(id=client_id)
        client_data = {
            'id': client.id,
            'full_name': client.full_name,
            'gender': client.gender,
            'date_of_birth': client.date_of_birth,
            'age': client.age,
        }
        return JsonResponse(client_data)
    except Client.DoesNotExist:
        return JsonResponse({'error': 'Client not found'}, status=404)
