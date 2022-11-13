from domain.entities import Picturi
from repository.picturi_repo import PicturiRepoFile


class PicturiService:
    def __init__(self,repo):
        self.__repo=repo

    def add_pictura(self,id,nume,autor,an):
        pictura=Picturi(id,nume,autor,an)
        self.__repo.add_pictura(pictura)

    def get_picturi(self):
        return self.__repo.get_picturi()

    def sort_alph(self):
        pict_list=self.__repo.get_picturi()
        pict_list.sort(key=Picturi.get_an,reverse=True)
        return pict_list

    def find_the_string(self,pict_list,the_str):
        new_list=[]
        for pictura in pict_list:
            if the_str in pictura.get_nume():
                new_list.append(pictura)
        return new_list

    def find_by_id(self,id):
        return self.__repo.find_by_id(id)

