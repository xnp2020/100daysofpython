import json
import requests

def main():
    # 执行api调用并存储响应
    url = 'http://api.tianapi.com/social/index?key=6e82fd683a034ff6be87108885ca7700&num=10'
    r = requests.get(url)
    print(f"Status code: {r.status_code}")
    response_dict = r.json()
    for news in response_dict['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()

