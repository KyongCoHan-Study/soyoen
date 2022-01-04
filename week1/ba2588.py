# 곱셈


a = input()
b = input()

li_a = list(map(int, a))
li_b = list(map(int, b))

first = int(a)*li_b[-1]
second = int(a)*li_b[-2]
third = int(a)*li_b[-3]

print(first)
print(second)
print(third)
print(first+(second*10)+(third*100))

'''
a = int(input())
b = int(input())

print(a * (b%10))
print(a * ((b%100)//10))
print(a * (b//100))
print(a * b)
'''