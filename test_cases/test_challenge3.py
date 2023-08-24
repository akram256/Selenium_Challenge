# from selenium.common.exceptions import NoSuchElementException
import time
from configurations.test_data import TestData
from utilities.custom_logger import LogGen
from test_cases.configtest import setup
from page_objects.filters import FilterOptions
from page_objects.cart import Cart
from page_objects.signin import SignIn
from page_objects.landingpage import LandingPage
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
        signin = SignIn(self.driver)
        landing_page = LandingPage(self.driver)
        filter_page = FilterOptions(self.driver)
        cart_page = Cart(self.driver)
        page_title = self.driver.title
        if page_title == TestData.home_page_title:
            
            signin.click_signin_on_landingpage()
            signin.signin_submit() 
            landing_page.navigate_to_tees()
            filter_page.filter_options()
            cart_page.add_to_cart()
            cart_page.proceed_to_checkout()
            cart_page.verify_cart_subtotal()
            cart_page.verify_order_summary()
            cart_page.print_values()
            
            time.sleep(10) 
           
        else:
            logger.error("***Tests  Fialed***")
            self.driver.save_screenshot("../screenshots/test_challenge3.png")
        self.driver.quit()


