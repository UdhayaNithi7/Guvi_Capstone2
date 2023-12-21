from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from Data2 import data2
from Locator2 import locator2
from time import time

class Test_Capstoneorg:

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 40)
        self.driver.get(locator2.Orange_locat2().url)
        self.driver.maximize_window()
        yield
        self.driver.close()

    # Getting the Resetting Password Message on Display

    def test_resetpassword(self, booting_function):

        try:
            forgot_password_link = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locator2.Orange_locat2().forgot_password)))
            forgot_password_link.click()

            UserName = self.wait.until(
                EC.element_to_be_clickable((By.NAME, locator2.Orange_locat2.username_in_forgot_password)))
            UserName.click()
            username_data = org.access_data(2, 4)
            UserName.send_keys(username_data)

            reset = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locator2.Orange_locat2().reset_button))).click()
            

            message_on_screen = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locator2.Orange_locat2().reset_message))).text
            expected_data = org.access_data(2, 6)

            if expected_data in message_on_screen:
                org.write_data(2, 7, "Data Matched")
                screenshot_directory = r"E:\Automation Testing\\practice\\Task\\Capstone_02\\screenshots2\\"
                screenshot_filename = "resetpassword.png"
                screenshot_path = f"{screenshot_directory}{screenshot_filename}"
                self.driver.save_screenshot(screenshot_path)
                assert expected_data == message_on_screen
                print("Reseting Message displayed: ", message_on_screen)

            else:
                org.write_data(2, 7, "Data Not Matched")
                screenshot_directory = r"E:\Automation Testing\\practice\\Task\\Capstone_02\\screenshots2\\"
                screenshot_filename = "resetpassword.png"
                screenshot_path = f"{screenshot_directory}{screenshot_filename}"
                self.driver.save_screenshot(screenshot_path)
                print("Reseting Message displayed: ", message_on_screen)

        except Exception as e:
            print("error on: ",e)

     # Common Login Function for using the test cases        

    @pytest.fixture
    def test_login(self, booting_function):

        try:
            username1 = self.wait.until(
                EC.element_to_be_clickable((By.NAME, locator2.Orange_locat2().username_in_launchpage)))
            username1.click()
            username1_data = org.access_data(3, 4)
            username1.send_keys(username1_data)

            password1 = self.wait.until(
                EC.element_to_be_clickable((By.NAME, locator2.Orange_locat2().password_in_launchpage)))
            password1.click()
            password1_data = org.access_data(3, 5)
            password1.send_keys(password1_data)

            submit_button =  self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator2.Orange_locat2().login_button)))
            submit_button.click()
        except Exception as e:
            print("login error on : ", e)

    # Validate the Header & title of the OranngeHRM

    def test_header(self, booting_function, test_login, request):

        try:
            title1 = self.driver.title
            expected_title = org.access_data(3, 6)
            if expected_title in title1:
                org.write_data(3, 7, "Title Verified")
                print("Title Verification Passed: ",title1)
                assert title1 == expected_title
            else:
                org.write_data(3,7, "Ttitle Mismatched")
                print("Title Verification Failed: ", title1)
                assert title1 == expected_title
        except Exception as e:
            print("title error on : ",e)

    # Verify & Validate the Header Tabs in the Admin Panel
        
    def test_admin(self, booting_function,test_login, request):

        try:
            admin1 = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator2.Orange_locat2().admin_tab)))
            admin1.click()

    # Create a Variable & assign the locators of Admin & its Header web elements

            user_management1 = locator2.Orange_locat2().user_management
            job1 = locator2.Orange_locat2().jobs
            organization1 = locator2.Orange_locat2().organization
            qualification1 = locator2.Orange_locat2().qualification
            nationalites1 = locator2.Orange_locat2().nationalites
            corporate_branding1 = locator2.Orange_locat2().corporate_branding
            configuration1 = locator2.Orange_locat2().configuration

    # Make the Web elements and its verifications as Dictonary for iteration

            tab_elements = {
            user_management1: "User Management",
            job1: "Job",
            organization1: "Organization",
            qualification1: "Qualifications",
            nationalites1: "Nationalities",
            corporate_branding1: "Corporate Branding",
            configuration1: "Configuration"
            }

            visible_of_tab_elements = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, user_management1)))

    # Iterate the Admin Tab Elements to verify its presence in the webpage
      
            for xpath, expected_text in tab_elements.items():
                element = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, xpath)))
                assert element.is_displayed(), f"Element not visible: {xpath}"
                assert element.text == expected_text, f"Element text mismatch for: {xpath}"

            screenshot_directory = r"E:\Automation Testing\practice\Task\Capstone_02\screenshots2\\"
            screenshot_filename = "admin_elements.png"
            screenshot_path = f"{screenshot_directory}{screenshot_filename}"
            self.driver.save_screenshot(screenshot_path)
            org.write_data(3, 7, "Title & Admin Tab Elements are Verified")
            print("Admin Tab Elements are Visible")
        except Exception as e:
            print("Element error on: ",e)

    # Verify & Validate the Elemnts in Sidepane
    
    def test_sidepane(self, booting_function, test_login, request):
        
        try:
            admin1 = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, locator2.Orange_locat2().admin_tab)))
            admin1.click()

     # Create a Variable & assign the locators of Sidepane web elements

            pim1 = locator2.Orange_locat2().pim
            leave1 = locator2.Orange_locat2().leave
            time1 = locator2.Orange_locat2().time
            recruiments1 =locator2.Orange_locat2().recruiments
            my_info1 = locator2.Orange_locat2().my_info
            performance1 = locator2.Orange_locat2().perfomance
            dashboard1 = locator2.Orange_locat2().dashboard
            directory1 = locator2.Orange_locat2().directory
            maintenance1 = locator2.Orange_locat2().maintenance
            claim1 = locator2.Orange_locat2().claim
            buzz1 = locator2.Orange_locat2().buzz
    
     # Make the Web elements and its verifications as Dictonary for iteration

            sidepane_elements = {
                pim1: "PIM",
                leave1: "Leave",
                time1: "Time",
                recruiments1: "Recruitment",
                my_info1: "My Info",
                performance1: "Performance",
                dashboard1: "Dashboard",
                directory1: "Directory",
                maintenance1: "Maintenance",
                claim1: "Claim",
                buzz1: "Buzz"
                }

            visibility_of_menu = self.wait.until(
                EC.presence_of_all_elements_located((By.XPATH, pim1)))
    
     # Iterate the Sidepane Elements to verify its presence in the webpage
            
            for tab, expected_text in sidepane_elements.items():
                element = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, tab)))
                assert element.is_displayed(), f"Element not visible: {tab}"
                assert element.text == expected_text, f"Element text mismatch for: {tab}"
            screenshot_directory = r"E:\Automation Testing\practice\Task\Capstone_02\screenshots2\\"
            screenshot_filename = "side_pane_elements.png"
            screenshot_path = f"{screenshot_directory}{screenshot_filename}"
            self.driver.save_screenshot(screenshot_path)
            org.write_data(4, 7, "SidePane Tab Elements are Present")
            print("Side Pane  Elements are Visible")
        except Exception as e:
            print("Element error on: ",e)


excel_file = r"E:\Automation Testing\practice\Task\Capstone_02\capstonedata2.xlsx"
sheet_name = "Sheet1"
org = data2.Orange_dat2(excel_file, sheet_name)
max_row = org.row_count()






        

           