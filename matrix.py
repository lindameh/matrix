# function sum
def sum(a,b):
    if len(a)!=len(b) or len(a[0])!=len(b[0]):
        return "NA"
    else:
        c = []
        for i in range(len(a)):
            row = []
            for j in range(len(a[0])):
                row.append(a[i][j]+b[i][j])
            c.append(row)
        return c

# function product
def product(a,b):
    if len(a)!=len(b[0]) or len(a[0])!=len(b):
        return "NA"
    else:
        c = []
        for i in range(len(a)):
            row = []
            for j in range(len(a)):
                total = 0
                for k in range(len(b)):
                    total += a[i][k]*b[k][j]
                row.append(total)
            c.append(row)
        return c

# input matrix 1                
print("Matrix 1")
while True:
    m1 = input("Enter m: ")
    if m1=="-1":
        break
    if m1.isdigit():
        m1 = int(m1)
        if 1<=m1<=5:
            break
        else:
            print("Cannot! Try again.")
    else:
        print("Cannot! Try again.")
while True:
    n1 = input("Enter n: ")
    if m1=="-1" and n1=="-1":
        break
    if n1.isdigit():
        n1 = int(n1)
        if 1<=n1<=5:
            break
        else:
            print("Cannot! Try again.") 
    else:
       print("Cannot! Try again.")
if m1=="-1" and n1=="-1":
    print("Bye")
    exit()

# input matrix 2  
print("Matrix 2")
while True:
    m2 = input("Enter m: ")
    if m2.isdigit():
        m2 = int(m2)
        if (m2==m1 or m2==n1) and 1<=m2<=5:
            break
        else:
            print("Cannot! Try again.")
    else:
        print("Cannot! Try again.")
while True:
    n2 = input("Enter n: ")
    if n2.isdigit():
        n2 = int(n2)
        if (m2,n2==m1,n1 or m2,n2==n1,m1) and 1<=n2<=5:
            break
        else:
            print("Cannot! Try again.")
    else:
        print("Cannot! Try again.")      

# generate matrix 1 and print
import random
a=[]
print("Matrix 1")
for i in range(m1):
    a.append([])
    for j in range(n1):
        num = random.randint(1,20)
        a[i].append(num)
        print("{0:>3}".format(num),end = "")
    print("")

# generate matrix 2 and print
b=[]
print("Matrix 2")
for i in range(m2):
    b.append([])
    for j in range(n2):
        num = random.randint(1,20)
        b[i].append(num)
        print("{0:>3}".format(num),end = "")
    print("")

# print sum
print("Sum")
c = sum(a,b)
if c == "NA":
    print("NA")
else:
    for i in range(m1):
        for j in range(n1):
            print("{0:>3}".format(c[i][j]),end = "")
        print("")

# print product
print("Product")
d = product(a,b)
if d == "NA":
    print("NA")
else:
    for i in range(m1):
        for j in range(m1):
            print("{0:>4}".format(d[i][j]),end = "")
        print("")
