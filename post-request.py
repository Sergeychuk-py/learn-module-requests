import requests

data = {  # словарь получили с сайта httpbin.org
    'custname': 'Serge Sergeychuk',
    'custtel': '79129288283',
    'custemail': 'sergeychuk.serzh@bk.ru',
    'size': 'large',
    'topping': 'onion',
    'delivery': '14:30',
    'comments': '.!.'
}

response = requests.post('https://httpbin.org/post', data=data)

# print(response.status_code)
# print(response.text)

variable = requests.Session()  # сессия
aaa = variable.get('https://httpbin.org/form/post')

print(response.json())
