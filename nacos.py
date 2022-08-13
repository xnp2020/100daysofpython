from urllib import request
import json

def fetch_data(url):
    req = request.Request(url)
    with request.urlopen(req) as f:
        data = f.read().decode('utf-8')
    return json.loads(data)


# 测试
URL = 'http://192.168.2.11:8848/nacos/v1/ns/instance/list?serviceName=node_exporter&namespaceId=5f61da8f-cd3e-42e8-894c-623eb14eb133'
data = fetch_data(URL)
print(type(data))
print('---')
print(data)
#assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')