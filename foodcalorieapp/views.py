from django.shortcuts import render
# Imtiaz Adar
# Calorie Counter App
# Python
# Django
# Phone : +8801778767775
def web_homepage(request):

    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers={'X-Api-Key': 'KWnXN4S78zGjMzmnYgP0qQ==9nAv3HfgMvYnjefF'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as err:
            api = '!!! THERE IS SOME ERROR !!!'
            print(err)
        return render(request, 'homepageweb.html', {'api':api})
    else:
        return render(request, 'homepageweb.html', {'query':'Enter a valid query'})


    # query = '1lb brisket and fries'
    # api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    # response = requests.get(api_url, headers={'X-Api-Key': 'KWnXN4S78zGjMzmnYgP0qQ==9nAv3HfgMvYnjefF'})
    # if response.status_code == requests.codes.ok:
    #     print(response.text)
    # else:
    #     print("Error:", response.status_code, response.text)
