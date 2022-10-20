from webbrowser import get


a = True
b = False

print(a and b)
print((a and b) or b)
print((a and b) or not(a and b))
print((a and b) or not(a or b) or b)
print(b and b) or not (a and (a or b or a) or not(a or b)) 
print(1<<2)
print(1 & 0 | 1>>1)
print(1 & 0 | 1>>0)
print(0b101 & 0b111 ^ 0b111 | 0b010)



A = int(input(''))
B = int(input(''))

if A > B:
    print(B)
else:
    print(A) 



N = int(input(''))
M = int(input('')) 
K = int(input('')) 

result = max(N, M, K) 
print("The maximum number is:", result)



x = int(input(''))
y = int(input('')) 
z = int(input('')) 

numbers = set([x, y, z])
print(numbers)












  





