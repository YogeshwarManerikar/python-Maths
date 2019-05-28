#to find the inverse of a matrix using adjoint method

def minor(A,i,j):
    X=[([x for x in row])for row in A]
    X.pop(i)
    for row in X:
       row.pop(j)
    return X

def det(A):
       if len(A)==1:
            return A[0][0]
       else:
            sum=0
            for i in range(len(A[0])):
                sum=sum+((-1)**i)*A[0][i]*det(minor(A,0,i))
            return sum

def transpose(X):
    return [([row[i]for row in X])for i in range(len(X[0]))]

def scale(A,Z):
    return[([X*Z for X in row])for row in A]

def inverse(A):
    CF=[([(-1)**(i+j)*det(minor(A,i,j))for j in range(len(A[i]))])for i in
range(len(A))]
    return scale(transpose(CF),1/det(A))

def product(A,B):
    return[([sum(A[i][k]*B[k][j] for k in range(len(B)))for j in
range(len(B[0]))])for i in range(len(A))]

A=[[0,0,1],[0,1,2,],[1,1,5]]

print('Matrix A: \n',A)
print('\n Inverse of A:\n',inverse(A))
print('\n Identity Matrix of A: \n',product(A,inverse(A)))
       
