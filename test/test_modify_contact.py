from model.contact import Contact
from random import randrange


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="firstname", lastname="lastname", address="address", email1="email1",
                                   email2="email2", email3="email3", homephone="+555", mobile="(1)111", workphone="2-22",
                                   phone2="44444"))
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    contact = Contact(firstname="New first name")
    contact.id = old_contact_list[index].id
    contact.lastname = old_contact_list[index].lastname
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contact_list) == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list[index] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


#def test_modify_contact_bday(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(bday="1"))
#    old_contact_list = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(bday="2"))
#    new_contact_list = app.contact.get_contact_list()
#    assert len(old_contact_list) == len(new_contact_list)