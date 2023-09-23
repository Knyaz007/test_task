# -*- coding: utf-8 -*-
import requests  
 

# URL ��� ��������� ���������� ���������
url = 'http://localhost:8000/myapp/api/product_stats/'
response = requests.get(url)

print(response.status_code)   

if response.status_code == 200:
    print(response.json())   
else:
    print('Error')

# URL ��� ��������� ������ ���� ������ ��������� ������������
url = 'http://localhost:8000/myapp/api/user_lessons/'
response = requests.get(url)

print(response.status_code)   

if response.status_code == 200:
    print(response.json())   
else:
    print('Error')
    

# URL ��� ��������� ������ ������ ��� ����������� ��������
url = 'http://localhost:8000/myapp/api/product_lessons/1/'  # �������� 1 �� ������ ��� ������������� ��������
response = requests.get(url)

print(response.status_code)   

if response.status_code == 200:
    print(response.json())   
else:
    print('Error')
    



input(" ")