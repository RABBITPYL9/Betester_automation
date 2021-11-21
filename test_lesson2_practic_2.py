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
        vkladka_alerts = driver.find_element_by_xpath(".//a[text() = 'Dynamic Data']")#переходим на вкладку Dynamic Data
        vkladka_alerts.click()
        run_btn = driver.find_element_by_css_selector("[class='cont_box_center'] > h3")
        #print(run_btn)
        #print(run_btn)
        #assertik = WebDriverWait(driver, 50).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[class='cont_box_center'] > h3")))
        modal_windows_text = run_btn.text
        assert "Loading the data Dynamically" in modal_windows_text
        get_btn = driver.find_element_by_css_selector("div>#save")
        get_btn.click()
        time.sleep(9)
        img = driver.find_element_by_css_selector("#loading>img")
        val = img.get_attribute("src")
        print(val)