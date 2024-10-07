import math
import decimal

class Tools:
    def customround(number, decimals=None):
        rounded = float(round(number, decimals))
        part = rounded - int(number)
        if part != 0:
            return rounded
        else:
            return int(number)

class Vector:
    """
    A class that takes a list of 2 or 3 numbers of type string, int or float forming a vector.
    It can return the vector as string, calculate its length and its normal vector.
    """
    def __init__(self, coords: list):
        try:
            if len(coords) not in [2,3]:
                raise decimal.DivisionByZero
            self.coords = []
            for i in coords:
                self.coords.append(decimal.Decimal(str(i)))
        except decimal.DivisionByZero:
            print("wrong type or length")
            raise ValueError

        self.dimensions = len(self.coords)
        if self.length() == 0:
            self.zero = True
        else:
            self.zero = False

    def __str__(self):
        return "(" + ", ".join(str(i) for i in self.coords) + ")"

    def length(self, round=True):
        under = 0
        for coord in self.coords:
            under += coord**2
        if round:
            return Tools.customround(math.sqrt(under), 2)
        else:
            return decimal.Decimal(math.sqrt(under))

    def normal_vector(self):
        if self.zero:
            return self
        else:
            if self.dimensions == 3:
                if self.coords[2] != 0:
                    x = 1
                    y = 0
                    z = Tools.customround(-self.coords[0] / self.coords[2], 2)
                else:
                    if self.coords[1] != 0:
                        x = 1
                        y = Tools.customround(-self.coords[0] / self.coords[1], 2)
                        z = 0
                    else:
                        x = 0
                        y = 1
                        z = 0
                return Vector([x, y, z])
            else:
                return Vector([-self.coords[1], self.coords[0]])

class Line:
    """
    A class that takes two vectors of type Vector by me (see above for details) that
    represent the starting point and the direction of the line.
    It can return the line as string, calculate its intersection points and its normal vector.
    """
    def __init__(self, s: Vector, r: Vector):
        if s.dimensions != r.dimensions or r.zero:
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

    def normal_vector(self):
        return self.r.normal_vector()

class Vectors:
    """
    A class that takes two vectors of type Vector by me (see above for details).
    It can return them as string, calculate their dot product, their angle, check
    if they are orthogonal or kolinear and calculate their normal vector.
    """
    def __init__(self, a: Vector, b: Vector):
        if a.dimensions != b.dimensions or a.zero or b.zero:
            print("not same dimensions or zero vector")
            raise ValueError
        self.a, self.b = a, b

    def __str__(self):
        return str(self.a) + ", " + str(self.b)

    def dot_product(self, round=True):
        product = 0
        for i, j in zip(self.a.coords, self.b.coords):
            product += i * j
        if round:
            return Tools.customround(product, 2)
        else:
            return product

    def orthogonal(self):
        return self.dot_product() == 0

    def angle(self):
        return Tools.customround(math.degrees(math.acos(self.dot_product(False) /\
                 (self.a.length(False) * self.b.length(False)))), 2)

    def small_angle(self):
        return Tools.customround(math.degrees(math.acos(abs(self.dot_product(False) /\
                 (self.a.length(False) * self.b.length(False))))), 2)

    def kolinear(self):
        i, a, b = 0, self.a.coords, self.b.coords
        while i < len(a) - 1 and a[i] == b[i] == 0:
            i += 1
        try:
            first = a[i] / b[i]
            for one, two in zip(a[i+1:], b[i+1:]):
                if not (one == two == 0) and one / two != first:
                    return False
        except decimal.DivisionByZero:
            return False
        return True

    def normal_vector(self):
        a, b = self.a, self.b
        parallel = self.kolinear()
        if parallel:
                return a.normal_vector()
        elif a.dimensions == 3:
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
    It can also calculate their angle, their normal vector and if they are othogonal.
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
        return Vectors(self.a.r, self.b.r).kolinear()

    def identical(self):
        i, s1, s2, r2 = 0, self.a.s.coords, self.b.s.coords, self.b.r.coords
        while i < len(r2) - 1 and r2[i] == (s1[i] - s2[i]) == 0:
            i += 1
        try:
            first = (s1[i] - s2[i]) / r2[i]
            for one, two, three in zip(s1[i+1:], s2[i+1:], r2[i+1:]):
                if not ((one - two) == three == 0) and (one - two) / three != first:
                    return False
        except decimal.DivisionByZero:
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
        except decimal.DivisionByZero:
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

    def orthogonal(self):
        return Vectors(self.a.r, self.b.r).orthogonal()

    def angle(self):
        return Vectors(self.a.r, self.b.r).angle()

    def small_angle(self):
        return Vectors(self.a.r, self.b.r).small_angle()

    def normal_vector(self):
        return Vectors(self.a.r, self.b.r).normal_vector()