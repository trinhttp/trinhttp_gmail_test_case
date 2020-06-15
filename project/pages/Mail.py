from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ComposeEmail():
    def __init__(self, driver):
        self.driver = driver
        self.compose_button_xpath = "//div[@class='T-I J-J5-Ji T-I-KE L3' and @role='button']"
        self.wait_10_seconds = WebDriverWait(driver, 10)
        self.wait_60_seconds = WebDriverWait(driver, 60)
        self.send_button_xpath = "//div[@class='dC']/div[@class='T-I J-J5-Ji aoO v7 T-I-atl L3' and @role='button']"
        self.receiver_email_name = "to"
        self.email_subject_name = "subjectbox"
        self.email_content_xpath = "//div[@class='Am Al editable LW-avf tS-tW' and @role ='textbox']"
        self.close_email_box_xpath = "//td/img[@class='Ha']"
        self.ok_button_name = "ok"

    def click_compose_button(self):
        self.wait_10_seconds.until(EC.element_to_be_clickable((By.XPATH, self.compose_button_xpath)))
        self.driver.find_element_by_xpath(self.compose_button_xpath).click()

    def compose_email(self, to, subject, content):
        self.wait_60_seconds.until(EC.element_to_be_clickable((By.XPATH, self.send_button_xpath)))
        self.driver.find_element_by_name(self.receiver_email_name).send_keys(to)
        self.driver.find_element_by_name(self.email_subject_name).send_keys(subject)
        self.driver.find_element_by_xpath(self.email_content_xpath).send_keys(content)

    def click_send_email_button(self):
        self.driver.find_element_by_xpath(self.send_button_xpath).click()

    def click_ok_button(self):
        self.driver.find_element_by_name(self.ok_button_name).click()

    def click_close_email_box(self):
        self.driver.find_element_by_xpath(self.close_email_box_xpath).click()

