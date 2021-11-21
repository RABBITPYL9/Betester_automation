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
        self.driver.create_options()
        self.driver.maximize_window()
    
    
    #проверка доступности элемента по редактированию пола пользователя
    def test_auto_reg(self):
        driver = self.driver
        driver.get("http://demo.automationtesting.in/WebTable.html") # метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
        vkladka = driver.find_element_by_xpath(".//a[text() = 'SwitchTo']") # объявляем переменную vkladka для поиска ссылки SwitchTo
        vkladka.click()
        vkladka_alerts = driver.find_element_by_xpath(".//a[text() = 'Alerts']")#переходим на вкладку Alerts
        vkladka_alerts.click()
        time.sleep(2)
        alert_btn = driver.find_element_by_css_selector("#OKTab:nth-child(1)")#находим кнопку с алертом
        alert_btn.click()
        confirm = driver.switch_to.alert
        alert_text = confirm.text
        print(alert_text)#выводим текст алерта
        confirm.accept()#соглашаемся с алертом
        if alert_text == "I am an alert box!":
            print("Текст на алерте совпадает с нашим значением")
        else:
            print("Текст на алерте не совпадает")
        current_page = driver.current_url#получаем адресс текущей страницы
        
        driver.execute_script("window.open();") # открытие новой вкладки
        window_after = driver.window_handles[1] # создание переменной, где укажем путь к второй вкладке (window_handles[1]) ; здесь будет 1, так как отсчёт начинается с 0
        driver.switch_to.window(window_after) # переключим область действия драйвера на новую вкладку, теперь дальнейшие элементы драйвер будет искать уже там
        time.sleep(2)
        driver.get(current_page) # на новой вкладке откроем страницу из шага 6 третьего урока.
        print(current_page)
        second_vkladka = driver.find_element_by_xpath("//*[text()='Alert with OK & Cancel ']")
        second_vkladka.click()
        time.sleep(2)
        alert_btn_with_cancel = driver.find_element_by_css_selector("#CancelTab:nth-child(2)")#кнопка с алертом
        alert_btn_with_cancel.click()
        decline = driver.switch_to.alert
        decline.dismiss()
        driver.execute_script("window.open();") # открытие новой вкладки
        window_after2 = driver.window_handles[1] # создание переменной, где укажем путь к второй вкладке (window_handles[1]) ; здесь будет 1, так как отсчёт начинается с 0
        driver.switch_to.window(window_after2) # переключим область действия драйвера на новую вкладку, теперь дальнейшие элементы драйвер будет искать уже там
        time.sleep(2)
        driver.get(current_page)
        third_vkladka = driver.find_element_by_xpath("//*[text()='Alert with Textbox ']")
        third_vkladka.click()
        third_btn = driver.find_element_by_css_selector("[onclick='promptbox()']")#находим кнопку с алертом
        third_btn.click()
        prompt = driver.switch_to.alert
        prompt.send_keys("Ура! Задание выполнено!")
        prompt.accept()
        

        

 




    




    


    def tearDown(self):
        #закрытие браузера при окончании каждого теста
        self.driver.quit()
 
 
if __name__ == '_main_':
    unittest.main()