from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from configurations.test_data import TestData



# Instianting Test data Class
test_data = TestData()

class LandingPage(BasePage):
    """Class describes test scripts for Functionality """
                

    def navigate_to_tees(self):
            wait = WebDriverWait(self.driver, 10)
            women_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Women']")))
            women_link.click()
            
            tees_link = self.driver.find_element(By.XPATH, "//a[contains(text(),'Tees')]")
            tees_link.click()