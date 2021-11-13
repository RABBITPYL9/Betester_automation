import time
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Be_tester(unittest.TestCase):
    def setUp(self):
        # запуск Chrome при начале каждого теста
        self.driver = webdriver.Chrome(r'C:\\Selenium\\chromedriver.exe')
    
    
    #проверка доступности элемента по редактированию пола пользователя
    def test_gender(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
        login = driver.find_element_by_css_selector("[name='txtUsername']") # объявляем переменную login, задаём ей значение селектора поля логин
        login.send_keys("Admin") # команда send_keys(“значение”) – нужна для ввода информации в поле
        password = driver.find_element_by_css_selector("[name='txtPassword']") # объявляем переменную password, задаём ей значение селектора поля пароль
        password.send_keys("admin123") # теперь наглядно видна польза объявленной переменной(не нужно писать driver_find.... .send_keys(..))
        time.sleep(1)
        login_btn = driver.find_element_by_css_selector("#btnLogin:nth-child(1)") # объявляем переменную login_btn, задаём ей значение селектора кнопки логин (btn сокращ. от button)
        login_btn.submit() # команда click() – нужна для нажатия(клика) на элемент
        time.sleep(1)
        pim_menu = driver.find_element_by_css_selector("#menu_pim_viewPimModule")
        pim_menu.click()
        search_emp = driver.find_element_by_xpath(".//a[text() = 'Ananya']")
        search_emp.click()#Переходим на страницу пользователя с ником Ananya
        scheduled = driver.find_element_by_id("personal_optGender_1")#проверяем что до нажатия кнопки EDIT выбор пола(противоположного) не активен
        scheduled_checked = scheduled.get_attribute("disabled")
        if scheduled_checked is None:
            print("Атрибута нет")
        else:
            print("Атрибут есть")
        click_edit = driver.find_element_by_css_selector("#btnSave:nth-child(1)")#Находим кнопку edit
        click_edit.click()#Жмем кнопку edit
        click_gender = driver.find_element_by_css_selector("[value='1']:nth-child(1)")#Находим противоположный пол
        click_gender.click()
        checked_gender_val = driver.find_element_by_id("personal_optGender_2")#проверяем новое значени для пола
        checked_gender_val = checked_gender_val.get_attribute("checked")
        click_selector = driver.find_element_by_id("personal_cmbNation")#находим селектор с выбором страны и нажимаем
        click_selector.click()
        val_selector = driver.find_element_by_css_selector("[value='193']").click()#Выбираем америку
    




    


    def tearDown(self):
        #закрытие браузера при окончании каждого теста
        self.driver.close()
 
 
if _name_ == '_main_':
    unittest.main()