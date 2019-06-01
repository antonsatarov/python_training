# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_contact(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("first")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("middle")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("last")
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("nick")
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("title")
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("company")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("address")
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("htel")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("mtel")
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys("wtel")
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys("fax")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("mail1")
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys("mail2")
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys("mail3")
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys("www")
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text("13")
        driver.find_element_by_xpath("//option[@value='13']").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("September")
        driver.find_element_by_xpath("//option[@value='September']").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("2000")
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text("16")
        driver.find_element_by_css_selector("select[name=\"aday\"] > option[value=\"16\"]").click()
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("September")
        driver.find_element_by_css_selector("select[name=\"amonth\"] > option[value=\"September\"]").click()
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys("2005")
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("sec address")
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys("sec home")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("notes")
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        driver.find_element_by_link_text("home page").click()
        driver.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
