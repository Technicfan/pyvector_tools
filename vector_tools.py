import math
import decimal

class Tools:
    def customround(number, decimals):
        rounded = float(round(number, decimals))
        part = rounded - int(number)
        if part != 0:
            return rounded
        else:
            return int(number)

class Vector:
    """
    A class that takes a list of 2 or 3 numbers of type string, int or float forming a vector.
    It can return the vector as string and calculate its length.
    """
    def __init__(self, coords: list):
        try:
            if len(coords) not in [2,3]:
                raise decimal.InvalidOperation
            self.coords = []
            for i in coords:
                self.coords.append(decimal.Decimal(str(i)))
        except decimal.InvalidOperation:
            print("wrong type or length")
            raise ValueError

        self.dimensions = len(self.coords)

    def __str__(self):
        return "(" + ", ".join(str(i) for i in self.coords) + ")"

    def length(self):
        under = 0
        for coord in self.coords:
            under += coord**2
        return Tools.customround(math.sqrt(under), 2)

class Line:
    """
    A class that takes two vectors of type Vector by me (see above for details) that
    represent the starting point and the direction of the line.
    It can return the line as string and calculate its intersection points.
    """
    def __init__(self, s: Vector, r: Vector):
        if s.dimensions != r.dimensions or r.length() == 0:
            print("not same dimensions or zero vector as r")
            raise ValueError
        else:
            self.s, self.r = s, r

    def __str__(self):
        return str(self.s) + " + r * " + str(self.r)

    def __intersection_point(self, index):
        if self.r.coords[index] != 0:
            point = []
            location = -self.s.coords[index] / self.r.coords[index]
            for i, j in zip(self.s.coords, self.r.coords):
                point.append(Tools.customround(i + location * j, 2))
            return point
        else:
            return None

    def intersections(self):
        if self.s.dimensions == 2:
            return False
        else:
            points = []
            for i in range(2, -1, -1):
                points.append(self.__intersection_point(i))
            return points

class Vectors:
    """
    A class that takes two vectors of type Vector by me (see above for details).
    It can return them as string, calculate their skalar product, their angle, check
    if they are orthogonal and calculate their normal vector.
    """
    def __init__(self, a: Vector, b: Vector):
        if a.dimensions != b.dimensions:
            print("not same dimensions")
            raise ValueError
        self.a, self.b = a, b

    def __str__(self):
        return str(self.a) + ", " + str(self.b)

    def skalar_product(self):
        product = 0
        for i, j in zip(self.a.coords, self.b.coords):
            product += i * j
        return Tools.customround(product, 2)

    def orthogonal(self):
        return self.skalar_product() == 0

    def angle(self):
        return Tools.customround(math.degrees(math.acos(self.skalar_product() /\
                 (self.a.length() * self.b.length()))), 2)

    def small_angle(self):
        return Tools.customround(math.degrees(math.acos(abs(self.skalar_product()) /\
                 (self.a.length() * self.b.length()))), 2)

    def normal_vector(self):
        a, b = self.a, self.b
        if a.dimensions == 3:
            x = Tools.customround(a.coords[1] * b.coords[2] - a.coords[2] * b.coords[1], 2)
            y = Tools.customround(a.coords[2] * b.coords[0] - a.coords[0] * b.coords[2], 2)
            z = Tools.customround(a.coords[0] * b.coords[1] - a.coords[1] * b.coords[0], 2)
            return Vector([x, y, z])
        else:
            return None

class Lines:
    """
    A class that takes two lines of type Line by me (see above for details).
    It can calculate the relation of the two lines (parallel/identical, crossing or nothing).
    The relation function returns an array where index 0 represents the relation:
    0: identical
    1: parallel
    2: crossing with point at index 1
    3: no relation
    """
    def __init__(self, a: Line, b: Line):
        if a.s.dimensions != b.s.dimensions:
            print("not same dimensions")
            raise ValueError
        self.a, self.b = a, b

    def __str__(self):
        return str(self.a) + ", " + str(self.b).replace("r", "s")

    def parallel(self):
        i, r1, r2 = 0, self.a.r.coords, self.b.r.coords
        while i < len(r1) - 1 and r1[i] == r2[i] == 0:
            i += 1
        try:
            first = r1[i] / r2[i]
            for one, two in zip(r1[i+1:], r2[i+1:]):
                if not (one == two == 0) and one / two != first:
                    return False
        except ZeroDivisionError:
            return False
        return True

    def identical(self):
        i, s1, s2, r2 = 0, self.a.s.coords, self.b.s.coords, self.b.r.coords
        while i < len(r2) - 1 and r2[i] == (s1[i] - s2[i]) == 0:
            i += 1
        try:
            first = (s1[i] - s2[i]) / r2[i]
            for one, two, three in zip(s1[i+1:], s2[i+1:], r2[i+1:]):
                if not ((one - two) == three == 0) and (one - two) / three != first:
                    return False
        except ZeroDivisionError:
            return False
        return True

    def crossing(self):
        first_part, second_part = [], []
        s1, s2, r1, r2 = self.a.s.coords, self.b.s.coords, self.a.r.coords, self.b.r.coords
        for x, y, a1, a2 in zip(r1, r2, s1, s2):
            first_part.append([x, -y])
            second_part.append(a2 - a1)

        try:
            x = ( first_part[1][1] * second_part[0] - first_part[0][1] * second_part[1] ) /\
                ( first_part[0][0] * first_part[1][1] - first_part[0][1] * first_part[1][0] )
            y = ( second_part[0] - first_part[0][0] * x ) / first_part[0][1]
        except ZeroDivisionError:
            return False
        if len(first_part) == 3 and first_part[2][0] * x + first_part[2][1] * y != second_part[2]:
            return False

        point = []
        for one, two in zip(s1, r1):
            point.append(Tools.customround(one + x * two, 2))
        return point

    def relation(self):
        if self.parallel():
            if self.identical():
                return [0]
            else:
                return [1]
        else:
            result = self.crossing()
            if result:
                return [2, result]
            else:
                return [3]