from urllib import request, parse

# with request.urlopen('https://xytx.ncu.edu.cn') as f:
#    data = f.read()
#    print('Status:', f.status, f.reason)
#    for k, v in f.getheaders():
#        print('%s: %s' % (k, v))
#    print('Data:', data.decode('utf-8'))
#
#req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS #X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/#8536.25')
# with request.urlopen(req) as f:
#    print('Status:', f.status, f.reason)
#    for k, v in f.getheaders():
#        print('%s: %s' % (k, v))
#    print('Data: ', f.read().decode('utf-8'))

# 模拟POST请求
#print('Login to weibo.cn...')
#email = input('Email: ')
#passwd = input('Password: ')
#login_data = parse.urlencode([('username', email),
#                              ('password', passwd),
#                              ('entry', 'mweibo'),
#                              ('client_id', ''),
#                              ('savestate', '1'),
#                              ('ec', ''),
#                              ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
#                              ])
#req = request.Request('https://passport.weibo.cn/sso/login')
#req.add_header('Origin', 'https://passport.weibo.cn')
#req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77')
#req.add_header(
#    'Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

#with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#    print('Status:', f.status, f.reason)
#    for k, v in f.getheaders():
#        print('%s: %s' % (k, v))
#    print('Data:', f.read().decode('utf-8'))

# 通过代理访问
proxy_handler = request.ProxyHandler({'http':'192.168.43.105:10809','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4181.9 Safari/537.36'})
#proxy_auth_handler = request.ProxyBasicAuthHandler()
#proxy_auth_handler.add_password('realm','host','username','password')
#opener = request.build_opener(proxy_handler, proxy_auth_handler)
opener = request.build_opener(proxy_handler)
with opener.open('https://www.youtube.com/') as f:
    print('Status:',f.status,f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))    

# 利用urllib读取JSON，然后将JSON解析为Python对象
import json
def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read().decode('utf-8')
        #print(type(data))
    return json.loads(data)