# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

list = [i for i in range(1,10)]
for folder_number in list:
    Newdir = 'Newdir' + str(folder_number)
    dir_path = os.path.join(os.getcwd(), Newdir)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')
    #os.rmdir(dir_path) #УДАЛЕНИЕ ПАПОК

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
files = os.listdir()
for i in files:
    if os.path.isfile(os.path.join(os.getcwd(), i)) == False:
        print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import sys, shutil
shutil.copyfile(sys.argv[0], 'copy1.py')
