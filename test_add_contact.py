# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select # used for selecting birthday and anniversary
import unittest
from contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_new_contact_page(wd)
        self.create_contact(wd, Contact(firstname="sdfsdf",
                                        middlename="sadsa",
                                        lastname="asdsad",
                                        nickname="as",
                                        title="sda",
                                        company="gfd",
                                        address="sad",
                                        homephone="sdf",
                                        mobile="123",
                                        workphone="23",
                                        fax="123",
                                        email1="asasd",
                                        email2="das",
                                        email3="das",
                                        homepage="asd",
                                        secaddress="asd",
                                        sechome="asda",
                                        notes="asda"))
        self.return_to_homepage(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_homepage(self, wd):
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, wd, contact):
        # fill contact form
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homephone)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.workphone)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email1)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # select birthday
        #wd.find_element_by_name("bday").click()
        #Select(wd.find_element_by_name("bday")).select_by_visible_text("13")
        #wd.find_element_by_xpath("//option[@value='13']").click()
        #wd.find_element_by_name("bmonth").click()
        #Select(wd.find_element_by_name("bmonth")).select_by_visible_text("September")
        #wd.find_element_by_xpath("//option[@value='September']").click()
        #wd.find_element_by_name("byear").click()
        #wd.find_element_by_name("byear").clear()
        #wd.find_element_by_name("byear").send_keys("2000")
        # select anniversary
        #wd.find_element_by_name("aday").click()
        #Select(wd.find_element_by_name("aday")).select_by_visible_text("16")
        #wd.find_element_by_css_selector("select[name=\"aday\"] > option[value=\"16\"]").click()
        #wd.find_element_by_name("amonth").click()
        #Select(wd.find_element_by_name("amonth")).select_by_visible_text("September")
        #wd.find_element_by_css_selector("select[name=\"amonth\"] > option[value=\"September\"]").click()
        #wd.find_element_by_name("ayear").click()
        #wd.find_element_by_name("ayear").clear()
        #wd.find_element_by_name("ayear").send_keys("2005")
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.secaddress)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.sechome)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit form
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def add_new_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
