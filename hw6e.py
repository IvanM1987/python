# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
print('ТРЕУГОЛЬНИК')


class Triangle:

    def __init__(self, point_coord_1, point_coord_2, point_coord_3):
        self.point1 = point_coord_1
        self.point2 = point_coord_2
        self.point3 = point_coord_3

    def side_size_1(self):
        side_1 = ((int(self.point1.split(',')[0]) - int(self.point2.split(',')[0])) ** 2 +
                  (int(self.point1.split(',')[1]) - int(self.point2.split(',')[1])) ** 2) ** 0.5
        return round(side_1)

    def side_size_2(self):
        side_2 = ((int(self.point2.split(',')[0]) - int(self.point3.split(',')[0])) ** 2 +
                  (int(self.point2.split(',')[1]) - int(self.point3.split(',')[1])) ** 2) ** 0.5
        return round(side_2)

    def side_size_3(self):
        side_3 = ((int(self.point3.split(',')[0]) - int(self.point1.split(',')[0])) ** 2 +
                  (int(self.point3.split(',')[1]) - int(self.point1.split(',')[1])) ** 2) ** 0.5
        return round(side_3)

    def perimeter(self):
        per = triangle.side_size_1() + triangle.side_size_2() + triangle.side_size_3()
        return round(per)

    def area(self):  # Площадь
        hp = triangle.perimeter() / 2  # Half perimeter
        triangle_area = (hp * (hp - triangle.side_size_1()) * (hp - triangle.side_size_2())
                         * (hp - triangle.side_size_3())) ** 0.5
        return round(triangle_area)

    def height(self):  # Высота
        height1 = triangle.area() * 2 / triangle.side_size_1()
        height2 = triangle.area() * 2 / triangle.side_size_2()
        height3 = triangle.area() * 2 / triangle.side_size_3()

        return round(height1), round(height2), round(height3)


triangle = Triangle('20, 25', '-42, 25', '100, 100')

print(f'Периметр треугольника: {triangle.perimeter()}')
print(f'Площадь треугольника: {triangle.area()}')
print(f'Высота каждой стороны: {triangle.height()}')

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
print('ТРАПЕЦИЯ')


class Trapeze:

    def __init__(self, point_coord_1, point_coord_2, point_coord_3, point_coord_4):
        self.point1 = point_coord_1
        self.point2 = point_coord_2
        self.point3 = point_coord_3
        self.point4 = point_coord_4

    def side_size_1(self):  # Длинна катета
        side = ((int(self.point1.split(',')[0]) - int(self.point2.split(',')[0])) ** 2 +
                (int(self.point1.split(',')[1]) - int(self.point2.split(',')[1])) ** 2) ** 0.5
        return side

    def side_size_2(self):  # Длинна катета
        side = ((int(self.point3.split(',')[0]) - int(self.point4.split(',')[0])) ** 2 +
                (int(self.point3.split(',')[1]) - int(self.point4.split(',')[1])) ** 2) ** 0.5
        return side

    def short_base_lenght(self):  # Длинна катета
        sb = ((int(self.point2.split(',')[0]) - int(self.point3.split(',')[0])) ** 2 +
              (int(self.point2.split(',')[1]) - int(self.point3.split(',')[1])) ** 2) ** 0.5
        return sb

    def long_base_lenght(self):  # Длинна катета
        lb = ((int(self.point4.split(',')[0]) - int(self.point1.split(',')[0])) ** 2 +
              (int(self.point4.split(',')[1]) - int(self.point1.split(',')[1])) ** 2) ** 0.5
        return lb

    def perimeter_trapeze(self):
        per = trapeze.side_size_1() * 2 + trapeze.short_base_lenght() + trapeze.long_base_lenght()
        return per

    def area_trapeze(self):
        height = (trapeze.side_size_1() ** 2 - ((trapeze.long_base_lenght() -
                                                 trapeze.short_base_lenght()) / 2) ** 2) ** 0.5
        full_area = height * ((trapeze.long_base_lenght() + trapeze.short_base_lenght()) / 2)
        return full_area

    def check(self):
        if (trapeze.side_size_1() == trapeze.side_size_2() and
                trapeze.kolinear_base() == True and
                trapeze.long_base_lenght() != trapeze.short_base_lenght()):
            print('Трапеция равнобедренна')
        else:
            print('Трапеция не равнобедренна')

    def kolinear_base(self):  # Проверка параллельности оснований
        try:
            a = ((int(self.point3.split(',')[0]) - int(self.point2.split(',')[0])) /
                 (int(self.point4.split(',')[1]) - int(self.point1.split(',')[1])))
        except ZeroDivisionError:
            a = -10000
        try:
            b = ((int(self.point3.split(',')[1]) - int(self.point2.split(',')[1])) /
                 (int(self.point4.split(',')[1]) - int(self.point1.split(',')[1])))
        except ZeroDivisionError:
            b = -10000
        if a == b:
            return True


trapeze = Trapeze('0, 0', '10, 10', '30, 10', '40, 0')

print(f'Длинна боковой стороны: {trapeze.side_size_1()}')
print(f'Длинна боковой стороны: {trapeze.side_size_2()}')
print(f'Длтнна большего основания трапеции: {trapeze.long_base_lenght()}')
print(f'Длтнна меньшего основания трапеции: {trapeze.short_base_lenght()}')
print(f'Длинна периметра: {trapeze.perimeter_trapeze()}')
print(f'Площадь: {trapeze.area_trapeze()}')
print(f'Равнобедренность: {trapeze.check()}')