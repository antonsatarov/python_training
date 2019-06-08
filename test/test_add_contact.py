# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="sdfsdf",
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
                                    sechome="asda",
                                    notes="asda"))
    app.logout()



