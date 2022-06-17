from datetime import date
import json
import re
import string
from this import d


def add_data_telephone(key, telephone_dictionary):
    data = input(
        'Введите ФИО, номер телефона и примечание(при необходимости) через "/"...   ')
    data += f'/{date.today()}'
    telephone_dictionary[key] = data


def print_string_directory(flag_key, telephone_directory: dict):
    if flag_key == '/all':
        for key in telephone_directory:
            print(data_list_parse(key, telephone_directory))
    else:
        print(data_list_parse(flag_key, telephone_directory))


def data_list_parse(key, telephone_directory: dict, flag='line'):

    data_list = telephone_directory[key].split('/')

    data_string = ''

    if flag == 'line':
        if len(data_list) == 4:
            data_string += f'{key} {data_list[0]} - номер телефона: {number_telef(data_list[1])} ; '\
                f'примечание: {data_list[2]} , дата создания контакта: {data_list[-1]}'
        else:
            data_string += f'{key} {data_list[0]} - номер телефона: {number_telef(data_list[1])}; '\
                f'дата создания контакта: {data_list[-1]}'

    if flag == 'columns':
        if len(data_list) == 4:
            data_string += f'{key}\n \t{data_list[0]}\n \tномер телефона: {number_telef(data_list[1])}\n'\
                f'\tдата создания контакта: {data_list[-1]}\n \tпримечание: {data_list[2]}'
        else:
            data_string += f'{key}\n \t{data_list[0]}\n \tномер телефона: {number_telef(data_list[1])}\n'\
                f'\tдата создания контакта: {data_list[-1]}'

    return data_string


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
    string_data = input('Введите новые данные...   ')
    if identific == 'номер':
        data_list[1] = string_data
    elif identific == 'ФИО':
        data_list[0] = string_data

    if len(data_list) == 4:
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


def print_in_file(data_dictionary: dict, format: str):
    if format == '/json':
        with open('data_dictionary.json', 'a') as file:
            json.dump(data_dictionary, file, indent=4, ensure_ascii=False)

    elif format == '/txt_line':
        with open('data_dictionary_line.txt', 'a') as file:
            for key in data_dictionary:
                data_string = data_list_parse(key, data_dictionary)
                file.write(data_string + '\n')

    elif format == '/txt_columns':
        with open('data_dictionary_columns.txt', 'a') as file:
            for key in data_dictionary:
                data_string = data_list_parse(key, data_dictionary, 'columns')
                file.write(data_string + '\n')

def load_on_file(data_dictionary, file: str, identific: str): #ToDo
    if identific == 'txt_line':
        data = open(file, 'r')
        key = 1
        for line in data:
           key_l = 'l' + str(1)
           key +=1
           data_dictionary[key_l] = data_file_parse_txt(line)


def data_file_parse_txt(line:str):
    list_del = ['-', 'номер', 'телефона:','примечание', 'дата', 'создания', 'контакта:', ',', ';']
    str_buf = []
    new_str = ''
    str_buf = line.split()
    del str_buf[0]
    new_list_data = [word for word in str_buf if word not in list_del]
    new_str = '/'.join(new_list_data)
    return new_str


