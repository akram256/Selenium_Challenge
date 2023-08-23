# from selenium.common.exceptions import NoSuchElementException
import time
from configurations.test_data import TestData
from utilities.custom_logger import LogGen

from page_objects.functionality import MagentoFunctionality
from test_cases.configtest import setup

base_url = TestData.base_url
logger = LogGen.loggen()
    
class TestFunctionality:
    """Class describes the methods to test cases"""

    def test_challenge_functionality(self, setup):
        """This methods tests functionality of the application"""

        self.driver = setup
        self.driver.get(base_url)
        logger.info("*************Test Cases running**********************")

        
        #instatianting the page object class
        page_obj = MagentoFunctionality(self.driver)
    
        page_title = self.driver.title
        if page_title == TestData.home_page_title:
            
            page_obj.click_signin_on_landingpage()
            page_obj.signin_submit() 
            page_obj.navigate_to_tees()
            page_obj.filter_options()
            page_obj.add_to_cart()
            page_obj.proceed_to_checkout()
            page_obj.verify_cart_subtotal()
            page_obj.verify_order_summary()
            page_obj.print_values()
            
            time.sleep(10) 
           
        else:
            logger.error("***Tests  Fialed***")
            self.driver.save_screenshot("../screenshots/test_challenge3.png")
        self.driver.quit()


