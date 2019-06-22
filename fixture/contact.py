from selenium.webdriver.support.ui import Select  # used for selecting birthday and anniversary


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.add_new_contact_page()
        self.fill_contact_form(contact)
        # submit form
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_homepage()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        # click edit
        wd.find_element_by_xpath("//tr[2]/td[8]/a/img").click()
        # fill contact form with new data
        self.fill_contact_form(new_contact_data)
        # click update
        wd.find_element_by_name("update").click()
        self.return_to_homepage()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill main fields
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        # select birthday
        self.change_select_value("bday", contact.bday)
        self.change_select_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        # select anniversary
        self.change_select_value("aday", contact.aday)
        self.change_select_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        # fill secondary fields
        self.change_field_value("address2", contact.secaddress)
        self.change_field_value("phone2", contact.sechome)
        self.change_field_value("notes", contact.notes)

    def change_select_value(self, select_value, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(select_value).click()
            Select(wd.find_element_by_name(select_value)).select_by_visible_text(text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.open_home_page()
        self.select_first_contact()
        # click delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # delete confirmation
        wd.switch_to.alert.accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def add_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))