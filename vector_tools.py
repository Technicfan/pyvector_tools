from decimal import Decimal, InvalidOperation, Overflow
from math import acos, degrees
from copy import deepcopy as copy

class Tools:
    def customround(number, decimals=None):
        rounded = float(round(number, decimals))
        if rounded - int(number) != 0:
            return rounded
        else:
            return int(number)

    def solve(A, b, floating=False) -> list:
        """
        a function that solves a linear equation system 
        of the form Ax = b using gaussian elimination
        - it takes two matrices which represent the equations with the first being non singular
        - the number of the equations must be the same or bigger as the number of coefficients
        - it returns a matrix in form of a list of decimal.Decimal 
          or float if third parameter is True
        example:
            A = [[9,3,4],
                 [4,3,4],
                 [1,1,1]]
            b = [[7],
                 [8],
                 [3]]
                -> returns [[-0.2], 
                            [ 4  ], 
                            [-0.8]]
        """
        # check if all lists have the same length
        invalid = False
        for i in range(len(A)):
            if len(A) < len(A[i]) or len(b[i]) != 1:
                invalid = True
                break
        if len(A) != len(b) or invalid:
            raise ValueError("invalid matrix sizes")

        # copy input to a single iwth the needed length array to work with
        length = len(A[0])
        matrix = copy(A[:length])
        for i in range(length):
            matrix[i].append(b[i][0])
            matrix[i] = list(map(Decimal, matrix[i]))

        # make sure first item not 0
        # and if not possible exit
        for i in range(1, length):
            if matrix[0][0] == 0:
                matrix[0], matrix[i] = matrix[i], matrix[0]
            else:
                break
        if matrix[0][0] == 0:
            return []

        # make gauss magic happen :)
        try:
            for i in range(length):
                for line in range(length):
                    top, bottom = matrix[i][i], matrix[line][i]
                    for row in range(length + 1):
                        matrix[line][row] *= top
                        matrix[line][row] -= bottom * matrix[i][row]
        except Overflow:
            raise Overflow("system is to big")

        # reverse everything for easier solving
        matrix.reverse()
        for i in range(length):
            matrix[i].reverse()
        # solve the resulting system
        results = []
        for i in range(length):
            result = matrix[i][0]
            for j in range(i):
                result -= matrix[i][j + 1] * results[j][0]
            if matrix[i][i + 1] != 0:
                results.append([result / matrix[i][i + 1]])
            else:
                return []
        results.reverse()

        # return results and convert them to float if needed
        if A[length:] == [] or Tools.validate(A[length:], b[length:], results):
            if floating:
                return [[float(i[0])] for i in results]
            else:
                return results
        else:
            return []

    def validate(A, b, r) -> bool:
        """
        check if result of solve() (above) is true
        input the two matrices like above and the results
        to check in the same form
        """
        invalid = False
        try:
            for i in range(len(A)):
                if len(A[i]) != len(r) or len(b[i]) != 1:
                    invalid = True
                    break
        except IndexError:
            invalid = True
        for i in r:
            if len(i) != 1:
                invalid = True
        if invalid:
            return False
        for eq, res in zip(A, b):
            result = 0
            for i in range(len(eq)):
                result += eq[i] * r[i][0]
            if abs(result - res[0]) > Decimal('1e-10'):
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
                raise InvalidOperation
            self.coords = [Decimal(str(i)) for i in coords]
        except InvalidOperation:
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
            return Tools.customround(under**Decimal(0.5), 2)
        else:
            return under**Decimal(0.5)

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
    It can return them as string, calculate their dot and cross product, their angle, check
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

    def cross_product(self):
        a, b = self.a, self.b
        if a.dimensions == 3:
            x = Tools.customround(a.coords[1] * b.coords[2] - a.coords[2] * b.coords[1], 2)
            y = Tools.customround(a.coords[2] * b.coords[0] - a.coords[0] * b.coords[2], 2)
            z = Tools.customround(a.coords[0] * b.coords[1] - a.coords[1] * b.coords[0], 2)
            return Vector([x, y, z])
        else:
            return None

    def orthogonal(self):
        return self.dot_product() == 0

    def angle(self):
        return Tools.customround(degrees(acos(self.dot_product(False) /\
                 (self.a.length(False) * self.b.length(False)))), 2)

    def small_angle(self):
        return Tools.customround(degrees(acos(abs(self.dot_product(False) /\
                 (self.a.length(False) * self.b.length(False))))), 2)

    def kolinear(self):
        left, right = [[i] for i in self.a.coords], [[i] for i in self.b.coords]
        return Tools.solve(left, right) != []

    def normal_vector(self):
        if self.kolinear():
            return self.a.normal_vector()
        elif self.a.dimensions == 3:
            return self.cross_product()
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
                    point.append(Decimal(str(i)))
            except InvalidOperation:
                raise ValueError("wrong input type")
        else:
            return False
        right = []
        left = [[i] for i in self.r.coords]
        for s, p in zip(self.s.coords, point):
            right.append([p - s])
        return Tools.solve(left, right) != []

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
        left, right = [[i] for i in self.b.r.coords], []
        for s1, s2 in zip(self.a.s.coords, self.b.s.coords):
            right.append([s1 - s2])
        return Tools.solve(left, right) != []

    def crossing(self):
        left, right = [], []
        s1, s2, r1, r2 = self.a.s.coords, self.b.s.coords, self.a.r.coords, self.b.r.coords
        for x, y, a1, a2 in zip(r1, r2, s1, s2):
            left.append([x, -y])
            right.append([a2 - a1])

        results = Tools.solve(left, right)

        if results == []:
            return False
        else:
            point = []
            for one, two in zip(s1, r1):
                point.append(Tools.customround(one + results[0][0] * two, 2))
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
        if self.crossing():
            return Vectors(self.a.r, self.b.r).angle()
        else:
            return None

    def small_angle(self):
        if self.crossing():
            return Vectors(self.a.r, self.b.r).small_angle()
        else:
            return None

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

    def probe_line(self, line: Line):
        left, right = [], []
        for s1, u, v, s2, r in zip(self.s.coords, self.u.coords, self.v.coords, line.s.coords, line.r.coords):
            left.append([u, v, -r])
            right.append([s2 - s1])

        results = Tools.solve(left, right)

        if results == []:
            return False
        else:
            point = []
            for s, r in zip(line.s.coords, line.r.coords):
                point.append(s + result[2][0] * r)
            return point
