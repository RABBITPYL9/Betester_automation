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
        vkladka_alerts = driver.find_element_by_xpath(".//a[text() = 'File Upload']")#переходим на вкладку File Upload
        vkladka_alerts.click()
        file_photo = ("C:\\Users\\1\\Downloads\\339179_big.jpg")
        upload_photo = driver.find_element_by_css_selector("div>#input-4")
        upload_photo.send_keys(file_photo)#загружаем фото
        del_click = driver.find_element_by_css_selector("div>[title='Clear selected files']")
        del_click.click()
        file_photo = ("C:\\Users\\1\\Downloads\\test.txt")
        upload_photo = driver.find_element_by_css_selector("div>#input-4")
        upload_photo.send_keys(file_photo)#загружаем фото
        red_close = driver.find_element_by_css_selector("[class='close kv-error-close']")
        red_close.click()
        checked_upload = driver.find_element_by_css_selector("[title='Upload selected files']")#находим что установлена последняя страна в списке
        checked_upload = checked_upload.get_attribute("disabled")
        

