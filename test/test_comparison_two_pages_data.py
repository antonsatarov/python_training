from model.contact import Contact
from random import randrange
import re


def test_comparison_contact_fields(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="firstname", lastname="lastname", address="address", email1="email1",
                                   email2="email2", email3="email3", homephone="+555", mobile="(1)111", workphone="2-22",
                                   phone2="44444"))
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_one_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_one_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_one_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobile, contact.workphone, contact.phone2]))))


def merge_emails_like_one_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))