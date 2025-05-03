import  requests


try:
    my_response = requests.get("https://www.marabibba.com")
    print(my_response)
    print(my_response.text)
except requests.exceptions.ConnectionError:
    print("There was a connection error")