import requests

"""
Note: I shall be using 'https://reqres.in/' to emulate the virtual endpoints
"""


'''


'''



my_request = requests.get("https://reqres.in//api/users/2")  # get single user with id = 2

print(my_request.text) # prints out the response as a string
# {"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},"support":{"url":"https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral","text":"Tired of writing endless social media content? Let Content Caddy generate it for you."}}


print(my_request.json()) # prints out the response as a json object which can be parsed as a dictionary in Python
# {'data': {'id': 2, 'email': 'janet.weaver@reqres.in', 'first_name': 'Janet', 'last_name': 'Weaver', 'avatar': 'https://reqres.in/img/faces/2-image.jpg'}, 'support': {'url': 'https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral', 'text': 'Tired of writing endless social media content? Let Content Caddy generate it for you.'}}


response_dictionary = my_request.json()
print(response_dictionary["data"]["email"]) # janet.weaver@reqres.in


