from math import factorial
 
X=float(input('the values of X:'))
x=[1,3,5,7,9]
y=[5,6,7,4,9]
n=len(x)-1 
h=x[1]-x[0]
p=(X-x[n])/h

def delta(i,j):
	if i>=2: return delta(i-1,j+1)-delta(i-1,j)
	elif i==1:return y[j+1]-y[j]
	elif i==0: return y[j]

	
sum=0
i=0
while i<len(x):
	j=0
	product=1
	while j<i:
		product=product*(p+j)
		j=j+1
	sum=sum+((product*delta(i,n-i))/factorial(i))
	i=i+1

	
print('y[{}]={}'. format(X,sum))
input('enter')

