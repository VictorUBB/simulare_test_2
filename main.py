# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from repository.dto_repo import DTORepoFile
from repository.picturi_repo import PicturiRepoFile
from service.dto_service import DTOService
from service.picturi_service import PicturiService
from ui.console import Console

picturi_repo=PicturiRepoFile('data/picturi.txt')
picturi_service=PicturiService(picturi_repo)

dto_repo=DTORepoFile('data/dto.txt')
dto_service=DTOService(dto_repo,picturi_repo)
console=Console(picturi_service,dto_service)
console.show_ui()