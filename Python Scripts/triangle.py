import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot((x-self.getx()), (y-self.gety()))

    def distance_from_point(self, point):
        return math.hypot((point.getx()-self.getx()), (point.gety()-self.gety()))


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertice1 = vertice1
        self.__vertice2 = vertice2
        self.__vertice3 = vertice3

    def perimeter(self):
        self.__side1 = self.__vertice1.distance_from_point(self.__vertice2)
        self.__side2 = self.__vertice1.distance_from_point(self.__vertice3)
        self.__side3 = self.__vertice2.distance_from_point(self.__vertice3)
        return (self.__side1 + self.__side2 + self.__side3)

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
