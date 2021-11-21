import time
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Test_betester(unittest.TestCase):
    def setUp(self):
        # запуск Chrome при начале каждого 
        self.driver = webdriver.Chrome(r'C:\\Selenium\\chromedriver.exe')
        self.driver.maximize_window()
    
    
    #проверка доступности элемента по редактированию пола пользователя
    def test_auto_reg(self):
        driver = self.driver
        driver.get("http://demo.automationtesting.in/Register.html") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
        login = driver.find_element_by_css_selector("[placeholder='First Name']") # объявляем переменную login, задаём ей значение селектора поля First name
        login.send_keys("Sereja") # команда send_keys(“значение”) – нужна для ввода информации в поле
        password = driver.find_element_by_css_selector("[placeholder='Last Name']") # объявляем переменную password, задаём ей значение селектора поля last name
        password.send_keys("Klassniy") # теперь наглядно видна польза объявленной переменной(не нужно писать driver_find.... .send_keys(..))
        #time.sleep(1)
        email_inp = driver.find_element_by_css_selector("[ng-model='EmailAdress']") # находим поле с емейл адрессом
        email_inp.send_keys("csrfsereja317@mail.ru") # заполняем емейл
        #time.sleep(1)
        phone_inp = driver.find_element_by_css_selector("[ng-model='Phone']")
        phone_inp.send_keys("7999317777")
        gender_inp = driver.find_element_by_css_selector("[value='Male']")#выбираем пол
        gender_inp.click()
        driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(2)
        country_up = driver.find_element_by_id("countries")
        country_up.click()
        country = driver.find_element_by_id("country")#Australia
        #country.send_keys("Australia")
        time.sleep(2)
        country_val = driver.find_element_by_css_selector("[value='Australia']")
        country_val.click()
        year_selecotr = "[id='yearbox']"
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, year_selecotr)))
        #birth_inp = driver.find_element_by_css_selector("[id='yearbox']")# поле с др
        time.sleep(2)
        #birth_inp.click()#клик
        driver.find_element_by_css_selector(year_selecotr).click()
        time.sleep(2)
        val_selector = driver.find_element_by_css_selector("[value='1995']")#находим 1995 год
        val_selector.click()#кликаем
        time.sleep(2)
        month_birth = driver.find_element_by_css_selector("[ng-model='monthbox']")#поле дня рождения с месяцом
        month_birth.click()
        month_val = driver.find_element_by_css_selector("[value='July']")
        month_val.click()
        time.sleep(2)
        day_birth = driver.find_element_by_css_selector("[id='daybox']")
        day_birth.click()
        time.sleep(2)
        day_val = driver.find_element_by_css_selector("[value='7']")
        day_val.click()
        time.sleep(2)
        pass_inp = driver.find_element_by_css_selector("[ng-model='Password']")
        pass_inp.send_keys("Qweshka999")
        conf_pass = driver.find_element_by_css_selector("[ng-model='CPassword']")
        conf_pass.send_keys("Qweshka999")
        file_photo = ("C:\\Users\\1\\Downloads\\339179_big.jpg")
        upload_photo = driver.find_element_by_id("imagesrc")
        upload_photo.send_keys(file_photo)#загружаем фото
        driver.execute_script("window.scrollBy(0, 300);")#скроллим страницу на 300 пикселей вниз
        submit_btn = driver.find_element_by_id("submitbtn")#кнопка отправки
        submit_btn.click()
        time.sleep(2)
        current_page = driver.current_url
        if current_page == "http://demo.automationtesting.in/WebTable.html":
            print("Находимся на нужной странице после регистрации")
        else:
            print("Не верная страница после регистрации")





    




    


    def tearDown(self):
        #закрытие браузера при окончании каждого теста
        self.driver.quit()
 
 
if __name__ == '_main_':
    unittest.main()