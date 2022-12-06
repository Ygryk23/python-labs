list = [1,2,3,4,4,5,6,6,7,7,8,9,9,7,6,9,9,32,43,45]
result = []
def odd_index(list):
    for i in range(len(list)):
        if i % 2 == 0:
            result.append(list[i])
    print(result)
odd_index(list)






a = [1,5,32,1,5,67,45,23,45,6,7,89]
c= []
for i in range(len(a) - 1):
    n = a[i]
    i += 1
    m = a[i]
    if m > n:
        c.append(m)
print(c) 







list = [1,2,3,4,5,6,7,8,9,10]
def replacement(list):
    i_of_max_el = list.index(max(list))
    i_of_min_el = list.index(min(list))
    list[i_of_max_el], list[i_of_min_el] = list[i_of_min_el], list[i_of_max_el]
    print(list)
replacement(list)







k = {1: 'hello', 2: 'is anyone here?', 3: 'how are you?', 4: 'ku'}
key = int(input('Введите ключ, чтобы получить его значение: '))
def get_value(dictionary):
    value = dictionary.get(key)
    print(value)
get_value(k)