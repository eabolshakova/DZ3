import time


def sum(counts):
    result = 0
    for count in counts:
        result += count
    return result


def multiplication(counts):
    result = 1
    for count in counts:
        result *= count
    return result


def minimum(counts):
    result = counts[0]
    for count in counts:
        if count < result:
            result = count
    return result


def maximun(counts):
    result = counts[0]
    for count in counts:
        if count > result:
            result = count
    return result


file_name = 'test6.txt'

with open(file_name, 'r') as file:
    counts = []
    for line in file:
        counts += list(map(int, line.split()))
    start = time.time()
    print('В файле:', str(counts)[1:-1])
    print('Минимальное:', minimum(counts))
    print('Максимальное:', maximun(counts))
    print('Сумма:', sum(counts))
    print('Произведение: ', multiplication(counts))
    end = time.time()
    print('Время работы: ', round(end - start, 3))
