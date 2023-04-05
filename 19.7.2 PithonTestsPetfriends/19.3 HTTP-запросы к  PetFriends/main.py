import requests

# res = requests.get(url, headers=headers, params=params)

# res.status_code — код состояния ответа,
# res.text — текстовые данные ответа от сервера,
# res.json() — преобразование полученных текстовых данных в формат json.

##########################
# status = 'available'
# res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}",
#                    headers={'accept': 'application/json'})
# print(res.status_code)
# print(res.text)
# print(res.json())
# print(type(res.json()))


##########################
# Ещё есть вариант передачи параметров при помощи атрибута params. Когда у вас много параметров,
# то их удобнее хранить в словаре, а не в длинной строке.

# status = 'available'
# res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'},
#                    headers={'accept': 'application/json'})
#
#     if 'application/json' in response.headers['Content-Type']:
#         response.json()
#     else:
#         response.text
#

##################################################################
# Тип запроса POST
# res = requests.post(url, headers=headers, data=data)

# data — это данные, отправляемые на сервер в теле запроса.
# Передаются в формате словаря data = {‘key1’: ‘value1’, ‘key2’: ‘value2’}.

##################################################################

# Тип запроса DELETE
#Используется для  удаления какого-либо объекта данных на сервере.
# Для этого в качестве параметров запроса также обязательно передаётся url-адрес,
# на который делается запрос. В зависимости от того, как сервер читает входящий запрос,
# соответственно передаются и остальные параметры.

#res = requests.delete(url, **kwargs)


##################################################################

#Тип запроса PUT
#Используется для изменения данных на сервере. В качестве параметров также принимает url
# и данные data для внесения изменений.
#По своей сути очень похож на POST-запрос.

#res = requests.put(url, data=data)