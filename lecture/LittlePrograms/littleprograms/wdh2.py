import abc
import random


class Article(abc.ABC):
    def __init__(self, name: str, color: str, price: float):
        self.name = name
        self.color = color
        self.price = price

    def __repr__(self):
        return f"Article({self.name}, {self.price})"

    @abc.abstractmethod
    def calculate_price(self) -> float:
        pass
    @abc.abstractmethod
    def calculate_shipping(self, country:str) -> float:
        pass

class TShirt(Article):

    @property
    def serial_number(self):
        return self.__serial_number

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        #if value == "XS" or value == "S" or value == "M"
        if value in ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]:
            self.__size = value
        else:
            self.__size = "M" # default wert wenn blödsinn angegeben wird

    def __init__(self, name: str, color: str, price:float, size: str):
        super().__init__(name, color, price)

        # bei get property müssen wir IMMER über __ direkt auf dem privaten attribut ändern
        # self.serial_number geht ja nicht da nur ein get property
        self.__serial_number = random.randint(10000000, 300000000)
        # set get property
        self.size = size # über property zugreifen damit die logik des setters vor fehleingaben schützt
        # self.__size = size

    def calculate_price(self) -> float:
        if self.size == "XL" or self.size == "XXL":
            return self.price * 1.1
        else:
            return self.price

    def calculate_shipping(self, country: str) -> float:
        return 5




if __name__ == '__main__':
    # x = Article("Tshirt", "red", 10) # nicht erlaubt
    t = TShirt("Model XYZ", "red", 20, "ABCD")

    print(t.calculate_price())
    t.size = "hansi"
    print(t.size)
    #t.__serial_number = "hansi" # ändert nicht am privaten attribut -> name mangeling
    print(t.serial_number)

# Abstrakte Klassen

# properties

