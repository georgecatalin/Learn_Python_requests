import requests


"""
Note: using the  https://pipedream.com/
"""

# one can also pass the parameters as a secondary argument in the get method, in this case the parameters have been created as parts in a dictionary object

my_params = {"first_key":"first_value", "second_key":"second_value"}

my_request = requests.get("https://eooo15md6jkjxpg.m.pipedream.net", params=my_params)

'''

steps.trigger
{2}
context
{19}
id:
2wXZKyurdLjh31bDwTg4BwjJEdV
ts:
2025-05-02T12:43:38.835Z
pipeline_id:
null
workflow_id:
p_7NCqYDz
deployment_id:
d_EksPMQPm
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
o_zwIXpMd
platform_version:
3.56.2
workflow_name:
RequestBin
resume:
null
emitter_id:
hi_DlHqePd
external_user_id:
null
•
external_user_environment:
null
trace_id:
2wXZKutwKikl6Fbk8ktrhdGk3I3
project_id:
proj_qzsdBox
event
{6}
method:
GET
path:
/
query
{2}
first_key:
first_value
second_key:
second_value
client_ip:
81.196.55.43
url:
https://eooo15md6jkjxpg.m.pipedream.net/?first_key=first_value&second_key=second_value
headers
{4}
host:
eooo15md6jkjxpg.m.pipedream.net
user-agent:
python-requests/2.32.3
accept-encoding:
gzip, deflate
accept:
*/*

'''

