    
    
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
from configurations.test_data import TestData



# Instianting Test data Class
test_data = TestData()

class Cart(BasePage):
    """Class describes test scripts for Functionality """
                   
    
    def add_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        item = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to Cart']")))
        item.click()
        
        show_items = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='action showcart']")))
        show_items.click()
   
        quantity_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='cart-item-309913-qty']")))
        quantity_input.clear()
        quantity_input.send_keys("3")
        
        
        add_to_cart_button = self.driver.find_element(By.ID, "product-addtocart-button")
        add_to_cart_button.click()
        
    def proceed_to_checkout(self):
        wait = WebDriverWait(self.driver, 10)
        proceed_to_checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='top-cart-btn-checkout']")))
        proceed_to_checkout_button.click()


    def verify_cart_subtotal(self):
        wait = WebDriverWait(self.driver, 10)
        cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[title='View your shopping cart']")))
        cart_icon.click()

        cart_subtotal = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".totals .price")))
        print(f"Cart Subtotal: {cart_subtotal.text}")

    def verify_shipping(self):
        wait = WebDriverWait(self.driver, 10)
        shipping_address = wait.until(EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Shipping Address']")))
        print(f"Shipping Address: {shipping_address.text}")

        shipping_methods = self.driver.find_elements(By.XPATH, "//div[normalize-space()='Shipping Methods']")
        print("Shipping Methods:")
        for method in shipping_methods:
            print(method.text)

        next_button = self.driver.find_element(By.ID, "shipping-method-buttons-container")
        next_button.click()

    def verify_order_summary(self):
        wait = WebDriverWait(self.driver, 10)
        cart_subtotal = self.driver.find_element(By.CSS_SELECTOR, "#subtotal span.price")
        shipping_cost = self.driver.find_element(By.CSS_SELECTOR, "#shipping .price")
        order_total = self.driver.find_element(By.CSS_SELECTOR, "#grand_total .price")

        print(f"Cart Subtotal: {cart_subtotal.text}")
        print(f"Shipping Cost: {shipping_cost.text}")
        print(f"Order Total: {order_total.text}")

        view_details_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@title, 'View Details')]")))
        view_details_button.click()

    def print_values(self):
        quantity = self.driver.find_element(By.CSS_SELECTOR, ".product-cart-actions input[name='qty']")
        size = self.driver.find_element(By.ID, "attribute90")
        color = self.driver.find_element(By.ID, "attribute178")

        print(f"Quantity: {quantity.get_attribute('value')}")
        print(f"Size: {size.get_attribute('value')}")
        print(f"Color: {color.get_attribute('value')}")

        cart_subtotal = self.driver.find_element(By.CSS_SELECTOR, "#td-subtotal .price")
        shipping_cost = self.driver.find_element(By.CSS_SELECTOR, "#td-shipping .price")
        order_total = self.driver.find_element(By.CSS_SELECTOR, "#td-grand_total .price")

        print(f"Total Cart Subtotal: {cart_subtotal.text}")
        print(f"Shipping Cost: {shipping_cost.text}")
        print(f"Total Order Total: {order_total.text}")
