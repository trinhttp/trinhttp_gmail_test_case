import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from project.pages.Login import LoginGmail
from project.pages.Mail import ComposeEmail
import xlrd
import verify

class LogInGmailAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Game/vsee/Driver/chromedriver.exe")

    def test_01_log_in_url(self):
        url_name = "https://mail.google.com/"
        self.login_to_gmail = LoginGmail(self.driver)
        self.login_to_gmail.open_url(url_name)
        self.assertIn("Gmail", self.driver.title)

    def test_02_input_email_account(self):

        self.email = LoginGmail(self.driver)

        # Get data from the excel file
        excel_file = xlrd.open_workbook("C:/Game/vsee/data/gmail_test_data.xlsx")
        sheet = excel_file.sheet_by_name('input_email_account')
        rows_count = sheet.nrows
        cols_count = sheet.ncols

        # Working with the excel file
        # >>>> 1. Get the list of the first row
        # >>>> 2. Create a dictionary to contain a row data
        # >>>> 3. Loop through the column and get column data into the dictionary

        first_row = []
        for column in range(0, cols_count, 1):
            first_row.append(sheet.cell_value(0,column))
        data = {}
        for row in range(1, rows_count, 1):
            data_in_dic = {}
            for col in range(0, cols_count, 1):
                data_in_dic[first_row[col]] = sheet.cell_value(row, col)
            data.update(data_in_dic) # ===> This will return a dictionary like this {'Code': 'F01', 'Email': '', 'Password': ''}

            self.email.input_email_account(data.get("Email"))
            self.email.click_next_button()
            self.driver.implicitly_wait(3)

            # Test case with corresponding codes on the excel file:
            # F01E: Empty email address
            # F02E: Invalid email address
            # S01E: Valid email address
            if data.get("Code") == "F01E":
                self.assertIn(self.driver.find_element(By.XPATH, "//div[@class='dEOOab RxsGPe']/div[@class='o6cuMc']").get_attribute("innerText"), 'Hãy nhập email hoặc số điện thoại')

            if data.get("Code") == "F02E":
                self.assertIn(self.driver.find_element(By.XPATH, "//div[@class='dEOOab RxsGPe']/div[@class='o6cuMc']").get_attribute("innerText"), 'Nhập tên, email hoặc số điện thoại')

            # if data.get("Code") == "S01E":
            #     self.assertIn(self.driver.find_element(By.XPATH, "//h1/span").get_attribute("innerText"),
            #                   "Chào mừng")

    def test_03_input_password(self):
        self.password = LoginGmail(self.driver)

        # Get data from the excel file
        excel_file = xlrd.open_workbook("C:/Game/vsee/data/gmail_test_data.xlsx")
        sheet = excel_file.sheet_by_name('input_password')
        rows_count = sheet.nrows
        cols_count = sheet.ncols

        # Working with the excel file
        # >>>> 1. Get the list of the first row
        # >>>> 2. Create a dictionary to contain a row data
        # >>>> 3. Loop through the column and get column data into the dictionary

        first_row = []
        for column in range(0, cols_count, 1):
            first_row.append(sheet.cell_value(0, column))
        data = {}
        for row in range(1, rows_count, 1):
            data_in_dic = {}
            for col in range(0, cols_count, 1):
                data_in_dic[first_row[col]] = sheet.cell_value(row, col)
            data.update(data_in_dic)  # ===> This will return a dictionary like this {'Code': 'F01', 'Email': '', 'Password': ''}

            # Input the password information & click next button
            self.password.input_password(data.get("Password"))
            self.password.click_password_next_button()

            # Test case with corresponding codes on the excel file:
            # F01P: Password is empty
            # S01P: Correct password

            if data.get("Code") == "F02P":
                verify.Equal(
                    self.driver.find_element(By.XPATH, "//div[@class='OyEIQ uSvLId']/div[2]/span").get_attribute(
                        "innerText"),
                    'Mật khẩu không chính xác. Hãy thử lại hoặc nhấp vào "Bạn quên mật khẩu" để đặt lại mật khẩu.')

            if data.get("Code") == "S01P":
                self.password.wait_until_successfully_log_in_to_gmail()
                self.assertIn("vsee.test.trinhttp@gmail.com", self.driver.title)

    def test_04_compose_email(self):
        self.compose = ComposeEmail(self.driver)

        excel_file = xlrd.open_workbook("C:/Game/vsee/data/gmail_test_data.xlsx")
        sheet = excel_file.sheet_by_name('compose_email')
        rows_count = sheet.nrows
        cols_count = sheet.ncols

        first_row = []
        for column in range(0, cols_count, 1):
            first_row.append(sheet.cell_value(0, column))
        data = {}
        for row in range(1, rows_count, 1):
            data_in_dic = {}
            for col in range(0, cols_count, 1):
                data_in_dic[first_row[col]] = sheet.cell_value(row, col)
            data.update(data_in_dic)  # ===> This will return a dictionary like this {'Code': 'F01', 'Email': '', 'Password': ''}

            self.compose.click_compose_button()
            self.compose.compose_email(data.get("To"), data.get("Subject"), data.get("Content"))
            self.compose.click_send_email_button()
            self.driver.implicitly_wait(5)

            # Test case with corresponding codes on the excel file:
            # F01C: Recipient is empty
            # F02C: Invalid recipient
            # S01C: Valid recipient, empty subject, empty content
            # S02C: Valid recipient, subject was inputted, empty content
            # S03C: Valid recipient, subject and content was inputted

            if data.get("Code") == "F01C":
                self.assertIn(self.driver.find_element(By.XPATH, "//div[@role='alertdialog']/div[@class='Kj-JD-Jz']").get_attribute("innerText"),
                              ["Please specify at least one recipient.", "Hãy chỉ định ít nhất một người nhận."])
                self.compose.click_ok_button()
                self.compose.click_close_email_box()

            if data.get("Code") == "F02C":
                self.assertIn(self.driver.find_element(By.XPATH,"//div[@role='alertdialog']/div[@class='Kj-JD-Jz']").get_attribute("innerText"),
                              ["The address \"%s\" in the \"To\" field was not recognized. Please make sure that all addresses are properly formed." % data.get("To"),
                               "Không nhận dạng được địa chỉ \"%s\" trong trường \"Đến\". Vui lòng đảm bảo rằng tất cả địa chỉ đều được định dạng đúng." % data.get("To")] )
                self.compose.click_ok_button()
                self.compose.click_close_email_box()

            if data.get("Code") == "S01C":
                alert = self.compose.driver.switch_to_alert()
                # alert_mes = alert.text()
                # self.assertIn(alert_mes, "Gửi thư này mà không có chủ đề hoặc nội dung thư?")
                alert.accept()
                self.assertIn(self.driver.find_element(By.XPATH,"//div[@class='vh']/span[@class='aT']/span[@class='bAq']").get_attribute("innerText"), "Đang gửi...")

            if data.get("Code") == "S02C" and "S03C":
                self.assertIn(self.driver.find_element(By.XPATH,"//div[@class='vh']/span[@class='aT']/span[@class='bAq']").get_attribute("innerText"), "Đang gửi...")

    def tearDown(self):
        self.driver.quit()