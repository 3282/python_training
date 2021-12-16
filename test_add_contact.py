# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_1 import Application_1


@pytest.fixture
def app_1(request):
    fixture = Application_1()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app_1):
        app_1.open_home_page()
        app_1.login(username="admin", password="secret")
        app_1.open_contact_name()
        app_1.fill_new_contact_form(Contact(firstname="Maria", middlename="Olegovna", lastname="Bakholdina", nickname="Masha", company="YOTA", address="Yakhtennaya 6", home="6789688",
                                   mobile="89995567584", fax="896-888", email="test1@mail.ru", email2="test2@mail.ru", email3="test3@mail.ru", bday="17",
                                   bmonth="December", byear="1973", address2="Antonova-Ovseenko 13"))
        app_1.logout()

