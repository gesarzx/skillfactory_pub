from api import PetFriends
from settings import *
import os
import re

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result
    print(f'ключ\n {result}')


def test_get_all_pets_with_valid_key(filter=''):
    """Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
     запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо ''"""

    # _,  --- означает, что статус не нужен

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='глазаналоб', animal_type='двортерьер',
                                     age='3', pet_photo='images/cat1.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    # pet_photo = os.path.join(os.path.dirname('F:\Python\QAP\pytest_first_test/tests/'), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "муська", "кот", "3", "images/cat2.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()
    num = len(my_pets['pets'])
    print(f' \n в списке , {num} питомцев')

# А что, если список питомцев пуст, и мы не можем добавить нового?
# Например, если не реализован такой функционал. И в этом случае нам приходится
# самим выбрасывать исключение как в тесте обновления информации о питомце:
def test_successful_update_self_pet_info(name='Мурзон', animal_type='Котэйка', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


# ДЗ 19.7.2

# тест 1
def test_get_api_key_with_correct_mail_and_wrong_password(email=valid_email, password=invalid_password):
    """Проверяем запрос с валидным email и c невалидным паролем.
    Проверяем нет ли ключа в ответе."""
    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result
    print(f'Статус {status} для теста с невалидным паролем')


# тест 2
def test_get_api_key_with_wrong_email_and_correct_password(email=invalid_email, password=valid_password):
    """Проверяем запрос с невалидным email и с валидным паролем.
    Проверяем нет ли ключа в ответе."""
    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result
    print(f'Статус {status} для теста с невалидным email')


# тест 3
def test_get_api_key_with_wrong_email_and_wrong_password(email=invalid_email, password=invalid_password):
    """Проверяем запрос с невалидным email и с невалидным паролем.
    Проверяем нет ли ключа в ответе."""
    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result
    print(f'\n Статус {status} для теста с невалидным email и паролем')


# тест 4
def test_add_new_pet_without_valid_data_BUG(name='', animal_type='', age=''):
    """Негатеинвый тест.
    Проверяем возможность добавление питомца с пустыми полями. Тест выводит предупреждение.
     После исправления бага, ответ сервера должен быть 400"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    print(f'\n Баг!!!Добавлен питомец с пустыми значениями name= {name}, animal_type={animal_type}, age={age}')


# тест 4.1
def test_add_new_pet_without_valid_data(name='', animal_type='', age=''):
    """позитивнй тест. Проверяем возможность добавление питомца с пустыми полями. Ответ сервера должен быть 400"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    assert status == 400


# тест 5
def test_get_my_pets_with_valid_key(filter='my_pets'):
    """ Проверяем, что запрос всех моих питомцев возвращает не пустой список.
       Для этого сначала получаем API ключ и сохраняем в переменную auth_key. Далее используя этоn ключ
       запрашиваем список всех моих питомцев и проверяем, что список не пустой."""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0
    num = len(result['pets'])
    print(f'\n {num} шт. my pets на сайте')


# тест 6
def test_add_pet_simple_with_incorrect_animal_type(name='Обормот', age='2'):
    """Проверка возможности добавление питомца (/api/create_pet_simple) с цифрами или символами вместо букв в переменной animal_type.
     ответ сервера должен быть 400."""

    animal_type = '-12###?/Cat'

    _, api_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(api_key, name, animal_type, age)

    assert status == 400


# тест 6.1
def test_add_pet_simple_with_incorrect_animal_type_BUG(name='Обормот', age='2'):
    """Негативный тест.
    Добавление питомца (/api/create_pet_simple) с цифрами\ символами вместо букв в переменной animal_type.
    Тест выводит предупреждение. После исправления бага ответ сервера должен быть 400."""

    animal_type = '-12###?/Cat'
    symbols = '#$%^&*{}|?/[]\><=+_~@-'
    symbol = []
    numbs='0123456789'
    numb=[]

    _, api_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(api_key, name, animal_type, age)

    assert status == 200
    for i in symbols:
        if i in result['animal_type']:
            symbol.append(i)

    for j in numbs:
        if j in result['animal_type']:
            numb.append(j)

    assert symbol[0] in result['animal_type'],numb[0] in result['animal_type']
    print(f'\n Баг!!!Добавлен питомец с недопустимыми в "Породе" (animal_type={animal_type}) \n специальными символами {symbol},{numb}')


# тест 7
def test_add_pet_simple_with_incorrect_age_BUG(name='Обормот', animal_type='смелый'):
    """Негативный тест.
    Добавление питомца (/api/create_pet_simple) с цифрами\ символами\ буквами вместо цифр в поле age.
    Тест выводит предупреждение. После исправления бага ответ сервера должен быть 400."""

    age = '2#ghfj'
    symbols = '#$%^&*{}|?/><=+_~@'
    symbol = []

    _, api_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(api_key, name, animal_type, age)

    assert status == 200
    for i in symbols:
        if i in result['age']:
            symbol.append(i)

    letter = re.search('[a-zA-Z]', result['age'])
    letter[0].isalpha()  # возвращает True если найдет хотя бы одну букву из указанного алфавита

    assert symbol[0] in result['age'], letter[0] in result['age']
    print(f'\n Баг!!!Добавлен питомец с недопустимыми в "возрасте" age={age} \n  символами: {symbol},{letter[0]}')

# тест 7.1
def test_add_pet_simple_with_incorrect_age(name='Обормот', animal_type='смелый'):
    """Негативный тест.Проверка возможности добавление питомца (/api/create_pet_simple) с цифрами\ символами\ буквами вместо цифр в поле age.
    Тест выводит предупреждение. После исправления бага ответ сервера должен быть 400."""

    age = '2#ghfj'

    _, api_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(api_key, name, animal_type, age)

    assert status == 400


# тест 8
def test_get_all_pets_without_valid_key(filter=''):
    """ Проверяем что запрос списка питомцев c неправильным ключем вернет нам статус  403 """

    status, result = pf.get_list_of_pets(invalid_key, filter)

    assert status == 403

# тест 9
def test_add_pet_with_a_lots_symbol_in_animal_type_BUG(name='кракен', age='8'):
    """Негативный тест.
    Добавления питомца с полем "Порода", которое имеет слишком длинное значение.
    Сообщение, если питомец будет добавлен в приложение с названием породы состоящим из 50 символов."""

    animal_type = 'QypIGnMnhFepDelGzbBbuEzxfrPHUvdKsPKlCrApxHSCnchktC'

    _, api_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(api_key, name, animal_type, age)

    list_animal_type = result['animal_type']
    symbol_count = len(list_animal_type)

    assert status == 200
    assert symbol_count > 25
    print(f'\n Баг!!! Добавлен питомец с названием породы породы более \n чем из 25 символов. {symbol_count}')

#тест 9.1
def test_add_pet_with_a_lots_symbol_in_animal_type(name='кракен', age='8'):
    """Проверка возможности добавления питомца с полем "Порода", которое имеет  значение более 50 символов."""

    animal_type = 'QypIGnMnhFepDelGzbBbuEzxfrPHUvdKsPKlCrApxHSCnchktC'

    _, api_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(api_key, name, animal_type, age)

    assert status == 400

#тест 10
def test_add_pet_with_3_digit_age(name='Кэт', animal_type='Кот', pet_photo='images/cat1.jpg'):
    """Добавление питомца с вводом в поле 'age' не более двузначного числа
       БАГ: должен быть статус 400 при вводе более двузначного числа,"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    # pet_photo = os.path.join(os.path.dirname('F:\Python\QAP\pytest_first_test/tests/'), pet_photo)

    age = '999'

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    count = result['age']
    assert status == 400 and len(count) <= 2
    #тут, возможно, перемудрил, скоре всего нужно было 2 теста делать: негативный и позитивный,
    #но точно понятно, что тест будет всегда отваливаться, пока не починят ответ сервера со статусом 400 при вводе
    #числа более 99



