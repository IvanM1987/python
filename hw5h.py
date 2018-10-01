# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import shutil
import sys

print('sys.argv = ', sys.argv)


def current_directory():
    print(os.getcwd())


def move_to():
    if not new_path:
        print("Необходимо указать имя директории или полный путь")
        return
    else:
        try:
            if new_path.startswith("C:"):
                os.chdir(new_path)
                print(os.getcwd())
            else:
                target_dir = os.path.join(os.getcwd(), new_path)
                os.chdir(target_dir)
                print(os.getcwd())
        except FileNotFoundError:
            print("Данной директории не существует!")


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("copy <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def remove_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_to_remove = os.path.join(os.getcwd(), file_name)
    try:
        answer = input(f"Вы уверены, что хотите удалить {file_name}: (Y/N)")
        if answer == "Y" or "y":
            os.remove(file_to_remove)
            print(f"Файл {file_name} удален")
        else:
            print("До свидания!")
    except FileNotFoundError:
        print(f"Файла {file_name} не существует.")


def copy_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_to_copy = os.path.join(os.getcwd(), file_name)
    new_file = file_to_copy + "_copy"
    try:
        shutil.copyfile(file_to_copy, new_file)
        print(f"Файл {file_name} скопирован")
    except FileNotFoundError:
        print(f"Файла {file_name} не существует.")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


a = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "copy": copy_file,
    "rm": remove_file,
    "ls": current_directory,
    "cd": move_to
}

try:
    new_path = sys.argv[2]
except IndexError:
    new_path = None

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if a.get(key):
        a[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
