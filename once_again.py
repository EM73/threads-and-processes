from concurrent.futures import ThreadPoolExecutor
import timeit

def sigmasum(n):
    sum = 0
    for i in range(1,n):
        sum += (n-i)*i
    return sum

liczby = [
        15972490,
        80247910,
        92031257,
        75940266,
        97986012,
        87599664,
        75231321,
        11138524,
        68870499,
        11872796,
        79132533,
        40649382,
        63886074,
        53146293,
        36914087,
        62770938,
    ]

sigma_one_thread = '''
with ThreadPoolExecutor(max_workers=1) as executor:
    executor.map(sigmasum, liczby)
'''

sigma_four_thread = '''
with ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(sigmasum, liczby)
'''

setup = '''
from concurrent.futures import ThreadPoolExecutor
def sigmasum(n):
    sum = 0
    for i in range(1,n):
        sum += (n-i)*i
    return sum

liczby = [
        15972490,
        80247910,
    ]
'''



#print(timeit.timeit(stmt=sigma_one_thread, setup=setup, number=1))
print(timeit.timeit(stmt=sigma_four_thread, setup=setup, number=1))
print(timeit.timeit(stmt=sigma_four_thread, setup=setup, number=1))


