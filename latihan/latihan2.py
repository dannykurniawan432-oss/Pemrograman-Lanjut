
from functools import reduce
list_data = [1,2,3,4,5,6,7,8,9]

hasil_map = list(map(lambda x: x * 2, list_data))

hasil_filter = list(filter(lambda x: x % 4 == 0, hasil_map))


hasil_reduce = reduce(lambda x, y: x + y, hasil_filter)


print("Data awal:", list_data)
print("Hasil Map:", hasil_map)
print("Hasil Filter:", hasil_filter)
print("Hasil Reduce:", hasil_reduce)