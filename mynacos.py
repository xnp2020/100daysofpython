#!/usr/bin/env python
#-*- coding:utf-8 -*-

from time import sleep
import requests
import json

# Make an API call, and store the response.
while True:
    url = 'http://192.168.2.11:8848/nacos/v1/ns/instance/list?serviceName=node_exporter&namespaceId=5f61da8f-cd3e-42e8-894c-623eb14eb133'
    r = requests.get(url)
    
    response_dict = r.json()
    nodelist = []
    for host in response_dict['hosts']:
        host_str = str(host["ip"])+':'+str(host["port"])
        host_list = [ host_str ]
        host_dict = { "targets": host_list }
        nodelist.append(host_dict)
    
    readable_file = 'node.json'
    with open(readable_file, 'w') as f:
        json.dump(nodelist, f, indent=4)
    
    sleep(5)