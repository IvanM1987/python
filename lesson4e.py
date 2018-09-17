# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random
list = [random.randint(0,10)**2 for x in range(10)]
print(list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruit_list_1 = ["яблоко", "апельсин", "мандарин"]
fruit_list_2 = ["яблоко", "апельсин", "лимон"]
result = []
for i in range(len(fruit_list_1)):
    if fruit_list_1[i] in fruit_list_2:
        result.append(fruit_list_1[i])
print(result)
# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
list_of_numbers = [random.randint(-100, 100) for _ in range(30)]
print(list_of_numbers)
final_list =[]
for i in range(len(list_of_numbers)):
    if list_of_numbers[i] % 3 ==0 and list_of_numbers[i] > 0 and list_of_numbers[i] % 4 !=0:
        final_list.append(list_of_numbers[i])
print(final_list)
