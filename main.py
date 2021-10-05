import random as rand
import sys


all_accords = [a for a in 'ABCDEFG']
music = []


#                   Класс MENU предназначен для взаимодействия с клиентом и
#                        инициализации списка аккордов и длины мелодии
class Menu:
    accords = None
    length = None

    def __init__(self):
        self.accords = []

    #               Метод для приветствия и выбора аккордов и длины мелодии

    def show_menu(self):
        print("Добро пожаловать в прогу по генерации аккордов\n"
              "Доступные аккорды: ",
              all_accords,
              "\nВведите аккорды, с которыми хотите сгенерировать мелодию:\n")
        for a in input():
            if a in all_accords:
                self.accords.append(a)
            else:
                print("Таких аккордов не существует!")
                sys.exit()
        print("Выберите длину мелодии: \n")
        self.length = int(input())
        print("Выбраннее аккорды:", self.accords, "\nДлина мелодии: ", self.length)


#                      В данном классе используются аккорды и длина
#                           заданные в экземпляре класса Menu


class MusicActions():
    def print_music(self):
        print("Полученная мелодия: \n", ''.join(map(str, music)))


class Generator(MusicActions):
    def __init__(self, length, accords):
        self.length = length
        self.accords = accords

    def generate_music(self):
        for a in range(self.length):
            music.append(rand.sample(self.accords, 1))


def main():
    menu = Menu()
    menu.show_menu()
    generate = Generator(menu.length, menu.accords)
    generate.generate_music()
    generate.print_music()


if __name__ == '__main__':
    main()
