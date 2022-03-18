from logic.person import Person

class Document(object):


    def __init__(self, id_document: int,
                 title_document: str = 'Titulo del docuemento',
                 number_page: int, category: str = 'Categoria',
                 Autor: [] = 'Autores'):

        self._id_document = id_document
        self._title_document = title_document
        self._number_page = number_page
        self._category = category
        self._Autor = Autor

    @property
    def id_document(self) -> int:
        return self._id_document

    @id_document.setter
    def id_document(self, id_document: int):
        self._id_document = id_document.setter

    @property
    def title_document(self) -> int:
        return self._title_document

    @title_document.setter
    def title_document(self, title_document: int):
        self._title_document = title_document.setter

    @property
    def number_page(self) -> int:
        return self._number_page

    @number_page.setter
    def number_page(self, number_page: int):
        self._number_page = number_page.setter

    @property
    def category(self) -> int:
        return self._category

    @category.setter
    def category(self, category: int):
        self._category = category.setter


def __str__(self):
    return '({0}, {1}, {2})'.format(self.id_document, self.title_document, self.number_page, self.category)

if __name__ == '__main__':

    info = Document(id_document=73577376, title_document="Mujeres en colombia", number_page=10
                    , category="Articulo",Autor=[])
    info.name = "Docuemento"
    print(info)