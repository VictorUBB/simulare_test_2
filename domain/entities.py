class Picturi:
    """
    Cream entitatea pentru obiectele de tip pictura
    """
    def __init__(self, id, nume, autor, an):
        self.__id = id
        self.__nume = nume
        self.__autor = autor
        self.__an = an

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_autor(self):
        return self.__autor

    def get_an(self):
        return self.__an

    def __str__(self):
        return "ID Pictura: "+str(self.__id)+" Nume: "+str(self.__nume)+" Autor: "+str(self.__autor)+" An: "+str(self.__an)

class DTO:
    def __init__(self,id,autor,an):
        self.__id=id
        self.__autor=autor
        self.__an=an

    def get_id(self):
        return self.__id
    def get_autor(self):
        return self.__autor

    def get_an(self):
        return self.__an

    def __str__(self):
        return "Id:"+str(self.__id)+" Autor:"+str(self.__autor)+" An:"+str(self.__an)
