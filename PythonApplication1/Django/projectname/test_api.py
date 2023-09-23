# -*- coding: utf-8 -*-
import requests  
 

# URL для получения статистики продуктов
url = 'http://localhost:8000/myapp/api/product_stats/'
response = requests.get(url)

print(response.status_code)   

if response.status_code == 200:
    print(response.json())   
else:
    print('Error')

# URL для получения списка всех уроков доступных пользователю
url = 'http://localhost:8000/myapp/api/user_lessons/'
response = requests.get(url)

print(response.status_code)   

if response.status_code == 200:
    print(response.json())   
else:
    print('Error')
    

# URL для получения списка уроков для конкретного продукта
url = 'http://localhost:8000/myapp/api/product_lessons/1/'  # Замените 1 на нужный вам идентификатор продукта
response = requests.get(url)

print(response.status_code)   

if response.status_code == 200:
    print(response.json())   
else:
    print('Error')
    



input(" ")