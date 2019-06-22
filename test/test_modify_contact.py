from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(firstname="New first name"))


def test_modify_contact_bday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(bday="1"))
    app.contact.modify_first_contact(Contact(bday="2"))