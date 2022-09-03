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
        return all_data_user

def delete_user(user):
    file_log_user_data = 'phonebook.txt'
    with open(file_log_user_data, 'r') as file:
        all_data_user = file.read().split(f'\n')
        wh = len(all_data_user)
        for i in range(0, wh):
            ind = all_data_user[i].find(user)
            if ind != -1:
                tmp = i
                break
        all_data_user.pop(tmp)
        all_data_user.pop(tmp-1)
        for i in range(0,len(all_data_user)):
            if len(all_data_user[i]) == 0:
                all_data_user.pop(i)
                break
        with open(file_log_user_data, 'w') as file_new:
            for i in range(0,len(all_data_user)):
                file_new.write(f'{all_data_user[i]}\n')

        