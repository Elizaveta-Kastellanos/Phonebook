from datetime import datetime as dt
from time import time 


def log_data_user(fio, phone_number):
    file_log_user_data = 'phonebook.txt'
    time = dt.now().strftime("%d/%m/%Y Time %H:%M")
    with open(file_log_user_data, 'a') as file:
        file.write(f'{time} \nFIO: {fio} - NumberPhone: {phone_number}\n')

def give_the_data_user(user_data_search):
    file_log_user_data = 'phonebook.txt'
    with open(file_log_user_data, 'r') as file:
        all_data_user = file.read()
        if all_data_user.find(user_data_search) == -1:
            return f'No person found with these parametrs.'
        else:
            all_data_user = all_data_user.split(f'\n')
            answer = -1
            answer_new = []
            for i in range(0,len(all_data_user)):
                answer = all_data_user[i].find(user_data_search)
                if answer != -1:
                    answer_new.append(all_data_user[i])
            return answer_new

      
       
           