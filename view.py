from this import d
import controller

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
              '"/load_on_file" - добавить в справочник данные из файла\n'
              '"/exit" - закрыть справочник(сохранение в файл "txt_line")\n\n'
              'Ознакомился? Введи нужную команду....')
    else:
        reply = input('Введи команду.... ')
    while True:    
        if reply == '/add':
            key = input('Введи индекс контакта...  ')
            controller.add_data_telephone(key, telephone_dictionary)
            reply = input('Введи команду....  ')

        elif reply == '/edit':
            key = input('Введи индекс контакта для редактирования...  ')
            identific = input('Введи признак редактирования: дата, номер, ФИО или комментрарий....  ')
            controller.edit_data_tel(key, telephone_dictionary, identific)
            reply = input('Введи команду....  ')

        elif reply == '/print':
            key = input('Введи индекс контакта для печати в консоль или /all для печати всего справочника...  ')
            controller.print_string_directory(key, telephone_dictionary)
            reply = input('Введи команду....  ')
        elif reply == '/delete':
            key = input('Введи индекс контакта, который необходимо удалить...  ')
            controller.del_data_tel(key, telephone_dictionary)
            reply = input('Введи команду....  ')

        elif reply == '/cls':
            key = input('Ты уверен, что хочешь очистить весь справочник?..../удалить   ')
            if key == '/удалить':
                controller.del_all_data_tel(telephone_dictionary)
            reply = input('Введи команду....  ')

        elif reply == '/print_in_file':
            format_save = input('Укажи необходимый формат: /json ||  /txt_line ||  /txt_columns  ')
            controller.print_in_file(telephone_dictionary, format_save)
            reply = input('Введи команду.... ')

        elif reply == "/load_on_file":
            print('Поддерживаемые типы файлов: ..')
            identific_l = input('Введи тип файла...  ')
            file = input('Введи имя файла...  ')
            controller.load_on_file(telephone_dictionary, file, identific_l)
            reply = input('Введи команду из имеющегося перечня....  ')

        elif reply == '/exit':
            flag = input('Сохранить справочник?... "да" / "нет"   ')
            if flag == 'да':
                controller.print_in_file(telephone_dictionary, '/txt_line')
                break
            break
        else:
            reply = input('Введи команду из имеющегося перечня....  ')


        





if __name__ == "__main__":

    start()