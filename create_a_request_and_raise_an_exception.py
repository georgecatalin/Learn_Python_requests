import requests

"""
I will be using https://httpbin.org/ to fake the API endpoint
"""

# there are two kinds of errors you might encounter when accessing an endpoint of an API:
#   1. The URL is wrong or the server is down
#   2. There is status code of 4xx client error or 5xx server error


try:
    response = requests.get('https://httpbin.org/status/504')
    print(response) # <Response [504]>
    response.raise_for_status()
except requests.exceptions.HTTPError:
    print("There was a 5xx error")

"""
Traceback (most recent call last):
  File "D:\Workshop\Training\Learn_Python_requests\create_a_request_and_raise_an_exception.py", line 15, in <module>
    response.raise_for_status()
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "D:\Workshop\Training\Learn_Python_requests\venv\Lib\site-packages\requests\models.py", line 1024, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 504 Server Error: GATEWAY TIMEOUT for url: https://httpbin.org/status/504
"""
