from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")


class TestLoginPage:

    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    LOGO_LOCATOR = ("xpath", "//div[@class='orangehrm-login-branding']")
    USERNAME_FIELD_LOCATOR = ("xpath", "//div[@class='orangehrm-login-form']//input[@placeholder='Username']")
    PASSWORD_FIELD_LOCATOR = ("xpath", "//div[@class='orangehrm-login-form']//input[@placeholder='Password']")
    LOGIN_BUTTON_LOCATOR = ("xpath", "//div[@class='orangehrm-login-form']//button[@type='submit']")

    def setup_method(self):
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(driver=self.driver, timeout=10, poll_frequency=1)

    def test_open_login_page(self):
        self.driver.get(self.BASE_URL)
        assert self.driver.current_url == self.BASE_URL, "Url is not correct"

    def test_is_logo_displayed(self):
        self.driver.get(self.BASE_URL)
        logo = self.wait.until(EC.visibility_of_element_located(self.LOGO_LOCATOR))
        assert logo.is_displayed() is True, "Logo is not displayed"

    def test_user_login(self):
        self.driver.get(self.BASE_URL)

        username_field = self.wait.until(EC.visibility_of_element_located(self.USERNAME_FIELD_LOCATOR))
        username_field.clear()
        username_field.send_keys("Admin")
        assert "Admin" in username_field.get_attribute("value")

        password_field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD_LOCATOR))
        password_field.clear()
        password_field.send_keys("admin123")
        assert "admin123" in password_field.get_attribute("value")

        login_button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON_LOCATOR))
        login_button.click()
        assert self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index", "Url is not correct. You are not logged in"

    def teardown_method(self):
        self.driver.quit()