import requests

"""
Note:
I will be using https://reqres.in/ for testing the API
"""
payload = {
    "name": "Mara Calin",
    "job": "software developer"
}

my_header = {"x-api-key":"reqres-free-v1"}

my_request = requests.post("https://reqres.in/api/users", json=payload, headers=my_header)

print(my_request) # this will print the status code of the response  --> <Response [201]>  2xx means SUCCESS
print(my_request.text) # this will print the response

# {"name":"Mara Calin","job":"software developer","id":"94","createdAt":"2025-05-02T19:05:53.375Z"}