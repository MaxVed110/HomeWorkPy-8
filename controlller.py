from datetime import date
import re
import string
from this import d
telephone_dictionary = {}


def add_data_telephone(key):
    data = input('Введите ФИО, номер телефона и примечание через "/"...')
    data += f'/{date.today()}'
    telephone_dictionary[key] = data


def print_string_directory(key, telephone_directory: dict):

    data_list = telephone_directory[key].split('/')

    if len(data_list) == 4:
        print(f'{telephone_directory[key]}// {data_list[0]} - номер телефона: {number_telef(data_list[1])}; '
              f'дата создания контакта: {data_list[-1]}, примечание: {data_list[2]}')
    else:
        print(f'{telephone_directory[key]}// {data_list[0]} - номер телефона: {number_telef(data_list[1])}; '
              f'дата создания контакта: {data_list[-1]}')


def number_telef(telephone_number):
    string_tel = re.sub(r'\+?[78](\d{3})(\d{3})(\d\d)(\d\d)',
                        r'+7(\1)\2-\3-\4', telephone_number)
    return string_tel


def del_data_tel(key, dictionary: dict):
    del dictionary[key]


def del_all_data_tel(dictionary: dict):
    dictionary.clear()


def edit_data_tel(key, dictionary: dict, identific: str):
    data_list = dictionary[key].split('/')
    string_data = input()
    if identific == 'номер':
        data_list[1] = string_data
    elif identific == 'ФИО':
        data_list[0] = string_data
    
    if len(data_list)==4:
        if identific == 'дата':
            data_list[3] = string_data
        elif identific == 'комментарий':
            data_list[2] = string_data
    else:
        if identific == 'дата':
            data_list[3] = string_data
        elif identific == 'комментарий':
            data_list.insert(2, string_data)
    str = '/'.join(data_list)
    dictionary[key] = str




if __name__ == "__main__":

    print('ddd')
    k = input()
    add_data_telephone(k)
    print(telephone_dictionary)
    edit_data_tel('1', telephone_dictionary, 'комментарий')
    print(telephone_dictionary)


#############
# import


###############
# export
