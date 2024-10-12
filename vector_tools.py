import math
import decimal
from copy import deepcopy as copy

class Tools:
    def customround(number, decimals=None):
        rounded = float(round(number, decimals))
        part = rounded - int(number)
        if part != 0:
            return rounded
        else:
            return int(number)

    def solve(A, b, floating=False) -> list:
        """
        a function that solves a linear equation system 
        of the for Ax = b using gaussian elimination
        - it takes two matrices which represent the equations
        - the number of the equations must be the same as the number of coefficients
        - it returns a list of decimal.Decimal or float if third parameter is True
        example:
            a = [[9,3,4],[4,3,4],[1,1,1]]
            b = [[7],[8],[3]]
            -> returns [-0.2, 4, -0.8]
        """
        invalid = False
        for i in range(len(A)):
            if len(A[i]) != len(b) or len(b[i]) != 1:
                invalid = True
                break
        if len(A) != len(b) or invalid:
            raise ValueError("invalid matrix sizes")

        matrix = copy(A)
        length = len(matrix)
        for i in range(length):
            matrix[i].append(b[i][0])
            for j in range(length + 1):
                matrix[i][j] = decimal.Decimal(matrix[i][j])

        for i in range(1, length):
            if matrix[0][0] == 0:
                matrix[0], matrix[i] = matrix[i], matrix[0]
            else:
                break

        for i in range(length):
            for line in range(1, length - i):
                top = matrix[i][i]
                bottom = matrix[-line][i]
                for row in range(length + 1):
                    matrix[-line][row] *= top
                    matrix[-line][row] -= bottom * matrix[i][row]

        matrix.reverse()
        for i in range(length):
            matrix[i].reverse()
        try:
            results = [matrix[0][0] / matrix[0][1]]
            for i in range(1, length):
                test = matrix[i][0]
                for j in range(1, i + 1):
                    test -= matrix[i][j] * results[j-1]
                results.append(test / matrix[i][i+1])
        except decimal.DivisionByZero:
            return []
        results.reverse()

        if floating:
            return list(map(float, results))
        else:
            return results

    def validate(a, b, r) -> bool:
        for eq, res in zip(a, b):
            result = 0
            for i in range(len(eq)):
                result += eq[i] * r[i]
            if result != res[0]:
                return False
        return True

class Vector:
    """
    A class that takes a list of 2 or 3 numbers of type string, int or float forming a vector.
    It can return the vector as string, calculate its length and its normal vector.
    """
    def __init__(self, coords: list):
        try:
            if len(coords) not in [2,3]:
                raise decimal.InvalidOperation
            self.coords = []
            for i in coords:
                self.coords.append(decimal.Decimal(str(i)))
        except (decimal.DivisionByZero, decimal.InvalidOperation):
            raise ValueError("wrong type or length")

        self.dimensions = len(self.coords)
        self.zero = True
        for i in self.coords:
            if i != 0:
                self.zero = False
                break

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

class Vectors:
    """
    A class that takes two vectors of type Vector by me (see above for details).
    It can return them as string, calculate their dot product, their angle, check
    if they are orthogonal or kolinear and calculate their normal vector.
    """
    def __init__(self, a: Vector, b: Vector):
        if a.dimensions != b.dimensions or a.zero or b.zero:
            raise ValueError("not same dimensions or zero vector")
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

class Line:
    """
    A class that takes two vectors of type Vector by me (see above for details) that
    represent the starting point and the direction of the line.
    It can return the line as string, calculate its intersection points and its normal vector.
    """
    def __init__(self, s: Vector, r: Vector):
        if s.dimensions != r.dimensions or r.zero:
            raise ValueError("not same dimensions or zero vector as r")
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

    def probe_point(self, p: list):
        if len(point) == s.dimensions:
            point = []
            try:
                for i in point:
                    point.append(decimal.Decimal(str(i)))
            except decimal.InvalidOperation:
                raise ValueError
        else:
            return False
        i, s2, r2 = 0, self.s.coords, self.r.coords
        while i < len(r2) - 1 and r2[i] == (point[i] - s2[i]) == 0:
            i += 1
        try:
            first = (point[i] - s2[i]) / r2[i]
            for one, two, three in zip(point[i+1:], s2[i+1:], r2[i+1:]):
                if not ((one - two) == three == 0) and (one - two) / three != first:
                    return False
        except decimal.DivisionByZero:
            return False
        return True

class Lines:
    """
    A class that takes two lines of type Line by me (see above for details).
    It can calculate the relation of the two lines (parallel/identical, crossing or skew).
    It can also calculate their angle, their normal vector and if they are othogonal.
    The relation function returns an array where index 0 represents the relation:
    0: identical
    1: parallel
    2: crossing with point at index 1
    3: skew
    """
    def __init__(self, a: Line, b: Line):
        if a.s.dimensions != b.s.dimensions:
            raise ValueError("not same dimensions")
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
        left, right = [], []
        s1, s2, r1, r2 = self.a.s.coords, self.b.s.coords, self.a.r.coords, self.b.r.coords
        for x, y, a1, a2 in zip(r1, r2, s1, s2):
            left.append([x, -y])
            right.append([a2 -a1])
            
        results = Tools.solve(left[:2], right[:2])
        
        if results == [] or (len(s1) == 3 and not Tools.validate(left[2:], right[2:], results)):
            return False
        #elif len(s1) == 3 and left[-1][0] * results[0] + left[-1][1] * results[1] == right[-1]:
        else:
            point = []
            for one, two in zip(s1, r1):
                point.append(Tools.customround(one + results[0] * two, 2))
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

class Level:
    def __init__(self, s: Vector, u: Vector, v: Vector):
        if not s.dimensions == u.dimensions == v.dimensions == 3\
            or u.zero or v.zero or Vectors(u, v).kolinear():
            raise ValueError("not 3 dimensions or zero vector or parallel")
        self.s, self.u, self.v = s, u, v

    def __str__(self):
        return str(s) + " + r * " + str(u) + " + s * " + str(v)

    def cross_line(self, line: Line):
        equations = []
        for s1, u, v, s2, r in zip(self.s.coords, self.u.coords, self.v.coords, line.s.coords, line.r.coords):
            equations.append(s1 - s2 + u * abc.x + v * abc.y - r * abc.z)

        results = solve(equations, [abc.x, abc.y, abc.z])

        if results == []:
            return False
        else:
            point = []
            for s, r in zip(line.s.coords, line.r.coords):
                point.append(s + result[abc.z] * r)
            return point
