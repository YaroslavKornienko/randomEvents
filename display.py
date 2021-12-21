import matplotlib.pyplot as plt
import numpy as np

roman_numerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
dictionary_I = {0.11:12, 1.11:12, 2.11:4,3.11:8 ,0.41:11,4.11:12,5.11:12 }
k = len(dictionary_I)
values_arr = []
for key in dictionary_I:
    print("key: %s , value: %s" % (key, dictionary_I[key]))


def check_dict(number_dict):
    if number_dict >= 1.000001:
        print(number_dict)
        number_dict -= 1.0
        print('aa')
        print(number_dict)
        return check_dict(number_dict)

    else:
        pass

    return number_dict


if k <= 7:
    number = 0
    for key in dictionary_I:
        key = check_dict(key)
        print(type(key))
        key = round(key, 2)
        values_arr.append('      ' + str(roman_numerals[number]) + ' (' + str(key) + ')')

        number += 1
else:
    number = 0
    for key in dictionary_I:
        key = check_dict(key)
        print(type(key))
        key = round(key, 2)
        values_arr.append(str(roman_numerals[number]))

        number += 1


index = np.arange(k)
plt.bar(index, dictionary_I.values())
plt.xticks(index, values_arr)
plt.show()
