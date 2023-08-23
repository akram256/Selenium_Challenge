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

    def test_sigin_functionality(self, setup):
        """This methods tests functionality of the application"""

        self.driver = setup
        self.driver.get(base_url)
        logger.info("**********Landing Page*******")
        logger.info("*************Test Case  001**********************")

        
        #instatianting the page object class
        landing_page = MagentoFunctionality(self.driver)
    
        page_title = self.driver.title
        if page_title == TestData.home_page_title:
            
            landing_page.click_signin_on_landingpage()
            landing_page.signin_submit() 
            landing_page.navigate_to_tees()
            landing_page.filter_options()
            landing_page.add_to_cart()
            landing_page.proceed_to_checkout()
            landing_page.verify_cart_subtotal()
            landing_page.verify_order_summary()
            landing_page.print_values()
            
            time.sleep(10) 
           
        else:
            logger.error("***Uichecks  Fialed***")
            self.driver.save_screenshot("../screenshots/test_challenge3.png")
        self.driver.quit()


