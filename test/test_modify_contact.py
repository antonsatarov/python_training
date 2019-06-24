from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contact_list = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="New first name"))
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)


def test_modify_contact_bday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(bday="1"))
    old_contact_list = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(bday="2"))
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)