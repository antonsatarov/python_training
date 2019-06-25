from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(firstname="New first name")
    contact.id = old_contact_list[0].id
    contact.lastname = old_contact_list[0].lastname
    app.contact.modify_first_contact(contact)
    assert len(old_contact_list) == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list[0] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


#def test_modify_contact_bday(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(bday="1"))
#    old_contact_list = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(bday="2"))
#    new_contact_list = app.contact.get_contact_list()
#    assert len(old_contact_list) == len(new_contact_list)