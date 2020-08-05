"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""
from abc import ABC, abstractmethod

class DrawShapesInterface(ABC):

    @abstractmethod
    def drawTriangle(self, pencilType: str, pencilBorder: int) -> str:
        pass

    @abstractmethod
    def drawRectangle(self, pencilType: str, pencilBorder: int) -> str:
        pass


class blackPencil(DrawShapesInterface):

    def drawTriangle(self, pencilType: str, pencilBorder: int) -> str:

        if pencilBorder:
            message = 'kalın'

        else:
            message = 'ince'

        print('{} siyah kalem ile {} bir üçgen çizildi.'.format(pencilType, message))

    def drawRectangle(self, pencilType: str, pencilBorder: int) -> str:

        if pencilBorder:
            message = 'kalın'

        else:
            message = 'ince'

        print('{} siyah kalem ile {} bir kare çizildi.'.format(pencilType, message))


class redkPencil(DrawShapesInterface):

    def drawTriangle(self, pencilType: str, pencilBorder: int) -> str:

        if pencilBorder:
            message = 'kalın'

        else:
            message = 'ince'

        print('{} kırmızı kalem ile {} bir üçgen çizildi.'.format(pencilType, message))

    def drawRectangle(self, pencilType: str, pencilBorder: int) -> str:

        if pencilBorder:
            message = 'kalın'

        else:
            message = 'ince'

        print('{} kırmızı kalem ile {} bir kare çizildi.'.format(pencilType, message))


if __name__ == '__main__':

    border1 = 0
    border2 = 1

    type1 = 'Keçeli'
    type2 = 'Kurşun'

    kalem1 = redkPencil()
    kalem2 = blackPencil()

    kalem1.drawTriangle(type1, border1)
    kalem2.drawRectangle(type2, border2)
