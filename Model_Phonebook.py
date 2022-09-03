import logger

fio = None
number_phone = None

def add_model_phonebook(user_data):
    global fio
    global number_phone
    fio = user_data[0]
    number_phone = user_data[1]
    logger.log_data_user(fio, number_phone)

def search_phone_in_phonebook(user_data_search):
    all_data_user = logger.give_the_data_user(user_data_search)
    return all_data_user

    
    
