def sum_of_numbers():
    n = input('Please input the maximum number: ')
    n = int(n)
    if n < 1:
        print('Invalid number, must be larger or equal than 1')
    else:
        i = 1
        even_sum = 0
        odd_sum = 0
        while i <= n:
            if i % 2 == 0:
                even_sum += i
            else:
                odd_sum += i
            i += 1
        print('sum of even numbers:', even_sum)
        print('sum of odd numbers:', odd_sum)
    
if __name__ == '__main__':
    sum_of_numbers()
        