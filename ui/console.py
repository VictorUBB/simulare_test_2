from termcolor import colored


class Console:
    def __init__(self,service,dto_service):
        self.__service=service
        self.__dto_service=dto_service

    def __show_picturi(self):
        pict_list=self.__service.get_picturi()
        for pictura in pict_list:
            print(pictura)

    def __add_pictura(self):
        try:
            id=int(input("Introduceti id:"))
            nume=input("Introduceti nume")
            autor=input("Introduceti auor")
            an=int(input("Introduceti an"))
        except ValueError:
            print(colored("Introduceti valori humerice pentru id si an",'red'))

        self.__service.add_pictura(id,nume,autor,an)

    def __sort_by_str(self):
        the_string=input("Introduceti sirul cautat:")
        pict_list=self.__service.sort_alph()
        list=self.__service.find_the_string(pict_list,the_string)
        for pictura in list:
            print(pictura)

    def __show_dto(self):
        self.__dto_service.create_dto()
        list=self.__dto_service.get_autori()
        for autor in list:
            print(autor)

    def __sort(self):
        list_of_autori=self.__dto_service.sort_by_age()
        self.__dto_service.sort_alph(list_of_autori)
        for index in range(len(list_of_autori)):
            if index>0:
                if list_of_autori[index]!=list_of_autori[index-1]:
                    print(self.__service.find_by_id(int(list_of_autori[index].get_id())))
            else : print(self.__service.find_by_id(int(list_of_autori[index].get_id())))

    def show_ui(self):
        while True:
            print(colored("Adaugati picturi",'blue'))
            print(colored("Afisati picturi", 'blue'))
            option=input("Introduceti optiunea dumneavoastra:")
            if option.lower()=='adauga':
                self.__add_pictura()
            elif option.lower()=='afisare':
                self.__show_picturi()
            elif option.lower()=='string':
                self.__sort_by_str()
            elif option.lower()=='dto':
                self.__show_dto()
            elif option.lower()=='sort':
                self.__sort()
