from datetime import date

from Page_object_hw.pages.registration_page import RegistrationForm
from Page_object_hw.models.user import User, Gender, Hobby
from Page_object_hw.data import users


def test_registration_with_preset_user():
    RegistrationForm() \
        .open() \
        .register(users.student) \
        .should_have_registered(users.student)



