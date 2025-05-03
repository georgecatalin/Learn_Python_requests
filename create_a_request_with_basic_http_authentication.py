import requests
from requests.auth import HTTPBasicAuth

"""
Note: I will be using https://httpbin.org/ to create the dummy requests

endpoint:
GET
/basic-auth/{user}/{passwd}
Prompts the user for authorization using HTTP Basic Auth.
"""

my_response = requests.get("https://httpbin.org//basic-auth/georgeca/pass", auth=HTTPBasicAuth("georgeca","pass") )
print(my_response) # prints the status code : 200 success, 4xx if unsuccessful due to client error