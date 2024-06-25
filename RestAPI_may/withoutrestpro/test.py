import requests
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'apijson'
resp = requests.get(BASE_URL + END_POINT)
# print(type(resp))
# print(resp.json())
# print(type(resp.json()))
data = resp.json()
print('Data from django application:')
print('-'*30)
print('Employee Number:',data['eno'])
print('Employee Name:',data['ename'])
print('Employee Salary:',data['esal'])
print('Employee Address:',data['eaddr'])