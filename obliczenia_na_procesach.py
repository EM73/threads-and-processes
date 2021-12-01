




def sigmasum(n):
    sum = 0
    for i in range(1,n):
        sum += (n-i)*i
    return sum


print(sigmasum(3))