import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestJokes:

    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    USERNAME_FIELD_LOCATOR = ("xpath", "//div[@class='orangehrm-login-form']//input[@placeholder='Username']")
    PASSWORD_FIELD_LOCATOR = ("xpath", "//div[@class='orangehrm-login-form']//input[@placeholder='Password']")
    LOGIN_BUTTON_LOCATOR = ("xpath", "//div[@class='orangehrm-login-form']//button[@type='submit']")

    # Menu
    BUZZ_BUTTON_LOCATOR = ("xpath", "//ul[@class='oxd-main-menu']/li//span[text()='Buzz']")

    SUCCESS_ALERT_LOCATOR = ("xpath", "//div[@aria-live='assertive']//div[contains(@class, '-wrap--success')]")

    # Buzz News Feed
    POST_INPUT_LOCATOR = ("xpath", "//div[@class='orangehrm-buzz-newsfeed']//textarea")
    POST_BUTTON_LOCATOR = ("xpath", "//div[@class='orangehrm-buzz-newsfeed']//button[@type='submit']")
    POST_CARD_LOCATOR = ("xpath", "//div[contains(@class, '--rounded oxd-sheet--white')]")
    post_text_locator = lambda self, post_text: ("xpath", f"//p[contains(@class, 'orangehrm-buzz-post-body-text') and text()='{post_text}']")

    def setup_method(self):
        self.wait = WebDriverWait(driver=self.driver, timeout=10, poll_frequency=1)
        self.driver.get(self.BASE_URL)

        username_field = self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD_LOCATOR))
        username_field.clear()
        username_field.send_keys("Admin")
        assert "Admin" in username_field.get_attribute("value"), "The username field does not contain 'Admin'"

        password_field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD_LOCATOR))
        password_field.clear()
        password_field.send_keys("admin123")
        assert "admin123" in password_field.get_attribute("value"), "The password field does not contain 'admin123'"

        login_button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON_LOCATOR))
        login_button.click()

    def test_post_jokes(self, get_joke):
        self.wait.until(EC.element_to_be_clickable(self.BUZZ_BUTTON_LOCATOR)).click()
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz", "Incorrect URL"

        post_input_field = self.wait.until(EC.element_to_be_clickable(self.POST_INPUT_LOCATOR))
        post_input_field.clear()
        post_text = get_joke
        post_input_field.send_keys(post_text)
        assert post_text in post_input_field.get_attribute("value")

        post_button = self.wait.until(EC.element_to_be_clickable(self.POST_BUTTON_LOCATOR))
        post_button.click()
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_ALERT_LOCATOR))
        self.wait.until(EC.invisibility_of_element_located(self.SUCCESS_ALERT_LOCATOR))

        created_post_text = self.driver.find_element(*self.post_text_locator(post_text))
        assert post_text == created_post_text.text
        