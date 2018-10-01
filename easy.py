# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
from pathlib import Path as pathto

def folder_creation(newdir):
    dir_path = os.path.join(os.getcwd(), newdir)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')

def folders_list():
    files = os.listdir()
    folders = []
    folder_index = []
    for name in (files):
        if os.path.isfile(os.path.join(os.getcwd(), name)) == False:
            folders.append(name)
    print("\n")
    for index, name in enumerate(folders, start=1):
        print(index, name)
    return folders

def folder_delete():
    item = folders_list()
    delete_item = int(input('Выберите папку, которую вы желаете удалить:'))
    dir_path = os.path.join(os.getcwd(), item[delete_item - 1])
    os.rmdir(dir_path)
    print(f"Папка {item[delete_item - 1]} удалена")

def move_to():
    print("Сейчвс вы находитесь: ", os.getcwd(), '\n')
    choice = int(input('Выберите пункт:\n'
              '1.Войти в одну из папок директории\n'
              '2.Войти в родительскую папку\n'
              '3.Подняться вверх по древу директорий\n'))
    if choice == 1:
        item = folders_list()
        folder_to_move = int(input('Выберите папку, в которую вы желаете перейти:'))
        dir_path = os.path.join(os.getcwd(), item[folder_to_move - 1])
        os.chdir(dir_path)
        print("Сейчвс вы находитесь: ", os.getcwd(), '\n')
    elif choice == 2:
        os.chdir(pathto(__file__).parent)
        print("Сейчвс вы находитесь: ", os.getcwd(), '\n')
    elif choice == 3:
        local_adress = os.getcwd()
        os.chdir(pathto(local_adress).parent)
        print("Сейчвс вы находитесь: ", os.getcwd(), '\n')
    else:
        print("Неверный выбор!")
