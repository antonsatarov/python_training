# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(firstname="sdfsdf",
                               middlename="sadsa",
                               lastname="asdsad",
                               nickname="as",
                               title="sda",
                               company="gfd",
                               address="sad",
                               homephone="4545",
                               mobile="123",
                               workphone="23",
                               fax="123",
                               email1="asasd",
                               email2="das",
                               email3="das",
                               homepage="asd",
                               bday="13",
                               bmonth="September",
                               byear="1980",
                               aday="10",
                               amonth="May",
                               ayear="2000",
                               secaddress="asd",
                               phone2="asda",
                               notes="asda")
    app.contact.create(contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
