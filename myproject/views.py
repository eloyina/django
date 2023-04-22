from django.http import JsonResponse

def hello_world(request):
    data_array = ['apple', 'banana', 'orange']

    # Create a list of dictionaries with each value and its index
    data_with_index = []
    for i, value in enumerate(data_array):
        data_with_index.append({
            'index': i,
            'value': value
        })

    # Create the response dictionary
    response_data = {
        'message': 'Hello, world!',
        'array': data_with_index
    }

    # Return the JSON response
    return JsonResponse(response_data)
