from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from configurations.test_data import TestData



# Instianting Test data Class
test_data = TestData()

class SignIn(BasePage):
    """Class describes test scripts for Functionality """
                
    def click_signin_on_landingpage(self):
        SignIn_xpath = "//div[@class='panel header']//a[contains(text(),'Sign In')]"
        wait = WebDriverWait(self.driver, 10)
        element = SignIn_xpath
        sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, element)))
        sign_in_button.click()
        

    def signin_submit(self):
        username = test_data.username
        password = test_data.password
       
        wait = WebDriverWait(self.driver, 10)
                
        username_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']")))
        password_field = self.driver.find_element(By.XPATH, "//fieldset[@class='fieldset login']//input[@id='pass']")
        sign_in_submit = self.driver.find_element(By.XPATH, "//fieldset[@class='fieldset login']//span[contains(text(),'Sign In')]")
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        sign_in_submit.click()
        