from domain.entities import DTO


class DTOService:
    def __init__(self,repo,picturi_repo):
        self.__repo=repo
        self.__picturi_repo=picturi_repo

    def create_dto(self):
        pict_list=self.__picturi_repo.get_picturi()
        for pictura in pict_list:
            dto_elm=DTO(pictura.get_id(),pictura.get_autor(),pictura.get_an())
            self.__repo.add_dto(dto_elm)

    def get_autori(self):
        return self.__repo.get_autori()

    def sort_by_age(self):
        list = self.__repo.get_autori()
        list.sort(key=DTO.get_an)
        return list

    def sort_alph(self,list_of_autori):
        list_of_autori.sort(key=DTO.get_autor)

