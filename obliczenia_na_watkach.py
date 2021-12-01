import timeit
from concurrent.futures import ProcessPoolExecutor

liczby = [
    159,

]

def sigmasum(n):
    sum = 0
    for i in range(1, n):
        sum += (n - i) * i
    return sum

def main():
    with ProcessPoolExecutor(max_workers=4) as executor:
        output = executor.map(sigmasum, liczby)
    str_output = [str(x) for x in output]
    print("Wyniki:", ' '.join(str_output))

if __name__ == '__main__':
    main()