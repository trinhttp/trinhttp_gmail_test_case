from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import xlrd

class LoginGmail():
    def __init__(self, driver):
        self.driver = driver
        self.email_account_id = "identifierId"
        self.next_button_id = "identifierNext"
        self.wait_10_seconds = WebDriverWait(driver, 10)
        self.wait_30_seconds = WebDriverWait(driver, 30)
        self.recheck_email_account_id = "profileIdentifier"
        self.password_name = "password"
        self.password_next_button_id = "passwordNext"
        self.empty_email_xpath ="//div[@class='o6cuMc']"
        self.gmail_link_text = "#inbox"
        self.compose_button_xpath = "//div[@class='T-I J-J5-Ji T-I-KE L3' and @role='button']"

    def open_url(self,url_name):
        self.driver.get(url_name)

    def input_email_account(self, email_account):
        self.driver.find_element_by_id(self.email_account_id).clear()
        self.driver.find_element_by_id(self.email_account_id).send_keys(email_account)

    def check_empty_email_account(self):
        return self.driver.find_element(By.XPATH(self.empty_email_xpath)).getText()

    def click_next_button(self):
        self.wait_10_seconds.until(EC.element_to_be_clickable((By.ID, self.next_button_id)))
        self.driver.find_element_by_id(self.next_button_id).click()

    def recheck_email_account_name(self):
        self.driver.find_element_by_id(self.recheck_email_account_id).getText()

    def input_password(self, password):
        self.wait_10_seconds.until(EC.element_to_be_clickable((By.NAME, self.password_name)))
        self.driver.find_element_by_name(self.password_name).clear()
        self.driver.find_element_by_name(self.password_name).send_keys(password)

    def click_password_next_button(self):
        self.wait_10_seconds.until(EC.element_to_be_clickable((By.ID, self.password_next_button_id)))
        self.driver.find_element_by_id(self.password_next_button_id).click()

    def check_if_password_text_box_is_present(self):
        try:
            self.driver.find_element_by_name(self.password_name)
        except NoSuchElementException:
            return False
        return True

    def wait_until_successfully_log_in_to_gmail(self):
        self.wait_30_seconds.until(EC.element_to_be_clickable((By.XPATH, self.compose_button_xpath)))
