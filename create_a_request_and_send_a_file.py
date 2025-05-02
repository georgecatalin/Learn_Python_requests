import requests

"""
I will be using https://pipedream.com/
"""

# sending files via API is not a frequently encountered situation

file = {'file':open('dog.jpg', 'rb')}
my_request = requests.post("https://eopukd1s21v6dza.m.pipedream.net", files=file)
# with this example multipart/form-data; boundary=bef19dfc9f6fb52e8e44c2cea86de089

# in case if we wish to pass also the mime type of the file to instruct the API endpoint what it is going to receive

# extract the mime type of the file type you are willing to send from https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types/Common_types

file_with_specified_mime_type ={'file':('dog.jpg',open('dog.jpg','rb'),'image/jpeg')}
my_request_with_specified_mime_type = requests.post("https://eopukd1s21v6dza.m.pipedream.net", files=file_with_specified_mime_type)

"""
steps.trigger
{2}
context
{19}
id:
2wYPmUgWPlS5ofZfOqcdZM5clVa
ts:
2025-05-02T19:54:52.319Z
pipeline_id:
null
•
workflow_id:
p_vQCwJyW
deployment_id:
d_WpsOrldZ
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
-more-
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
https://eopukd1s21v6dza.m.pipedream.net/
headers
{6}
body
{1}
file
{4}
filename:
dog.jpg
encoding:
7bit
mimetype:
image/jpeg
url
https://pipedream-catcher-bodies.s3.amazonaws.com/94285777-ca95-40f9-96ac-d389c9b84b87?AWSAccessKeyId=ASIA5F5AGIEA6YYQNDEB&Expires=1746217492&Signature=xAmPKM8LyoPh%2FbAsU4pRt%2F63EhA%3D&x-amz-security-token=FwoGZXIvYXdzEFUaDBDWQ0%2BtqdxhL8U4QiKNBIBLN0P2HMYeefvV1%2B1irDAMzYwErTmZuzY%2FerK9%2BYLCzMSEfE7RGXqBWBLQgbnoDVHfFnXLmm8c%2B76zAKlOcM1GOIO84rB1TvTZgpu3ZOjuNysT6M3elyUAnE%2F4WJOZtSsPj%2F8OOuAeWd%2BLPBH0N%2Bi1I7P3F0lXNIsDOBO6IchPumW0GMyc2jF3djAi%2F7kuRIZydujbuYkbuF0C5bGz22yBxlRFJCc8%2Bc3qp40d0Z%2Fzkxt%2FyXyNFCEIRyy%2B0iNF12%2BmjTNriT%2B95RzloTaFeQi3iMUABA20BgP33kXvuvlkTylIdvR5P3F4KYYOswGs7dDvdNG3LEmIPvv6s8UOeIlGz1GWQL%2BzdoQF4P%2FicS4xq3xIlTglGHpVEegvZPsASofkQlgkJ%2BpU8TA8Q%2Bz9hcq0c8ZhN04JqsFAQLpCAvgzxoYnedkVbtYUjwGF6W24CBtKszlvFqbQbJQ%2BEGLVJgvneDp2CX5LIwXkOPlR51MfdvjQ1JF9PPTfVmn2uDO5WgaqFEBTcpGi0tjKO9kydbMAoE8NWRVyhRYQ6IvCHDumIlaSJp6HkjsHaBFL5X6UhCUP2dxlaPrnuq5zzNmsftVI2tEDI7R6hBm5C22NMTYVvkcf0XDDfLxjRj7rEH7BUes9txhVlTcL3UIOw08mSakjGB4seoLLimneChRHpAArGU7pymJuZvVYgOGw4iilttTABjIqte%2F0YgkGjUyynNuciKHfI4QM9IZoZ7EGyHATihHq%2Fbxw3QP6IklLnleb
"""