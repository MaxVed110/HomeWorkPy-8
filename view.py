import controlller

def start():
    telephone_dictionary = {}
    print('Привет, перед тобой телефонный справочник.\nХочешь увидеть функционал или сразу приступим к работе?\nОтветь "хочу" или нажми любую клавишу')
    global reply
    reply = input()
    if reply == "хочу":
        reply = input('\nВот доступный функционал:\n'
              '"/add" - добавить контакт в справочник\n'
              '"/edit" - редактировать ранее добавленный контакт\n'
              '"/delete" - удалить указанный контакт\n'
              '"/cls" - очистить весь справочник\n'
              '"/print" - напечатать справочник в консоль\n'                        
              '"/print_in_file" - выгрузить справочник в файл в указанном формате\n'
              '"/load_on_file" - добавить в справочник данные из файла\n\n'
              'Ознакомился? Введи нужную команду....')
    else:
        reply = input('Введи команду....')
    while True:    
        if reply == '/add':
            controlller.add_data_telephone(telephone_dictionary)

        





if __name__ == "__main__":

    start()