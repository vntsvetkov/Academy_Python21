from abc import ABC, abstractmethod
""" Принципы проектирования классов SOLID
1. Принцип единственной ответственности
У каждого класса должна быть только одна «ответственность» 
и он не должен брать на себя другие обязанности.

2. Принцип открытости/закрытости
Классы должны быть открыты для расширения, но закрыты для изменений

3. Принцип подстановки Барбары Лисков
Объекты в программе должны быть заменяемы экземплярами их подтипов 
без ущерба корректности работы программы

4. Принцип разделения интерфейса

5. Принцип инверсии зависимостей
"""


class Radio:
    def __init__(self, station: str):
        self.__station = station

    @property
    def station(self):
        return self.__station

    @station.setter
    def station(self, station):
        self.__station = station

    def play(self):
        return f"В эфире радио {self.__station}"


class MixinRadio:

    def play_radio(self, radio: Radio):
        print(radio.play())


class MobilePhone(MixinRadio):
    def __init__(self, brand: str, year: int, color: str):
        self.__brand = brand
        self.__year = year
        self.__color = color


class Power:
    LOWER = 100
    MEDIUM = 150
    TOP = 200
    MAX = 300


class Car(MixinRadio):
    def __init__(self, brand: str, year: int, color: str, power: int):
        self.__brand = brand
        self.__year = year
        self.__color = color
        self.__power = power
        self.capacity = {}

    def __str__(self):
        return f"Марка: {self.__brand} год: {self.__year} цвет: {self.__color}"

    @property
    def power(self):
        return self.__power

    def set_capacity(self, place, trunk):
        self.capacity = {"Количество мест": place, "Объем багажника": trunk}


class SUV(Car):
    pass


class Sedan(Car):
    pass


class NalogCalculation:
    @abstractmethod
    def get_nalog(self):
        pass

class NalogCalculationLower(NalogCalculation):
    def __init__(self, power: int):
        self.__power = power

    def get_nalog(self):
        return self.__power * 2.5

class NalogCalculationMedium(NalogCalculation):
    def __init__(self, power: int):
        self.__power = power

    def get_nalog(self):
        return self.__power * 3.5



class FileManagementCar:
    @staticmethod
    def save(car: Car, path: str):
        pass

    @staticmethod
    def load(path: str):
        pass


class DBManagementCar:
    @staticmethod
    def save(car: Car, name: str):
        pass

    @staticmethod
    def load(name: str) -> Car:
        pass


def print_capacity_car(obj):
    capacity = obj.capacity
    for key in capacity.keys():
        print(key, capacity[key])


def execute_application():
    car = Car("BMW", 2005, "black", 80)
    radio = Radio("Авто радио")
    car.play_radio(radio)

    if car.power < Power.LOWER:
        ncl = NalogCalculationLower(car.power)
        print(ncl.get_nalog())
    elif Power.LOWER <= car.power < Power.MEDIUM:
        ncm = NalogCalculationMedium(car.power)
        print(ncm.get_nalog())

    suv = SUV("Jeep", 2010, "red", 160)
    sedan = Sedan("KIA", 2020, "gray", 105)
    car.set_capacity(4, 500)
    suv.set_capacity(6, 1000)
    sedan.set_capacity(4, 300)

    print_capacity_car(sedan)

    #mobile_phone = MobilePhone("Iphone 14", 2023, "white")
    #radio.station = "Европа +"
    #mobile_phone.play_radio(radio)


if __name__ == "__main__":
    execute_application()