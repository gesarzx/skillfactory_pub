
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome("./chromedriver.exe")
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    pytest.driver.implicitly_wait(5)
    yield
    pytest.driver.quit()

def test_all_my_pets_have_name_age_breed():
    """ Проверяем, что на странице my_pets во всех
     карточках питомцев присутствуют: имя, возраст, порода"""
    pytest.driver.find_element(By.ID, 'email').send_keys('gesarzx@rambler.ru')
    pytest.driver.find_element(By.ID, 'pass').send_keys('qwester')
    # time.sleep(5)
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.find_element(By.LINK_TEXT, u'Мои питомцы').click()
    names = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')))
    breed = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[2]')))
    age = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]')))

    for i in range(len(names)):
        assert names[i].text != ''
        assert breed[i].text != ''
        assert age[i].text != ''

def test_page_contains_all_my_pets():
    """Проверяем, что на странице my_pets есть питомцы"""
    pytest.driver.find_element(By.ID, 'email').send_keys('gesarzx@rambler.ru')
    pytest.driver.find_element(By.ID, 'pass').send_keys('qwester')
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.find_element(By.XPATH, "//a[text()='Мои питомцы']").click()
    # time.sleep(5)
    user_statistics = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'.col-sm-4 left')]")))
    my_pets_qty = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')))
    print(user_statistics.text.split("\n")[1].split(': ')[1])
    print(len(my_pets_qty))
    assert str(len(my_pets_qty)) == user_statistics.text.split("\n")[1].split(': ')[1]

def test_all_my_pets_have_dif_names():
    """Проверяем, что на странице my_pets у всех питомцев разные имена"""
    pytest.driver.find_element(By.ID, 'email').send_keys('gesarzx@rambler.ru')
    pytest.driver.find_element(By.ID, 'pass').send_keys('qwester')
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.find_element(By.XPATH, "//a[text()='Мои питомцы']").click()
    # time.sleep(5)
    names = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')))
    list_names = [names[i].text for i in range(len(names))]
    set_names = set(list_names)
    print(list_names)
    print(set_names)
    assert len(list_names) == len(set_names)

def test_half_my_pets_have_photo():
    """Проверяем, что на странице my_pets хотябы у половины карточек питомцев присутствует фото"""
    pytest.driver.find_element(By.ID, 'email').send_keys('gesarzx@rambler.ru')
    pytest.driver.find_element(By.ID, 'pass').send_keys('qwester')
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.find_element(By.XPATH, "//a[text()='Мои питомцы']").click()
    user_statistics = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'.col-sm-4 left')]")))
    images = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/th/img')))
    # time.sleep(5)
    pets_with_photo = []
    for i in range(len(images)):
        if images[i].get_attribute('src') != "":
            pets_with_photo.append(i)

    pets_qty = int(user_statistics.text.split("\n")[1].split(': ')[1])
    print(pets_qty // 2)
    print(len(pets_with_photo))
    assert pets_qty // 2 <= len(pets_with_photo)

def test_all_my_pets_unique():
    """Проверяем, что на странице my_pets нет повторяющихся карточек питомцев"""
    pytest.driver.find_element(By.ID, 'email').send_keys('gesarzx@rambler.ru')
    pytest.driver.find_element(By.ID, 'pass').send_keys('qwester')
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    pytest.driver.find_element(By.XPATH, "//a[text()='Мои питомцы']").click()
    my_pets_qty = WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')))
    list_pets = [my_pets_qty[i].text.replace(' ', '').lower() for i in range(len(my_pets_qty))]
    set_pets = set(list_pets)
    # time.sleep(5)
    print(list_pets)
    print(set_pets)
    assert len(list_pets) == len(set_pets)
