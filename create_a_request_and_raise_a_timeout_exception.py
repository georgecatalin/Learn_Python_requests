import requests


"""
Note: for the simulation I will be using https://httpbin.org/

GET:
/delay/{delay}
Returns a delayed response (max of 10 seconds).

There exists 2 possible errors bound to timeout:
1. requests.exceptions.ReadTimeout: this means that the server responded in time, but it did not provided the response within the timeout time
2. requests.exceptions.ConnectTimeout : this means that the server did not respende in time withing the timeout time

we can write the code to account both situations with a try: except:

"""
try:
    response =  requests.get("https://httpbin.org//delay/15", timeout=10)
except requests.exceptions.ConnectTimeout :
    print("There was a connection request time out")
except requests.exceptions.ReadTimeout:
    print("There was a response time out")

