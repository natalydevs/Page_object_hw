from selene import have
from Page_object_hw.pages.registration_page import RegistrationForm

def test_form_filling():
    registration_form = RegistrationForm()
    registration_form.open()
    registration_form.fill_firstname('Liza')
    registration_form.fill_lastname('Koss')
    registration_form.fill_useremail('lizakoss@mailinator.com')
    registration_form.select_gender('Female')
    registration_form.fill_user_phone_number('4564978762')
    registration_form.fill_date_of_birth('2000','March','15')
    registration_form.select_subject('Chemistry')
    registration_form.select_hobby('Reading')
    registration_form.upload_file('cat.png')
    registration_form.fill_current_address('Sevastopol,Test str., 1')
    registration_form.select_state('Haryana')
    registration_form.select_city('Karnal')
    registration_form.click_submit_button()
    registration_form.get_modal_popup().should(have.exact_text('Thanks for submitting the form'))
    registration_form.should_registered_user_with.should(have.exact_texts(
        'Liza Koss',
        'lizakoss@mailinator.com',
        'Female',
        '4564978762',
        '15 March,2000',  # без пробела — как в факте
        'Chemistry',
        'Reading',  # сначала Hobbies
        'cat.png',  # потом Picture
        'Sevastopol,Test str., 1',  # Address
        'Haryana Karnal'  # State and City
    ))
