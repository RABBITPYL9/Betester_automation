import time
from selenium import webdriver # импортируем webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Be_tester(unittest.TestCase):
    def setUp(self):
        # запуск Chrome при начале каждого теста
        self.driver = webdriver.Chrome(r'C:\\Selenium\\chromedriver.exe')


    def test_login(self):#тест входа и выхода из системы
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
        login = driver.find_element_by_css_selector("[name='txtUsername']") # объявляем переменную login, задаём ей значение селектора поля логин
        login.send_keys("Admin") # команда send_keys(“значение”) – нужна для ввода информации в поле
        password = driver.find_element_by_css_selector("[name='txtPassword']") # объявляем переменную password, задаём ей значение селектора поля пароль
        password.send_keys("admin123") # теперь наглядно видна польза объявленной переменной(не нужно писать driver_find.... .send_keys(..))
        time.sleep(4)
        login_btn = driver.find_element_by_css_selector("#btnLogin:nth-child(1)") # объявляем переменную login_btn, задаём ей значение селектора кнопки логин (btn сокращ. от button)
        login_btn.submit() # команда click() – нужна для нажатия(клика) на элемент
        time.sleep(4)
        check_lgn = driver.find_element_by_css_selector("#menu_admin_viewAdminModule")#проверяем что вошли, такое меню дступно только после входа
        check_lgn.click()
        time.sleep(2)
        check_for_log = driver.find_element_by_css_selector("#welcome:nth-child(2)")
        check_for_log.click()
        time.sleep(2)
        logout = driver.find_element_by_xpath("//*[text()='Logout']")#нажимаем кнопку выхода
        logout.click()
        self.assertNotIn("Welcome", driver.page_source)#проевка отсутствие текста приветствия после выхода


    def test_add_user(self):#тест создания пользователя
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
        login = driver.find_element_by_css_selector("[name='txtUsername']") # объявляем переменную login, задаём ей значение селектора поля логин
        login.send_keys("Admin") # команда send_keys(“значение”) – нужна для ввода информации в поле
        password = driver.find_element_by_css_selector("[name='txtPassword']") # объявляем переменную password, задаём ей значение селектора поля пароль
        password.send_keys("admin123") # теперь наглядно видна польза объявленной переменной(не нужно писать driver_find.... .send_keys(..))
        time.sleep(2)
        login_btn = driver.find_element_by_css_selector("#btnLogin:nth-child(1)") # объявляем переменную login_btn, задаём ей значение селектора кнопки логин (btn сокращ. от button)
        login_btn.submit() # команда click() – нужна для нажатия(клика) на элемент
        time.sleep(2)
        pim_menu = driver.find_element_by_css_selector("#menu_pim_viewPimModule")#переход в список пользователей
        pim_menu.click()
        time.sleep(2)
        emp_list = driver.find_element_by_css_selector("#menu_pim_addEmployee")#кнопка добавления пользователя
        emp_list.click()
        f_name = driver.find_element_by_css_selector("#firstName")#находим поле ввода имени
        f_name.send_keys("Sereja")
        l_name = driver.find_element_by_css_selector("#lastName")#находим поле ввода фамилии
        l_name.send_keys("Volshebniy")
        save_btn = driver.find_element_by_css_selector("#btnSave")#находим кнопку сохранения
        save_btn.submit()
        #urlik = driver.current_url#получаем id пользователя, так как для удаления в значении атрибута в чекбоксе id каждый раз разный
        #get_id_from_url = urlik[-2:]
        #time.sleep(2)
        #Be_tester.generate_id_emp = '#ohrmList_chkSelectRecord_' + str(get_id_from_url)#генерим css selecotr пользователя для его удаления
    
    def test_user_remove(self):
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
        time.sleep(1)
        emp_list = driver.find_element_by_css_selector("[name='empsearch[employee_name][empName]']")#находим поля для ввода имени
        emp_list.send_keys("Sereja")
        time.sleep(1)
        clear_emp = driver.find_element_by_css_selector("[name='empsearch[id]']")#очищаем соседнее поле с id
        clear_emp.clear()
        clear_emp2 = driver.find_element_by_css_selector("[name='empsearch[supervisor_name]']")#очищаем соседнее поле
        clear_emp2.clear()
        search_emp = driver.find_element_by_css_selector("#searchBtn:nth-child(1)")#нажимаем кнопку поиска
        search_emp.submit()
        time.sleep(1)
        del_emp = driver.find_element_by_name("chkSelectAll")#выбираем пользователей для удаления в селекторе
        del_emp.click()
        delete_btn = driver.find_element_by_id("btnDelete")#удаляем
        delete_btn.click()
        time.sleep(1)
        ok_btn = driver.find_element_by_css_selector("#dialogDeleteBtn")#в диалоговом окне соглашаемся с удалением
        ok_btn.click()
        driver.close()


    def tearDown(self):
        #закрытие браузера при окончании каждого теста
        self.driver.close()
 
 
if _name_ == '_main_':
    unittest.main()