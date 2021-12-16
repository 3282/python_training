# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
        app.open_home_page()
        app.login(username="admin", password="secret")
        app.open_contact_name()
        app.fill_new_contact_form(Contact(firstname="Maria", middlename="Olegovna", lastname="Bakholdina", nickname="Masha", company="YOTA", address="Yakhtennaya 6", home="6789688",
                                   mobile="89995567584", fax="896-888", email="test1@mail.ru", email2="test2@mail.ru", email3="test3@mail.ru", bday="17",
                                   bmonth="December", byear="1973", address2="Antonova-Ovseenko 13"))
        app.logout()

