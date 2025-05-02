import requests

"""
I will be using https://httpbin.org/#/Images
"""

my_response = requests.get("https://httpbin.org//image/jpeg")

print(my_response) # status of the request <Response [200]>
print(my_response.headers) # header of the response

# {'Date': 'Fri, 02 May 2025 20:05:32 GMT', 'Content-Type': 'image/jpeg', 'Content-Length': '35588', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}

# to save the file
with open("my_saved_image.jpg", "wb") as new_file:
    for chunk in my_response.iter_content(chunk_size=500):
        new_file.write(chunk)