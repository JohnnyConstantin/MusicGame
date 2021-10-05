import random as rand
import sys
import unittest

all_accords = [a for a in 'ABCDEFG']
music = []


#                   Класс MENU предназначен для взаимодействия с клиентом и
#                        инициализации списка аккордов и длины мелодии
class Menu(unittest.TestCase):
    accord = None
    accords = None
    length = None

    def __init__(self):
        super().__init__()
        self.accords = []
        self.accord = []

    #               Метод для приветствия и выбора аккордов и длины мелодии

    def insert_accords(self, accord):
        for a in accord:
            self.assertIn(a, all_accords, "Введенный аккорд не существует") #Тест на наличие аккордов
            self.accords.append(a)

    def get_length(self):
        self.length = int(input())
        return self.length

    def show_menu(self):
        print("Добро пожаловать в прогу по генерации аккордов\n"
              "Доступные аккорды: ",
              all_accords,
              "\nВведите аккорды, с которыми хотите сгенерировать мелодию:\n")
        for a in input():
            self.accord.append(a)
        self.assertFalse(len(self.accord) == 0, self.accord)    #Тест на нулевой список
        print(self.accord)
        self.insert_accords(self.accord)
        print("Выберите длину мелодии: \n")
        self.get_length()
        print("Выбраннее аккорды:", self.accords, "\nДлина мелодии: ", self.length)


#                       Класс для взаимодействия с мелодией

class MusicActions():
    def print_music(self):
        print("Полученная мелодия: \n", ''.join(map(str, music)))


#                      В данном классе используются аккорды и длина
#                 заданные в экземпляре класса Menu. Расширяет класс MusicActions


class Generator(MusicActions):
    def __init__(self, length, accords):
        self.length = length
        self.accords = accords

    def generate_music(self):
        for a in range(self.length):
            music.append(rand.sample(self.accords, 1))
        return music

#Тесты

class Test(unittest.TestCase):
    def test_not_empty(self):
        menu = Menu()
        menu.accord = ['f', 'a', 'shit']
        self.assertFalse(len(menu.accord) == 0, menu.accord)
    def test_equal(self):
        menu = Menu()
        menu.accord   = ['F', 'A', 'G']
        for a in menu.accord:
            self.assertIn(a, all_accords, "Введенный аккорд не существует")
    def test_for_str(self):
        tests = ['A', 'F', 'G']
        test = Generator(5, tests)
        self.assertFalse(test.generate_music() is list)


def main():
    menu = Menu()
    menu.show_menu()
    generate = Generator(menu.length, menu.accords)
    generate.generate_music()
    generate.print_music()


#
if __name__ == '__main__':
    unittest.main()     #Чтобы запустить программу без тестов: убрать unittest.
