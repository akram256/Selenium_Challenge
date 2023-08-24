from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from configurations.test_data import TestData



# Instianting Test data Class
test_data = TestData()

class FilterOptions(BasePage):
    """Class describes test scripts for Functionality """
                
    
    
    
    def filter_options(self):
        wait = WebDriverWait(self.driver, 10)
        size_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='Size']")))
        size_checkbox.click()

        select_large = self.driver.find_element(By.XPATH, "//a[@aria-label='L']//div[contains(@class,'swatch-option text')][normalize-space()='L']")
        select_large.click()
        
        color_checkbox = self.driver.find_element(By.XPATH, "//div[normalize-space()='Color']")
        color_checkbox.click()

        color_select = self.driver.find_element(By.XPATH, "//a[@aria-label='White']//div[contains(@class,'swatch-option color')]")
        color_select.click()
        
        
        click_price = self.driver.find_element(By.XPATH, "//div[normalize-space()='Price']")
        click_price.click()
        
        max_price_input = self.driver.find_element(By.ID, "//span[normalize-space()='$20.00']")
        max_price_input.click()