import time
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

class Test_betester(unittest.TestCase):
    def setUp(self):
        # запуск Chrome при начале каждого
        #path_to_extension = r'C:\\Users\\1\\AppData\\Local\\Google\\Chrome\\User Data\Default\\Extensions\\gighmmpiobklfepjocnamgkkbiglidom\\4.40.0_0'
        #chrome_options = Options()
        #chrome_options.add_argument('load-extension=' + path_to_extension)
        self.driver = webdriver.Chrome(r'C:\\Selenium\\chromedriver.exe')#, chrome_options=chrome_options)
        self.driver.implicitly_wait(50)
        #self.driver.create_options()
        self.driver.maximize_window()
    
    
    #проверка доступности элемента по редактированию пола пользователя
    def test_auto_reg(self):
        driver = self.driver
        #driver.implicitly_wait(200)
        driver.get("http://demo.automationtesting.in/WebTable.html") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
        vkladka = driver.find_element_by_xpath(".//a[text() = 'SwitchTo']") # объявляем переменную vkladka для поиска ссылки SwitchTo
        vkladka.click()
        vkladka_alerts = driver.find_element_by_xpath(".//a[text() = 'Windows']")#переходим на вкладку windows
        vkladka_alerts.click()
        #invisibility_of_element_located(locator)
        click_btn = driver.find_element_by_css_selector(".btn-info:nth-child(1)")
        click_btn.click()
        driver.execute_script("window.open();") # открытие новой вкладки
        window_after = driver.window_handles[1] # создание переменной, где укажем путь к второй вкладке (window_handles[1]) ; здесь будет 1, так как отсчёт начинается с 0
        driver.switch_to.window(window_after)
        driver.close()
        window_before = driver.window_handles[0]
        driver.switch_to.window(window_before)
        #move_menu = driver.find_element_by_css_selector("[aria-expanded='true']")
        #move_menu.click()
        url_click = driver.execute_script('window.open("Index.html");')
        #url_btn_click = driver.execute_script('window.open("http://www.selenium.dev/");')
        window_open = driver.window_handles[2]
        driver.switch_to.window(window_open)
        WebDriverWait(driver, 50).until(expected_conditions.url_to_be("http://demo.automationtesting.in/Index.html"))


        