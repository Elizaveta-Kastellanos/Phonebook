import View_phonebook
import Model_Phonebook

def Button_click():
    user_data = View_phonebook.Get_view_model()
    Model_Phonebook.add_model_phonebook(user_data)

def Button_click_search():
    user_data_search = View_phonebook.Get_user_search()
    all_user_data = Model_Phonebook.search_phone_in_phonebook(user_data_search)
    return all_user_data