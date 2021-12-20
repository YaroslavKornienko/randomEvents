import random

# a = input("Первое coбытие = ")
# b = input("Второе coбытие = ")
#
# if random.randint(int(a), int(b)) <= 50:
#     print('hex')
#     print(a, b)
#
# else:
#     print('oct')
#     print('lvl')

a = 0.12
b = 0.43
c = 0.24
d = 0.12
e = 0.234
arr_events = [0.15, 0.15, 0.1, 0.1, 0.2]
probability = []
k = 10
r1 = arr_events[0]
index_arr = 0
print(probability)
count_arr = len(arr_events)


def probability_func(arr, count):
    arr_new = []
    new = 0
    for i in range(count):
        print(i-1)
        new = arr[i] + new
        arr_new.append(new)
    print(arr_new)
    if arr_new[count-1] < 1.0:
        print('a')
        new_event = 1.0 - arr_new[count-1]
        arr_new.append(new_event + new)
    return arr_new


def error_number_1(arr, count):
    global k
    if arr[count-1] > 1.0:
        k = 0
        print('Помилка  #1\nВведіть інші ймовірності')


def real_event(i, index):
    global r1, index_arr, probability
    if i <= r1:
        print(r1)
        # print(index, 'index')
        index_arr = 0
        r1 = probability[0]
        # print(index_arr, 'asd')
    else:
        print(index)
        index += 1
        r1 = probability[index]
        real_event(i, index)


probability = probability_func(arr_events, count_arr)
error_number_1(probability, count_arr)
print(probability)
while k:
    k -= 1

    r = random.random()
    print(r)
    real_event(r, index_arr)


