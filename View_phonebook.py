
def Get_view_model():
    fio = input('Enter FIO: ')
    while True:
        number_phone = input('Enter number phone: ')
        if number_phone.isdigit() == True:
            break
    return (fio, number_phone)

def Get_user_search():
    data_user = input('Enter FIO or numberphone: ')
    return data_user

def Get_user_delete():
    delete_user = input('Enter who you want to delete: ')
    print('Are you sure you want to delete?')
    return delete_user