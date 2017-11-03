from sys import stdin


class MatrixError(BaseException):
    def __init__(self, m1, m2):
        self.matrix1 = m1
        self.matrix2 = m2


class Matrix:
    def __init__(self, matrix):
        # создание копии
        self.M = list(map(list, matrix))

    def __str__(self):
        s = list()
        for row in self.M:
            s.append('\t'.join(map(str, row)))
        return '\n'.join(s)

    def size(self):
        return len(self.M), len(self.M[0])

    def __add__(self, other):
        if self.size() == other.size():
            rows = list()
            (c, r) = self.size()
            for i in range(c):
                line = list()
                for j in range(r):
                    line.append(self.M[i][j] + other.M[i][j])
                rows.append(line)

            return Matrix(rows)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        rows = list()
        (c, r) = self.size()
        for i in range(c):
            line = list()
            for j in range(r):
                line.append(self.M[i][j] * other)
            rows.append(line)
        return Matrix(rows)

    __rmul__ = __mul__

    def transpose(self):
        tM = list()
        (c, r) = self.size()
        for j in range(r):
            line = list()
            for i in range(c):
                line.append(self.M[i][j])
            tM.append(line)
        self.M = tM
        return self

    @staticmethod
    def transposed(x):
        tM = list()
        (c, r) = x.size()
        for j in range(r):
            line = list()
            for i in range(c):
                line.append(x.M[i][j])
            tM.append(line)
        return Matrix(tM)


# m1 = [[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]]
# m = Matrix(m1)
# m1[0][0] = 0
# print(m)

exec(stdin.read())
