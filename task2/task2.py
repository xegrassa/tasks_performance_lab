import sys
from sympy.geometry import Point, Polygon


def main():
    with open(sys.argv[1], 'r', encoding='utf8') as file:
        rectangle = []
        for i in file:
            rectangle.append(Point(i.split()))
        rect = Polygon(*rectangle[:])
    with open(sys.argv[2], 'r', encoding='utf8') as file:
        points = []
        for i in file:
            points.append(Point(i.split()))

    for point in points:
        if point in rect.vertices:
            print(0)
        elif list(filter(None, map(point.intersection, rect.sides))):
            print(1)
        elif rect.encloses_point(point):
            print(2)
        else:
            print(3)


if __name__ == '__main__':
    main()
