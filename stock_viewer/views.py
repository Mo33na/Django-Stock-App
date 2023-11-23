import json
import requests
from django.http import JsonResponse
from django.shortcuts import render

def stock_data(request):
    if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        api_url = request.GET.get('api_url')
        api_key = request.GET.get('apikey')  # if provided
        
        if api_key:
            api_url += f'?apikey={api_key}'  
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Failed to fetch data'}, status=400)

    return render(request, 'stock_data.html')

