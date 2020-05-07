class Matrix:
    def __init__(self, a):
        self.b = '\n'.join(['\t'.join([str(j) for j in i]) for i in a])
        List = []
        for i in a:
            List.append([j for j in i])
        self.a = List

    def __str__(self):
        self.c = str(self.b)
        return self.c

    def __add__(self, other):
        mat_1 = len(self.a)
        mat_2 = len(other.a[0])
        for i in range(mat_1):
            for j in range(mat_2):
                self.a[i][j] = self.a[i][j] + other.a[i][j]
            Result = self.a
            return Matrix(Result)


mat_1 = Matrix([[1, 2], [3, 4], [5, 6]])
mat_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(mat_1 + mat_2)
