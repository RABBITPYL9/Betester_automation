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
        path_to_extension = r'C:\\Users\\1\\AppData\\Local\\Google\\Chrome\\User Data\Default\\Extensions\\gighmmpiobklfepjocnamgkkbiglidom\\4.40.0_0'
        chrome_options = Options()
        chrome_options.add_argument('load-extension=' + path_to_extension)
        self.driver = webdriver.Chrome(r'C:\\Selenium\\chromedriver.exe', chrome_options=chrome_options)
        self.driver.implicitly_wait(50)
        #self.driver.create_options()
        self.driver.maximize_window()
    
    
    #проверка доступности элемента по редактированию пола пользователя
    def test_auto_reg(self):
        driver = self.driver
        #driver.implicitly_wait(200)
        driver.get("http://demo.automationtesting.in/WebTable.html") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
        vkladka = driver.find_element_by_xpath(".//a[text() = 'More']") # объявляем переменную vkladka для поиска ссылки More
        vkladka.click()
        vkladka_jq = driver.find_element_by_xpath(".//a[text() = 'JQuery ProgressBar']")#переходим на вкладку JQ
        vkladka_jq.click()
        #invisibility_of_element_located(locator)
        inv_btn = WebDriverWait(driver, 20).until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, "[type='button']:nth-child(1)")))#кнопка клоз невидима
        dwn_btn = driver.find_element_by_css_selector("#downloadButton:nth-child(1)")#кнопка старта загрузки
        dwn_btn.click()
        cancel_btn = WebDriverWait(driver, 20).until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, "//*[text()='Cancel Download']")))#ожидем клавишу отмены загрузки с названием Cancel Download
        close_click = driver.find_element_by_css_selector("[type='button']:nth-child(1)")
        close_click.click()
        dwn_btn1 = driver.find_element_by_css_selector("#downloadButton:nth-child(1)")#кнопка старта загрузки
        dwn_btn1.click()
        status_bar = WebDriverWait(driver, 20).until(expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, "//*[text()='Complete!']")))#ожидаем текст комплит




        

