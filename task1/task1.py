import sys

def procentile(list, P):
    P = P / 100
    index = (P * (len(list) - 1))
    b1 = int(index)
    b2 = index - int(index)
    result = list[b1] + b2 * (list[b1 + 1] - list[b1])
    return result

def main():
    numbers =[]
    with open(sys.argv[1], 'r', encoding='utf8') as file:
        for i in file:
            numbers.append(int(i))
    numbers.sort()
    print('{:.2f}'.format(procentile(numbers, 90)))
    print('{:.2f}'.format(procentile(numbers, 50)))
    print('{:.2f}'.format(numbers[-1]))
    print('{:.2f}'.format(numbers[0]))
    print('{:.2f}'.format(sum(numbers) / len(numbers)))

if __name__ == '__main__':
    main()
