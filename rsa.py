print('Введите p[200,300]:')
p = int(input())
print('Введите q[200,300]:')
q = int(input())
n = p*q
f = (p-1)*(q-1)
print('Введите сообщение')
message = input()

    
def is_prime(k):
    if k <= 1:
        return False
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            return False
        return True
list =[]
for t in range (2,f):
    if (is_prime(t) == True) and (f%t != 0):
        list.append(t)
e = int(list[0])

list1 = []
for d in range(0,100000):
  if(d*e)%f ==1:
    list1.append(d)
d = list1[0]

#coded text

D = [(ord(x)**e)%n for x in message]

print(f"закодированное сообщение:{D}")
#encoded text

E = ''.join([chr((x**d)%n) for x in D])


print('encoded message:')
print(E)


