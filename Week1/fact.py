def factorial():
    n = input('Please input the number: ')
    n = int(n)
    if n < 0:
        print('invalid number, must be larger or equal to 0')
        return
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
    return result

if __name__ == '__main__':
    output = factorial()
    print('result is: ', output)