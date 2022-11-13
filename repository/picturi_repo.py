from domain.entities import Picturi
from exceptions.exceptions import CorruptedFileException


class PicturiRepoFile:
    def __init__(self, filename):
        self.__filename = filename

    def __load_from_file(self):
        """
        Functie ce se ocupa cu aducerea elementelor din fisier
        :return: lista cu picturi
        """
        try:
            f = open(self.__filename, 'r')
        except IOError:
            raise CorruptedFileException

        picturi_list = []
        lines = f.readlines()
        for line in lines:
            pic_id, pic_nume, pic_autor, pic_an = [token.strip() for token in line.split(';')]
            pictura = Picturi(pic_id, pic_nume, pic_autor, pic_an)
            picturi_list.append(pictura)
        f.close()
        return picturi_list

    def __save_to_file(self, pict_list):
        """
        Functie ce se ocupa cu salvarea obiectelor in fisier
        :param pict_list: lista cu obiectele de tip picturi
        :return: -
        """
        with open(self.__filename, 'w') as f:
            for pictura in pict_list:
                pict_str = str(pictura.get_id()) + ';' + str(pictura.get_nume()) + ';' + str(
                    pictura.get_autor()) + ';' + str(pictura.get_an()) + '\n'
                f.write(pict_str)

    def add_pictura(self,pictura):
        """
        Functie ce se ocupa cu adaugarea de noi picturi in fisier
        :param pictura: obiect de tip pictura
        :return:-
        """
        pict_list=self.__load_from_file()
        pict_list.append(pictura)
        self.__save_to_file(pict_list)

    def get_picturi(self):
        """
        :return: Lista cu elementele in fisier
        """
        return self.__load_from_file()

    def find_by_id(self,id):
        list=self.__load_from_file()
        for picturi in list:
            if int(picturi.get_id())==id:
                return picturi