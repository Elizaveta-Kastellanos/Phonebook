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
    if all_data_user.find(user_data_search) == -1:
        return 'No person found with these parametrs.'
    else:
        all_data_user = all_data_user.split(f'\n')
        answer = -1
        answer_new = []
        for i in range(0,len(all_data_user)):
            answer = all_data_user[i].find(user_data_search)
            if answer != -1:
                answer_new.append(all_data_user[i])
        return answer_new
    

def delete_user(user):
    all_data_user = logger.give_the_data_user(user)
    if all_data_user.find(user) == -1:
        return 'No person found with these parametrs.'
    else:
        all_data_user = all_data_user.split(f'\n')
        answer = -1
        answer_new = []
        for i in range(0,len(all_data_user)):
            answer = all_data_user[i].find(user)
            if answer != -1:
                answer_new.append(all_data_user[i])
        if len(answer_new) != 1:
            return 'To delete, enter more complete data or phone number!'
        else:
            logger.delete_user(user)
            return 'Removal was successful!'

        

    
