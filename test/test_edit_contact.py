from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="sdfsdf1",
                               middlename="sadsa1",
                               lastname="asdsad1",
                               nickname="as1",
                               title="sda1",
                               company="gfd1",
                               address="sad1",
                               homephone="45451",
                               mobile="1231",
                               workphone="231",
                               fax="1231",
                               email1="asasd1",
                               email2="das1",
                               email3="das1",
                               homepage="asd1",
                               bday="14",
                               bmonth="April",
                               byear="1981",
                               aday="11",
                               amonth="April",
                               ayear="2001",
                               secaddress="asd1",
                               sechome="asda1",
                               notes="asda1"))
    app.session.logout()