print("Enter matrix elements")
row=3
column=3
row=int(input("Enter row"))
column=int(input("enter column"))

matrix1=[[int(input()) for i in range(column)] for j in range(row)]
print(matrix1)

for i in range(row):
    for j in range(column):
result = [[0,0,0],
[0,0,0],
[0,0,0]]
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            #print(X[i])
            result[i][j] += X[i][k] * Y[k][j]
for x in result:
    print(lx)
