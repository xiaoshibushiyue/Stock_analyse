import requests

proxies = {"http": "140.250.149.139:47112"}
r = requests.get("http://www.baidu.com/", proxies=proxies)

print(r.status_code)
print(r.content)
