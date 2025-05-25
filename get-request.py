import requests

from apikey import API_TOKEN

params = {'q': 'London', 'appid': API_TOKEN, 'units': 'metric'}  # параметры, q - это поиск,
# appid - это ключ сайта к доступу API,
# units - это доп параметр с сайта

headers = {
    "headers": {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
        "Host": "httpbin.org",
        "Priority": "u=1, i",
        "Referer": "https://httpbin.org/",
        "Sec-Ch-Ua": "\"Chromium\";v=\"136\", \"Microsoft Edge\";v=\"136\", \"Not.A/Brand\";v=\"99\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
        "X-Amzn-Trace-Id": "Root=1-6832dc2c-58b1b4bc75543bce1f2d626d"
    }
}

response = requests.get('https://httpbin.org/headers', params=headers)
# print(response.status_code)  # узнаем статус запроса
# print(response.headers)  # узнаем служебную информацию, которую передаёт сайт вашему браузеру
# print(response.text)  # получаем код сайта в тексте, можем достать что угодно из него
# print(response.json())  # получаем словарь json

# x = response.json()
# print(x["weather"][0]["main"])  #  словаря json, получаем значение
print(response.text)
