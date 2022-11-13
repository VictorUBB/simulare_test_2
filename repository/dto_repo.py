from domain.entities import DTO
from exceptions.exceptions import CorruptedFileException


class DTORepoFile:
    def __init__(self,filename):
        self.__filename=filename

    def __load_from_file(self):
        try:
            f=open(self.__filename,'r')
        except IOError:
            raise CorruptedFileException

        autori=[]
        lines=f.readlines()
        for line in lines:
            pict_id,pict_autor,pict_an=[token.strip() for token in line.split(';')]
            dto=DTO(pict_id,pict_autor,pict_an)
            autori.append(dto)

        f.close()
        return autori

    def __save_to_file(self,dto_list):
        with open(self.__filename,'w') as f:
            for elm in dto_list:
                dto_string=str(elm.get_id())+';'+str(elm.get_autor())+';'+str(elm.get_an())+'\n'
                f.write(dto_string)

    def get_autori(self):
        return self.__load_from_file()

    def add_dto(self,dto):
        list=self.__load_from_file()
        list.append(dto)
        self.__save_to_file(list)