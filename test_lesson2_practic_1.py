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
        self.driver = webdriver.Chrome(r'C:\\Selenium\\chromedriver.exe')
        #self.driver.create_options()
        self.driver.maximize_window()
    
    
    #проверка доступности элемента по редактированию пола пользователя
    def test_auto_reg(self):
        driver = self.driver
        #driver.implicitly_wait(200)
        driver.get("http://demo.automationtesting.in/Loader.html") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
        vkladka = driver.find_element_by_xpath(".//a[text() = 'More']") # объявляем переменную vkladka для поиска ссылки More
        vkladka.click()
        vkladka_alerts = driver.find_element_by_xpath(".//a[text() = 'Loader']")#переходим на вкладку Loader
        vkladka_alerts.click()
        run_btn = driver.find_element_by_css_selector("#loader:nth-child(1)")
        run_btn.click()
        modal_windows = "[class='modal-body']"
        assertik = WebDriverWait(driver, 50).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, modal_windows)))
        #time.sleep(20)
        #modal_windows = driver.find_element_by_css_selector("[class='modal-title']")
        modal_windows_text = assertik.text
        assert "Lorem" in modal_windows_text
        save_changes_btn = driver.find_element_by_css_selector("[onclick='history.go(0)']")
        save_changes_btn.click()