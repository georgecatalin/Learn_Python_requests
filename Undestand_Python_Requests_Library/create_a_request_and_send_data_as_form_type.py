import requests


"""
Note: 
I will be using the following services for testing here:
https://httpbin.org/
https://pipedream.com/
"""

payload_httpbin = {"name": "George Calin", "location":"Galati"}
my_request_httpbin = requests.post("https://httpbin.org/post", data=payload_httpbin)

print(my_request_httpbin) # prints out the status code of the response
print(my_request_httpbin.text) # prints out the response which in this dummy API endpoint goes for The request's POST parameters.

"""
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "location": "Galati", 
    "name": "George Calin"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "33", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.32.3", 
    "X-Amzn-Trace-Id": "Root=1-68151b56-2901a01b30799cd22c8c9575"
  }, 
  "json": null, 
  "origin": "5.13.131.213", 
  "url": "https://httpbin.org/post"
}

"""

payload_pipedream = {"brand":"Ford", "model":"Kuga Hybrid 2.5"}
my_request_pipedream_form_data = requests.post("https://eow5gbrear6if9z.m.pipedream.net", data=payload_pipedream)
print(my_request_pipedream_form_data) # get the status code <Response [200]>
print(my_request_pipedream_form_data.text) # get the response

# {"about":"Pipedream is the fastest way to connects APIs. Build and run workflows with code-level control when you need it — and no code when you don't.","event_id":"2wYMODOP5lYXMCxsGJUsFedYUhz","workflow_id":"p_PACd7M7","owner_id":"o_1rIOGVw","deployment_id":"d_zqsAgb5q","timestamp":"2025-05-02T19:26:59.888Z","inspect":"https://pipedream.com/@/p_PACd7M7","quickstart":"https://pipedream.com/quickstart/"}

# content-type:  application/x-www-form-urlencoded   appears when the data is based form type in the request



"""

steps.trigger
{2}
context
{19}
id:
2wYMODOP5lYXMCxsGJUsFedYUhz
ts:
2025-05-02T19:26:59.888Z
pipeline_id:
null
workflow_id:
p_PACd7M7
deployment_id:
d_zqsAgb5q
source_type:
COMPONENT
verified:
false
hops:
null
test:
false
replay:
false
owner_id:
o_1rIOGVw
platform_version:
3.56.2
workflow_name:
RequestBin
resume:
null
emitter_id:
hi_kvHOPgp
external_user_id:
null
external_user_environment:
null
trace_id:
2wYMOAZTcOQmgfguuiclu0qtT8j
project_id:
proj_N9sV029
event
{7}
method:
POST
path:
/
query
{0}
client_ip:
5.13.131.213
url:
https://eow5gbrear6if9z.m.pipedream.net/
headers
{6}
host:
eow5gbrear6if9z.m.pipedream.net
content-length:
32
user-agent:
python-requests/2.32.3
•
accept-encoding:
gzip, deflate
accept:
*/*
content-type:
application/x-www-form-urlencoded
body
{2}
brand:
Ford
model:
Kuga Hybrid 2.5


"""


my_request_pipedream_params_data = requests.post("https://eow5gbrear6if9z.m.pipedream.net", params=payload_pipedream) # url parameters

"""

steps.trigger
{2}
context
{19}
•
id:
2wYN2Sl7QHco8BJsaDLzRnSiN7t
ts:
2025-05-02T19:32:19.373Z
pipeline_id:
null
workflow_id:
p_PACd7M7
deployment_id:
d_zqsAgb5q
source_type:
COMPONENT
verified:
false
hops:
null
test:
false
replay:
false
owner_id:
o_1rIOGVw
platform_version:
3.56.2
workflow_name:
RequestBin
resume:
null
emitter_id:
hi_kvHOPgp
external_user_id:
null
external_user_environment:
null
trace_id:
2wYN2P9iXqdLWg49pmpSmQdtD3f
project_id:
proj_N9sV029
event
{7}
method:
POST
path:
/
query
{2}
brand:
Ford
model:
Kuga Hybrid 2.5
client_ip:
5.13.131.213
url:
https://eow5gbrear6if9z.m.pipedream.net/?brand=Ford&model=Kuga+Hybrid+2.5
headers
{5}
host:
eow5gbrear6if9z.m.pipedream.net
content-length:
0
user-agent:
python-requests/2.32.3
accept-encoding:
gzip, deflate
accept:
*/*
body:

"""




my_request_pipedream_json_data = requests.post("https://eow5gbrear6if9z.m.pipedream.net", json=payload_pipedream) # json object passed as data

"""
"""