import timeit
from statistics import median

from html_with_class import *

setup = '''
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
def sigmasum(n):
    sum = 0
    for i in range(1, n):
        sum += (n - i) * i
    return sum
liczby = [
    15972490,
    80247910,
    92031257,
]
'''
sigma_one_thread = '''
with ThreadPoolExecutor(max_workers=1) as executor:
    executor.map(sigmasum, liczby)
'''
sigma_four_thread = '''
with ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(sigmasum, liczby)
'''
sigma_four_process = '''
with ProcessPoolExecutor(max_workers=4) as executor:
    executor.map(sigmasum, liczby)
'''
sigma_default_process = '''
with ProcessPoolExecutor(max_workers=None) as executor:
    executor.map(sigmasum, liczby)
'''


def main():

    results=[]
    for i in range(3):
        loop_results = []
        loop_results.append(timeit.timeit(stmt=sigma_one_thread, setup=setup, number=1))
        loop_results.append(timeit.timeit(stmt=sigma_four_thread, setup=setup, number=1))
        loop_results.append(timeit.timeit(stmt=sigma_four_process, setup=setup, number=1))
        loop_results.append(timeit.timeit(stmt=sigma_default_process, setup=setup, number=1))

        results.append(loop_results)


        #four_process.append(timeit.timeit(stmt=sigma_four_process, setup=setup, number=1))
        #default_process.append(timeit.timeit(stmt=sigma_default_process, setup=setup, number=1))

    median_results = []
    for j in range(len(results[0])):
        loop_results = []
        for k in range(len(results)):
            loop_results.append(results[k][j])
        median_results.append(median(loop_results))


    r1 = RaportBuilder()
    r1.header()
    r1.enviro()
    r1.table_results(results, ["Execution:", "1 thread (s)", "4 threads (s)", "1 process", "Default processes"])
    print(median_results)
    r1.table_results(median_results, ["Execution:", "1 thread (s)", "4 threads (s)", "1 process", "Default processes"])
    r1.footer()

    file_appender(r1.get_template(), output_html_path)


if __name__ == '__main__':

    main()